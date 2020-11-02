from django.shortcuts import render
from .models import Business, Post
from django.views.generic  import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.

class BusinessListView(LoginRequiredMixin,ListView):
    model = Business
    template_name= 'estate/home.html'
    context_object_name = 'businesses'


class BusinessDetailView(LoginRequiredMixin,DetailView):
    model = Business

class BusinessCreateView(LoginRequiredMixin,CreateView):
    model = Business
    fields = ['business_name','email','business_image']

    def form_valid(self, form):
        form.instance.business_owner = self.request.user
        return super().form_valid(form)


class BusinessUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Business
    fields = ['business_name', 'email', 'business_image']

    def form_valid(self, form):
        form.instance.business_owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        business = self.get_object()

        if self.request.user == business.business_owner:
            return True
        return False


class BusinessDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Business
    success_url = '/'

    def test_func(self):
        business = self.get_object()
        

        if self.request.user == business.business_owner:
            return True
        return False



class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'estate/post_list.html'
    context_object_name = 'posts'

class PostCreateView(CreateView):
    model = Post
    fields =  ['post']
    success_url = 'posts'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
