from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class HairProduct(models.Model):
    brand = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    url =  models.URLField()
    image = models.URLField()
    price = models.CharField(max_length=20)

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"

    def num_saves(self):
        return self.savedhairproduct_set.count()

    def __str__(self):
        return '%s - %s' % (self.title, self.brand)

    def get_absolute_url(self):
        return reverse("product_detail", args=[str(self.id)])


class HairProductReview(models.Model):
    '''
        Model representing user rating for one product
        @ product: Product review associated with.
        @ value: Rating value.
        @ comment: Reviewer's comment on the product.
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(HairProduct, on_delete=models.CASCADE)
    review_date = models.DateTimeField(auto_now_add=True, verbose_name='Review Date')
    # Specifying rating choices
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    rate_value = models.IntegerField(choices=RATING_CHOICES, default=1)
    comment = models.TextField(max_length=2024)

    class Meta:
        verbose_name = "product_review"
        verbose_name_plural = "products_reviews"

    def __str__(self):
        return '%s - %s - %s' % (self.product, self.rate_value, self.user)
    

class SavedHairProduct(models.Model):
    ''' Represents the relationship between users and saved products '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(HairProduct, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.user, self.product)


# class Product(models.Model):
#     """
#         Class product model to store JSON data from our
#         NatHairAPI.
#     """
#     brand = models.CharField(max_length=250)
#     title = models.CharField(max_length=250)
#     url = models.URLField()
#     image = models.URLField()
#     price = models.CharField(max_length=20)

#     class Meta:
#         verbose_name = "product"
#         verbose_name_plural = "products"

#     def __str__(self):
#         return '%s %s' % (self.title, self.brand)

#     def get_absolute_url(self):
#         return reverse("product_detail", args=[str(self.id)])
    
    
# class ProductReview(models.Model):
#     """
#         Model representing user rating for one product
#         @ product: Product review associated with.
#         @ value: Rating value.
#         @ comment: Reviewer's comment on the product.
#     """
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     review_date = models.DateTimeField(auto_now_add=True, verbose_name='Review Date')
#     # Specifying rating choices
#     RATING_CHOICES = (
#         (1, '1'),
#         (2, '2'),
#         (3, '3'),
#         (4, '4'),
#         (5, '5'),
#     )
#     rate_value = models.IntegerField(choices=RATING_CHOICES, default=1)
#     comment = models.TextField(max_length=2024)

#     class Meta:
#         verbose_name = "product_review"
#         verbose_name_plural = "products_reviews"

#     def __str__(self):
#         return '%s %s' % (self.product, self.rate_value, self.user)
    


