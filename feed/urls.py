from django.urls import path
from .views import FollowPostsView, PostDetailView


urlpatterns = [
    path('', FollowPostsView.as_view(), name='posts'),
    path('<uuid:pk>/', PostDetailView.as_view(), name='post_detail')
]