from django import forms
from .models import HairRoutine, RoutineStep
from products.models import HairProduct


class HairRoutineForm(forms.ModelForm):
    class Meta:
        model = HairRoutine
        fields = [
            'name',
            'description',
            'notes',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Routine Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Routine Description'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Additional Notes'}),
        }

    def clean_name(self):
        ''' Field level validation ensuring name is not empty. '''
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Routine name cannot be empty.")
        return name


class RoutineStepForm(forms.ModelForm):
    class Meta:
        model = RoutineStep
        fields = [
            'title',
            'description',
            'product',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Routine Step Title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Routine Step Description'}),
            'product': forms.Select(help_text='Select the product you use for this step.'),
        }

    def clean_title(self):
        ''' Field level validation ensuring title is not empty. '''
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Routine step title cannot be empty.")
        return title
    
    def clean_product(self):
        ''' Field level validation ensuring product is not empty. '''
        product = self.cleaned_data.get('product')
        if not product:
            raise forms.ValidationError("Product used cannot be empty.")
        return product
    
class DeleteRoutineStepForm(forms.ModelForm):
    class Meta:
        model = RoutineStep
        fields = []

    routine_step_id = forms.IntegerField(widget=forms.HiddenInput())