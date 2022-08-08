from django.shortcuts import render, get_object_or_404

from .models import Group, Post


def index(request):
    posts = Post.objects.select_related('group')[:Post.OUTPUT_OF_POSTS]
    context = {
        'posts': posts,
        'title': 'Последние обновления на сайте'
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:Post.OUTPUT_OF_POSTS]
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, 'posts/group_list.html', context)
