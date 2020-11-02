from django import forms
from django.forms import fields
from .models import Business, Post

class BusinessForms(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model =  Business
        fields = ['business_name','email','business_image']


class PostForms(forms.ModelForm):
    class Post:
        fields = ['post']