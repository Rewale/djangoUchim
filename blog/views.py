from django.shortcuts import render
from .models import Post


# Create your views here.
def post_list(requset):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(requset, 'blog/post_list.html', {'posts': posts})
