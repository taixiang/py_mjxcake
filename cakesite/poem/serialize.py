from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from .models import Poems, Poetry, PoemsAuthor, PoetryAuthor, Recommend, ErrorInfo


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
        print(obj.type)
        data = []
        content = None
        if obj.type == 0:
            Poems.objects.get(id=obj.pId)
        data.append({})
        return "111"
