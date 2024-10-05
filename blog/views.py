from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound

from .models import Blog
# Create your views here.


def blog_search_view(request):
    query_dict = request.GET
    query = query_dict["query"]

    try:
        blog_obj = Blog.objects.get(id=query)
    except:
        raise Http404

    return render(request, "search.html", {"obj": blog_obj})
