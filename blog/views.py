from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Post


class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['-date',]
    context_object_name = 'posts' #changes name to be called in html template

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class AllPostsView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'all_posts'


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/post-detail.html', {'post': identified_post, 'tags': identified_post.tags.all()})
