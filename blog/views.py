from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def home_page(request):
    context = {"all_posts": Post.objects.all()}
    return render(request, "blog/home.html", context)


def single_post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, "blog/single_post.html", {"post": post})
