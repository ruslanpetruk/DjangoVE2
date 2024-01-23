# app_blog/urls.py
from django.urls import path, re_path
from app_blog import views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (HomePageView, ArticleDetail, ArticleList, ArticleCategoryList)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('articles-list', ArticleList.as_view(), name='articles-list'),
    path('articles', ArticleList.as_view(), name='articleslist'),
    path('articles/category/<slug>', ArticleCategoryList.as_view(), name='articles-category-list'),
    path('articles/<year>/<month>/<day>/<slug>', ArticleDetail.as_view(), name='news-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    