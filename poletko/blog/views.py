from django.shortcuts import render
from datetime import date

from .models import Post

all_posts = [

]

def get_date(post):
    return post['date']


def starting_page(request):
    latests_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html', {
        'posts': latests_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html', {
        'posts': all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': identified_post
    })
