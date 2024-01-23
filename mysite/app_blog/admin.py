# Register your models here.
# admin.site.register(Article)

# -*- coding: utf-8 -*-
from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.utils.text import slugify

from .models import Article, ArticleImage, Category
from .forms import ArticleImageForm

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    prepopulated_fields = {'slug': ('category',)}  # автозаповнення для slug

admin.site.register(Category, CategoryAdmin)


class ArticleImageInline(admin.TabularInline):
 model = ArticleImage
 form = ArticleImageForm
 extra = 0
 fieldsets = (
  ('', {
   'fields': ('title', 'image',),
  }),
 )

class ArticleAdmin(admin.ModelAdmin):
 list_display = ('title', 'pub_date', 'category', 'slug', 'main_page')
 inlines = [ArticleImageInline]
 multiupload_form = True
 multiupload_list = False
 prepopulated_fields = {'slug': ('title',)}
 raw_id_fields = ('category',)
 fieldsets = (
  ('', {
   'fields': ('pub_date', 'title', 'description', 'main_page'),
  }),
 ((u'Додатково'), {
  'classes': ('grp-collapse grp-closed',),
  'fields': ('slug','category'),
 }),
 )

 def delete_file(self, pk, request):
  '''Delete an image.'''

  obj = get_object_or_404(ArticleImage, pk=pk)
  return obj.delete()

admin.site.register(Article, ArticleAdmin)
