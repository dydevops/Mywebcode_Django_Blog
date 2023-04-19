from django.core import validators
from django import forms
from .models import Contact

      
class ComplainForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=[
            'name','email','phone','subject',
        ]
        widgets = {
        'message':forms.Textarea(attrs={'rows': 3, 'cols': 30})
        }      