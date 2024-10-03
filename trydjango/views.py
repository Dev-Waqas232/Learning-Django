from django.http import HttpResponse

from blog.models import Blog


def home_view(request):

    blog_obj = Blog.objects.get(id=1)

    blog_title = blog_obj.title
    blog_content = blog_obj.content

    H1_STRING = f"""
    <h1>{blog_title}</h1>
    """

    P_STRING = f"""
    <p>{blog_content}</p>
    """

    HTML_STRING = H1_STRING + P_STRING

    return HttpResponse(HTML_STRING)
