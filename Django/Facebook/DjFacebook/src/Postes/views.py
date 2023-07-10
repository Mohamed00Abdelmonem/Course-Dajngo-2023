from django.shortcuts import render
from .models import Post
# Create your views here.

def  post_list(request):
    data = Post.objects.all()
    return render(request, 'list_post.html', {'context': data})


def detail_list(request, id_post):
    data = Post.objects.get(id=id_post)
    return render(request, 'detail_list.html', {'context':data})