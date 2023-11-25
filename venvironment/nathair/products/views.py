from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import View, CreateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse
import requests
import json
from django.contrib.sessions.models import Session
from .models import HairProduct, SavedHairProduct, HairProductReview
from .forms import HairProductReviewForm


# Create your views here.

# Home Page
class HomeView(ListView):
    template_name = 'home.html'
    model = HairProduct

    def get_queryset(self, *args, **kwargs):
        products = super(HomeView, self).get_queryset(*args, **kwargs)
        products = products.order_by("-id")
        return products


@login_required(login_url='login')
def product_list(request):
    '''
        View to read json data, save data to product
        model, and display product list in template.
    '''
    template = 'product_list.html'

    url = 'https://nathair-product-api.onrender.com/products/'
    headers = {
        'Accepts': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0'
    }
    session = requests.session()
    session.headers.update(headers)
    response = session.get(url)
    products = response.json()

    for product in products:
        existing_product = HairProduct.objects.filter(
            brand=product['brand'],
            title=product['title'],
            url=product['url'],
            image=product['image'],
            price=product['price'],
        ).first()

        if not existing_product:
            HairProduct.objects.create(
                brand=product['brand'],
                title=product['title'],
                url=product['url'],
                image=product['image'],
                price=product['price'],
            )
    
    context = {
        'products': HairProduct.objects.all()
    }
    return render(request, template, context)


@login_required(login_url='login')
def product_detail(request, product_id):
    template = 'product_detail.html'
    product = get_object_or_404(HairProduct, id=product_id)
    saved_product_count = product.num_saves()
    product_reviews = HairProductReview.objects.filter(product=product)
    average_rating = product.average_rating()
    # Check if the user has already reviewed the product
    user_reviewed = HairProductReview.objects.filter(user=request.user, product=product).exists()
    form = HairProductReviewForm(request.POST)

    if request.method == 'POST':
        # Preventing second review form same user
        if user_reviewed:
            messages.warning(request, 'You hve already reviewed this product')
            return redirect('product_detail', product_id=product_id)

        form = HairProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.rate_value = form.cleaned_data['rate_value']
            review.comment = form.cleaned_data['comment']
            review = HairProductReview.objects.create(
                user=request.user,
                product=product,
                rate_value=review.rate_value,
                comment=review.comment,
            )
            review.save()
            messages.success(request, 'Product rating has been added successfully')
            return redirect('product_detail', product_id=product_id)
        else:
            messages.warning(request, 'Something went wrong. Please try again')
    else:
        form = HairProductReviewForm()

    context = {
        'product': product,
        'saved_product_count': saved_product_count,
        'average_rating': average_rating,
        'form': form,
        'product_reviews': product_reviews,
    }

    return render(request, template, context)


@login_required(login_url='login')
def save_product(request, product_id):
    product = get_object_or_404(HairProduct, id=product_id)

    if not SavedHairProduct.objects.filter(user=request.user, product=product).exists():
        SavedHairProduct.objects.create(user=request.user, product=product)
        messages.success(request, 'Product saved successfully.')
    else:
        messages.warning(request, 'You have already saved this product.')
    return redirect('product_detail', product_id=product_id)


@login_required(login_url='login')
def saved_products(request):
    template = 'saved_products.html'
    saved_products = SavedHairProduct.objects.filter(user=request.user)
    context = {
        'saved_products':saved_products,
    }
    return render(request, template, context)


@login_required(login_url='login')
def unsave_product(request, product_id):
    saved_product = get_object_or_404(SavedHairProduct, user=request.user, product__id=product_id)
    saved_product.delete()
    return redirect('saved_products')


# class ProductView(CreateView):
#     """
#         Class based view to read json data, save data to product
#         model, and display product list in template.
#     """
#     template_name = 'products.html'
#     def get(self, request, *args, **kwargs):
        
#         # read the JSON
#         url = 'https://nathair-product-api.onrender.com/products/'
#         headers = {
#             'Accepts': 'application/json',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0'
#         }
#         session = requests.session()
#         session.headers.update(headers)
#         response = session.get(url)
#         products = response.json()
#         # Create product model object for each object in the JSON
#         for product in products:
#             Product.objects.create(
#                                     brand=product['brand'],
#                                     title=product['title'],
#                                     url=product['url'],
#                                     image=product['image'],
#                                     price=product['price']
#                                     )
#         # passing product dict as b template context
#         context = {'products': Product.objects.all()}
        # return render(request, self.template_name, context)

# class ProductDetailView(FormMixin, DetailView):
#     """
#         class based view to show individual product details and allow
#         users to rate and comment on individual product.
#     """
#     # model used 
#     model = HairProduct
#     template_name = 'product-detail.html'
#     form_class = ProductReviewForm

#     def get_success_url(self):
#         return reverse('product-detail', kwargs={'pk': self.object.id})

#     def get_context_data(self, **kwargs):
#         context = super(ProductDetailView, self).get_context_data(**kwargs)
#         context['form'] = ProductReviewForm(initial={'product': self.object})
#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

#     def for_valid(self, form):
#         form.save()
#         return super(ProductDetailView, self).form_valid(form)

    