from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields=['title', 'description', 'amount']

    def clean(self, *args, **kwargs):
        data=self.cleaned_data
        content=data.get('description', None)
        if content == '':
            content=None
        if content is None:
            raise forms.ValidationError('Заполните поле content')
        return super().clean(*args, **kwargs)