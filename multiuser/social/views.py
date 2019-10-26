from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Blog

# Create your views here.


class AllPostListView(ListView):
    template_name = 'social/blog_list.html'
    model = Blog

    """ def get_queryset(self):
        queryset = super(BlogListView, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

 """
