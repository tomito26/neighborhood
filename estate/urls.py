from estate.views import BusinessCreateView, BusinessDeleteView, BusinessDetailView, BusinessListView, BusinessUpdateView
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('',BusinessListView.as_view(),name='home'),
    path('business/<int:pk>/',BusinessDetailView.as_view(), name='business-detail'),
    path('business/new/', BusinessCreateView.as_view(), name='business-create'),
    path('business/<int:pk>/update/',BusinessUpdateView.as_view(), name='business-update'),
    path('business/<int:pk>/delete/',BusinessDeleteView.as_view(),name='business-delete')
]
