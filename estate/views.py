from django.shortcuts import render
from .models import Business
from django.views.generic  import ListView

# Create your views here.

class BusinessListView(ListView):
    model = Business
    template_name= 'estate/home.html'
    context_object_name = 'businesses'
    
