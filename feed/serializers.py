from rest_framework import serializers
from .models import Post, Comment


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