from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.


class HomeView(TemplateView):
    template_name = 'blog/home.html'

@method_decorator(login_required, name='dispatch')
class BlogListView(ListView):
    template_name = 'blog/blog_list.html'
    model = Blog

@method_decorator(login_required, name='dispatch')
class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
    model = Blog
