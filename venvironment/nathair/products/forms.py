"""
    Module for Product application forms.
"""
from django import forms
from .models import ProductReview

#Product Review form
class ProductReviewForm(forms.ModelForm):
    """
        Product review form for user input.
    """
    rate_value = forms.MultipleChoiceField(required=True)
    comment = forms.CharField(max_length=2024, required=True)

    class Meta:
        model = ProductReview
        fields = [
            'rate_value',
            'comment',
            'post',
        ]