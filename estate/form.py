from django import forms
from django.forms import fields
from .models import Business

class BusinessForms(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model =  Business
        fields = ['business_name','email','business_image']