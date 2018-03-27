from django.db import models


# Create your models here.
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
