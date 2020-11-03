from django import forms
from django.forms import fields
from .models import Business, Post

class BusinessForms(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model =  Business
        fields = ['name','email','business_image','location']


class PostForms(forms.ModelForm):
    class Post:
        fields = ['post']