from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Comment, Likes
from users.models import User, Follow
from django.utils import timezone
from .serializers import GenericPostsSerializer, CommentsSerializer, CommentsCreateSerializer
from rest_framework import status


class FollowPostsView(APIView):

    def get(self, request, format=None):
        user = request.user
        qs = Follow.objects.filter(user=user)
        follows = [user]
        for obj in qs:
            follows.append(obj.follow_user)

        all_posts = [GenericPostsSerializer(instance=post).data for post in Post.objects.filter(author__in=follows).order_by('-date_posted')]
        context = {
            'all_posts': all_posts,
        }
        return Response(context, status=status.HTTP_200_OK)


class PostDetailView(APIView):

    def get(self, request, pk, format=None):
        qs = Post.objects.get(pk=pk)
        post = GenericPostsSerializer(qs).data
        comments = [CommentsSerializer(instance=comment).data for comment in Comment.objects.filter(post_connected=Post.objects.get(pk=pk))]
        context = {
            'post': post,
            'comments': comments,
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, pk, format=None):
        post = Post.objects.get(pk=pk)
        try:
            like = Likes.objects.get(user=request.user, liked=True, post_connected=post)
            if request.POST.get('liked'):
                like.delete()
                return Response(status=status.HTTP_205_RESET_CONTENT)
        except:
            if request.POST.get('liked'):
                Likes.objects.create(user=request.user, liked=True, post_connected=post)
                return Response(status=status.HTTP_201_CREATED)
        data = dict(request.data.items())
        serializer = CommentsCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save(author=request.user, date_posted=timezone.now(), post_connected=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)