from django import forms

from .models import User,Category,Listing,Logs

class ProductForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields=['brand','model','description']
        widgets = {
            'brand': forms.TextInput(attrs={'class':'form-control'}),
            'model': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
        }