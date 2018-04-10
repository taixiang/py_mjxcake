from django.db import models


# Create your models here.
# 词
class Poems(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    author_id = models.IntegerField()
    dynasty = models.CharField(max_length=10, blank=True, null=True)
    author = models.CharField(max_length=150)

    class Meta:
        ordering = ["id"]
        managed = False
        db_table = 'poems'


class PoemsAuthor(models.Model):
    name = models.CharField(max_length=150)
    intro_l = models.TextField(blank=True, null=True)
    intro_s = models.TextField()
    dynasty = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        ordering = ["id"]
        managed = False
        db_table = 'poems_author'


# 诗
class Poetry(models.Model):
    title = models.CharField(max_length=150)
    yunlv_rule = models.TextField()
    author_id = models.IntegerField()
    content = models.TextField()
    dynasty = models.CharField(max_length=10)
    author = models.CharField(max_length=150)

    class Meta:
        ordering = ["id"]
        managed = False
        db_table = 'poetry'


class PoetryAuthor(models.Model):
    name = models.CharField(max_length=150)
    intro = models.TextField(blank=True, null=True)
    dynasty = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        ordering = ["id"]
        managed = False
        db_table = 'poetry_author'


# 用户表
class UserInfo(models.Model):
    nickName = models.CharField("昵称", max_length=150)
    avatarUrl = models.TextField("头像", blank=True, default="")
    gender = models.IntegerField("性别", blank=True, default=0)
    language = models.CharField("语言", max_length=150, blank=True, default="")
    city = models.CharField("市", max_length=150, blank=True, default="")
    province = models.CharField("省", max_length=150, blank=True, default="")
    country = models.CharField("国家", max_length=150, blank=True, default="")
    openId = models.CharField("openId", max_length=150, blank=True, default="")

    class Meta:
        verbose_name = "用户列表"
        verbose_name_plural = "用户列表"


# 纠错信息
class ErrorInfo(models.Model):
    openId = models.CharField("openId", max_length=150, blank=True, default="")
    pId = models.IntegerField("诗词id")
    content = models.TextField("内容", default="", blank=True)
    type = models.IntegerField("诗词类别")  # 0--诗 1--词

    class Meta:
        verbose_name = "纠错信息"
        verbose_name_plural = "纠错信息"


# 搜索内容
class SearchInfo(models.Model):
    content = models.CharField("搜索内容", max_length=150, blank=True, default="")
    openId = models.CharField("openId", max_length=150, blank=True, default="")
    type = models.IntegerField("诗词类别")  # 0--诗 1--词

    class Meta:
        verbose_name = "搜索内容"
        verbose_name_plural = "搜索内容"


# 推荐内容
class Recommend(models.Model):
    week = models.IntegerField("星期几")
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    content = models.TextField()

    class Meta:
        ordering = ["-id"]
        verbose_name = "推荐内容"
        verbose_name_plural = "推荐内容"
