from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from .models import Poems, Poetry, PoemsAuthor, PoetryAuthor


class ResultPagination(PageNumberPagination):
    page_size = 15


# 词
class PoemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poems
        fields = ('id', 'title', 'content', 'author', 'author_id')


class PoemAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoemsAuthor
        fields = ('id', 'name', 'intro_l')

class PoemDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poems
        fields = (
            'id', 'title', 'content', 'author', 'author_id')


# 诗
class PoetryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poetry
        fields = ('id', 'title', 'content', 'author', 'author_id')


class PoetryAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoetryAuthor
        fields = ('id', 'name', 'intro')


class PoetryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poetry
        fields = (
            'id', 'title', 'content', 'author', 'author_id')


