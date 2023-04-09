from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Blog, Category


class CategorySerialezer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UserSerialezer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_active']


class BlogSerialezer(serializers.ModelSerializer):
    category = CategorySerialezer(many=False)
    user = UserSerialezer(many=False)
    class Meta:
        model = Blog
        fields = '__all__'

