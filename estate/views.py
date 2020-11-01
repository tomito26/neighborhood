from django.shortcuts import render
from .models import Business
from django.views.generic  import ListView,DetailView,CreateView

# Create your views here.

class BusinessListView(ListView):
    model = Business
    template_name= 'estate/home.html'
    context_object_name = 'businesses'
    
    
class BusinessDetailView(DetailView):
    model = Business
    
class BusinessCreateView(CreateView):
    model = Business
    
    fields = ['business_name','email','business_image']