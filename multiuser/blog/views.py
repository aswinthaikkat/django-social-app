from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Blog
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin


# Create your views here.


class HomeView(TemplateView):
    template_name = 'blog/home.html'


class BlogListView(LoginRequiredMixin, ListView):
    template_name = 'blog/blog_list.html'
    model = Blog

    def get_queryset(self):
        queryset = super(BlogListView, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset


class BlogDetailView(LoginRequiredMixin,  DetailView):
    # def test_func(self):
    #     return self.request.user.email.endswith('@example.com')
    def get_queryset(self):
        queryset = super(BlogDetailView, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset
    template_name = 'blog/blog_detail.html'
    model = Blog


class BlogCreateView(LoginRequiredMixin, CreateView):
    success_message = 'Added Successfully'
    model = Blog
    fields = ['title', 'description']

    def form_valid(self, form):
        # here you bind the foreign key teacher to the current user
        form.instance.author = self.request.user
        return super(BlogCreateView, self).form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    success_message = 'Added Successfully'
    model = Blog
    fields = ['title', 'description']
    template_name_suffix = '_update_form'


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    success_message = 'deletedb Successfully'
    model = Blog
    success_url = reverse_lazy('blog:blog')
