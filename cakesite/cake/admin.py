from django.contrib import admin
from .models import Category, Cake, Message
from form_utils.widgets import ImageWidget
from django.db import models
from django.utils.safestring import mark_safe

# Register your models here.
admin.site.register(Category)

admin.site.site_header = "后台管理"


class cakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'size', 'price', 'image')
    formfield_overrides = {models.ImageField: {'widget': ImageWidget}}
    list_filter = ('category_id', 'size')
    search_fields = ('name', 'code')
    list_per_page = 10


admin.site.register(Cake, cakeAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('logoImg', 'slogen', 'address', 'qrcodeImg')
    formfield_overrides = {models.ImageField: {'widget': ImageWidget}}


admin.site.register(Message, MessageAdmin)
