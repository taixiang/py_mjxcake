from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField("类别", max_length=40)
    pub_time = models.DateTimeField("时间", default=timezone.now)
    order = models.IntegerField("权重值", default=0, help_text="值越大越靠前")

    class Meta:
        ordering = ["-order", "pub_time"]
        verbose_name = "分类"
        verbose_name_plural = "分类"

    def __str__(self):
        return self.name


class Cake(models.Model):
    name = models.CharField("名称", max_length=40, default="", blank=True)
    code = models.CharField("编号", max_length=40, help_text="必填")
    size = models.CharField("尺寸", max_length=10, help_text="必填，直接填写对应数字即可，例：填13即为13寸")
    price = models.IntegerField("价格", default=0)
    img1 = models.ImageField("图片1", upload_to="photos/%Y/%m/%d", help_text="必填")
    img2 = models.ImageField("图片2", upload_to="photos/%Y/%m/%d", default="photos/blank.jpg", blank=True, null=True)
    img3 = models.ImageField("图片3", upload_to="photos/%Y/%m/%d", default="photos/blank.jpg", blank=True, null=True)
    label = models.CharField("标签", max_length=100, default="", blank=True)
    order = models.IntegerField("权重值", default=0, help_text="值越大越靠前")
    desc = models.TextField("描述", default="", help_text="每个蛋糕都拥有一段故事", blank=True)
    pub_time = models.DateTimeField("时间", default=timezone.now)
    category_id = models.ManyToManyField("Category", related_name="cake_post", verbose_name="分类")

    class Meta:
        ordering = ["-order", "pub_time"]
        verbose_name = "蛋糕列表"
        verbose_name_plural = "蛋糕列表"

    def image(self):
        return '<img src="/static/img/%s" width="50px" height="50px" />' % self.img1

    image.allow_tags = True
    image.short_description = "图片"

    def __str__(self):
        return self.name


class Message(models.Model):
    logo = models.ImageField("logo图", default="photos/logo.png", upload_to="photos/%Y/%m/%d")
    slogen = models.CharField("标语", max_length=40, default="", blank=True)
    address = models.CharField("地址", max_length=50, default="", blank=True)
    qrcode = models.ImageField("微信二维码", default="photos/qrcode.png", upload_to="photos/%Y/%m/%d")

    class Meta:
        verbose_name = "基本信息"
        verbose_name_plural = "基本信息"

    def logoImg(self):
        return '<img src="/static/img/%s" width="50px" height="50px" />' % self.logo

    logoImg.allow_tags = True
    logoImg.short_description = "logo图"

    def qrcodeImg(self):
        return '<img src="/static/img/%s" width="50px" height="50px" />' % self.qrcode

    qrcodeImg.allow_tags = True
    qrcodeImg.short_description = "微信二维码"

    def __str__(self):
        return self.slogen
