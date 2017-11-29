from django.contrib import admin
from .models import Category, Cake

# Register your models here.
admin.site.register(Category)
admin.site.register(Cake)
admin.site.site_header = "后台管理"
