from django.contrib import admin
from .models import Category, Cake
from form_utils.widgets import ImageWidget
from django.db import models
from django.utils.safestring import mark_safe

# Register your models here.
admin.site.register(Category)
admin.site.site_header = "后台管理"


class cakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'size', 'price', 'image')
    formfield_overrides = {models.ImageField: {'widget': ImageWidget}}
    list_filter = ('category_id',)
    search_fields = ('name',)


admin.site.register(Cake, cakeAdmin)
