from estate.views import BusinessCreateView, BusinessDetailView, BusinessListView
from django.conf.urls import url
from django.urls import path
from estate import views

urlpatterns = [
    path('',BusinessListView.as_view(),name='home'),
    path('business/<int:pk>/',BusinessDetailView.as_view(), name='business-detail'),
    path('business/new/', BusinessCreateView.as_view(), name='business-create'),
]
