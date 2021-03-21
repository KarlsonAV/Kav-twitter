from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsAuthorOrReadOnly
from rest_framework import status
from rest_framework import permissions
from .models import User, Profile, Follow
from feed.models import Post
from .serializers import ProfileSerializer, FollowSerializer, UpdateProfileSerializer
from feed.serializers import GenericPostsSerializer


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, username, format=None):
        user = User.objects.get(username=username)
        profile = ProfileSerializer(Profile.objects.get(user=user)).data
        profile['date_joined'] = user.date_joined
        posts = [GenericPostsSerializer(instance=post).data for post in Post.objects.filter(author=user)]
        context = {
            'profile': profile,
            'posts': posts,
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, username, format=None):
        user = request.user
        if user.username != username:
            follow_user = User.objects.get(username=username)
            try:
                follow = Follow.objects.get(user=user, follow_user=follow_user)
                if request.POST.get('followed'):
                    follow.delete()
                    return Response(status=status.HTTP_205_RESET_CONTENT)
            except:
                if request.POST.get('followed'):
                    Follow.objects.create(user=user, follow_user=follow_user)
                    return Response(status=status.HTTP_201_CREATED)
        return HttpResponseRedirect(request.path)


class UpdateProfileView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def put(self, request, username, format=None):
        user = User.objects.get(username=username)
        if request.user == user:
            profile = Profile.objects.get(user=user)
            data = request.data
            profile.image = data['image']
            if not profile.image:
                profile.image = 'users_profiles/default-user-img-768x768.jpg'
            profile.status = data['status']
            profile.user = user
            profile.save()
            serializer = UpdateProfileSerializer(profile).data
            return Response(serializer, status=status.HTTP_205_RESET_CONTENT)
        return HttpResponseRedirect(reverse('profile', kwargs={'username': username}))


class FollowView(APIView):

    def get(self, request, username, format=None):
        user = User.objects.get(username=username)
        follow = [FollowSerializer(instance=follow).data for follow in Follow.objects.filter(follow_user=user)]
        context = {
            'follow': follow,
        }
        return Response(context, status=status.HTTP_200_OK)


class FollowingView(APIView):

    def get(self, request, username, format=None):
        user = User.objects.get(username=username)
        follow = [FollowSerializer(instance=follow).data for follow in Follow.objects.filter(user=user)]
        context = {
            'follow': follow,
        }
        return Response(context, status=status.HTTP_200_OK)