from django.urls import path
from .views import FollowPostsView, PostDetailView, PostDeleteView


urlpatterns = [
    path('', FollowPostsView.as_view(), name='posts'),
    path('<uuid:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<uuid:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]