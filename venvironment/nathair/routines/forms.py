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

    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Routine Name'}),
        help_text='Please name your routine eg. \"Summer hair routine\".',
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Routine Description'}),
        help_text='Please provide a description for your routine, eg. \"My full summer hair routine including wash day and styling\".'
    )

    notes = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Additional Notes'}),
        help_text='Any additional text to help your routine be more understandable.'
    )

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
        }

    product = forms.ModelChoiceField(
        queryset=HairProduct.objects.all(),
        help_text='Select the product you use for this step'
    )
    
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