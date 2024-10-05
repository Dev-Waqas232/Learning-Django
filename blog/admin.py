from django.contrib import admin

# Register your models here.
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "content"]
    search_fields = ["id"]


admin.site.register(Blog, BlogAdmin)
