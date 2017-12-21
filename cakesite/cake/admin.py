from django.contrib import admin
from .models import Category, Cake, Message
from django.db import models
from django.utils.safestring import mark_safe
from django import forms


# Register your models here.
admin.site.register(Category)

admin.site.site_header = "后台管理"

class ImageWidget2(forms.FileInput):
    template = '%(input)s<br />%(image)s'

    def __init__(self, attrs=None, template=None, width=200, height=200):
        if template is not None:
            self.template = template
        self.width = width
        self.height = height
        super(ImageWidget2, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        input_html = super(ImageWidget2, self).render(name, value, attrs)
        if hasattr(value, 'width') and hasattr(value, 'height'):

            image_html = '<img src="/upload/img/%s" width="50px" height="50px" />' % value.name

            output = self.template % {'input': input_html,
                                      'image': image_html}
        else:
            output = input_html
        return mark_safe(output)


class cakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'size', 'price', 'image')
    formfield_overrides = {models.ImageField: {'widget': ImageWidget2}}
    list_filter = ('category_id', 'size')
    search_fields = ('name', 'code')
    list_per_page = 10


admin.site.register(Cake, cakeAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('logoImg', 'slogen', 'address', 'qrcodeImg')
    formfield_overrides = {models.ImageField: {'widget': ImageWidget2}}


admin.site.register(Message, MessageAdmin)




