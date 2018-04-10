from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from .models import Poems, Poetry, PoemsAuthor, PoetryAuthor, Recommend, ErrorInfo
from django.core import serializers as jsonSer
from django.http import JsonResponse
from django.forms.models import model_to_dict


class ResultPagination(PageNumberPagination):
    page_size = 15


class SubCateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poems
        fields = ('title', 'content')


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


# 推荐内容
class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommend
        fields = ('id', 'title', 'content', 'author', 'week')


class MyErrorSerializer(serializers.ModelSerializer):
    pId = serializers.SerializerMethodField('getPId')

    class Meta:
        model = ErrorInfo
        fields = ('id', 'openId', 'pId', 'content', 'type')

    def getPId(self, obj):
        if obj.type == 0:
            queryset = Poetry.objects.get(id=obj.pId)

        else:
            queryset = Poems.objects.get(id=obj.pId)
        content = model_to_dict(queryset)

        return content
