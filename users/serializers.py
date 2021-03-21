from rest_framework import serializers

from .models import Profile, Follow


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            'user',
            'image',
            'status',
            'followers',
            'following',
        ]


class UpdateProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            'image',
            'status',
        ]


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = [
            'user',
        ]