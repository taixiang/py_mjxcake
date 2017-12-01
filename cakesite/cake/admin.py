from django.contrib import admin
from .models import Category, Cake
from form_utils.widgets import ImageWidget
from django.db import models

# Register your models here.
admin.site.register(Category)
admin.site.site_header = "后台管理"


class cakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'size', 'price', 'img1')
    formfield_overrides = {models.ImageField: {'widget': ImageWidget}}


admin.site.register(Cake)
