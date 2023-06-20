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
    rate_value = forms.ChoiceField(label="Rating", required=True, widget=forms.RadioSelect())
    comment = forms.Textarea()

    class Meta:
        model = ProductReview
        fields = [
            'rate_value',
            'comment',
        ]