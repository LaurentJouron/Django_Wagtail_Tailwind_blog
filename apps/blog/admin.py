from django.contrib import admin
from .models import BlogPage, ArticlePage, ArticleTag

admin.site.register(BlogPage)
admin.site.register(ArticlePage)
admin.site.register(ArticleTag)
