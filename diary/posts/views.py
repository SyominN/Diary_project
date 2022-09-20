from django.shortcuts import render

from .models import Post


def index(request):
    template = 'posts/index.html'
    posts = (
        Post.objects
        .select_related(
            'author',
            'group'
        )
        .order_by('-pub_date')[:10]
    )
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = (
        Post.objects
        .select_related(
            'author'
        )
        .order_by('-pub_date')[:10]
    )
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, template, context)
