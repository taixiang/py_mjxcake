from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from .models import Category, Cake


class SubCateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class CakeListSerializer(serializers.ModelSerializer):
    category_id = SubCateSerializer(many=True)
    pub_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Cake
        fields = ('id', 'name', 'code', 'price', 'size', 'label', 'img1', 'pub_time', 'category_id')


class ResultPagination(PageNumberPagination):
    page_size = 2


class DetailSerializer(serializers.ModelSerializer):
    pub_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Cake
        fields = (
            'id', 'name', 'code', 'price', 'size', 'label', 'img1', 'img2', 'img3', 'desc', 'pub_time', 'category_id')
