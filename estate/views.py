from django.shortcuts import render
from .models import Business

# Create your views here.
def home(request):
    business = Business.objects.all()
    title = 'Hood - Welcome to hood get the latest updates in your neighborhood '
    
    context = {
        'title':title
    }
    return render(request,'estate/home.html')
    
