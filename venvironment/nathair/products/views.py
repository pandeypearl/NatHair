from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import View, CreateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from .models import Product, ProductReview
from .forms import ProductReviewForm
from django.urls import reverse
import requests
import json
from django.contrib.sessions.models import Session
from .models import Product, HairProduct


# Create your views here.

# Home Page
class HomeView(ListView):
    template_name = 'home.html'
    model = Product

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

    context = {
        'product': product,
    }

    return render(request, template, context)


class ProductView(CreateView):
    """
        Class based view to read json data, save data to product
        model, and display product list in template.
    """
    template_name = 'products.html'
    def get(self, request, *args, **kwargs):
        
        # read the JSON
        url = 'https://nathair-product-api.onrender.com/products/'
        headers = {
            'Accepts': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0'
        }
        session = requests.session()
        session.headers.update(headers)
        response = session.get(url)
        products = response.json()
        # Create product model object for each object in the JSON
        for product in products:
            Product.objects.create(
                                    brand=product['brand'],
                                    title=product['title'],
                                    url=product['url'],
                                    image=product['image'],
                                    price=product['price']
                                    )
        # passing product dict as b template context
        context = {'products': Product.objects.all()}
        return render(request, self.template_name, context)

class ProductDetailView(FormMixin, DetailView):
    """
        class based view to show individual product details and allow
        users to rate and comment on individual product.
    """
    # model used 
    model = Product
    template_name = 'product-detail.html'
    form_class = ProductReviewForm

    def get_success_url(self):
        return reverse('product-detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['form'] = ProductReviewForm(initial={'product': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def for_valid(self, form):
        form.save()
        return super(ProductDetailView, self).form_valid(form)

    