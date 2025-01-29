from django.urls import include, path
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail import urls as wagtail_urls
from . import views

urlpatterns = [
    path("cms/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", views.article_search, name="article_search"),
    path("", include(wagtail_urls)),
]
