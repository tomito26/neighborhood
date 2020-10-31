from django.conf.urls import url
from django.urls import path
from estate import views

urlpatterns = [
    path('',views.home,name='home')
]
