from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    output_of_posts_index = 10
    posts = Post.objects.select_related('group')[:output_of_posts_index]
    context = {
        'posts': posts,
        'title': 'Последние обновления на сайте'
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    output_of_posts_group = 10
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:output_of_posts_group]
    context = {
        'group': group,
        'posts': posts,
        'title': 'Лев Толстой – зеркало русской революции.'
    }
    return render(request, 'posts/group_list.html', context)
