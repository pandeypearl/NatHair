"""
    Module for Product application forms.
"""
from django import forms
from .models import HairProductReview

#Product Review form
class HairProductReviewForm(forms.ModelForm):
    '''
        Hair Product review form for user input.
    '''
    class Meta:
        model = HairProductReview
        fields = [
            'rate_value',
            'comment',
        ]
       
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Add your comment here.'}),
        help_text='Leave a helpful comment about your experience using this product.',
    )