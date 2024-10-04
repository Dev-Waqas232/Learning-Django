from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Blog


def home_view(request):

    blog_obj = Blog.objects.get(id=1)

    return render(request, "home.html", {
        "title": blog_obj.title,
        "content": blog_obj.content
    })
