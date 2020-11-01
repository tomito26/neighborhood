from estate.views import BusinessListView
from django.conf.urls import url
from django.urls import path
from estate import views

urlpatterns = [
    path('',BusinessListView.as_view(),name='home')
]
