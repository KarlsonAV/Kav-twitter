from rest_framework import serializers
from .models import Post, Comment
from users.models import User


class GenericPostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'pk',
            'content',
            'author',
            'image',
            'date_posted',
            'number_of_comments',
            'number_of_likes',
        ]


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'content',
            'date_posted',
            'author',
            'image',
        ]


class CommentsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'content',
            'image',
        ]


class UserSearchSeializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username'
        ]