from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from .models import Category,Cake

class SubCateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category',)

class CakeListSerializer(serializers.ModelSerializer):
    category_id = SubCateSerializer(many=True)
    pub_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Cake
        fields = ('id', 'name', 'price', 'discount_price', 'desc', 'label', 'pub_time', 'category_id')