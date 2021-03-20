from django.urls import path
from .views import ProfileView, FollowView, FollowingView, ChangeProfileView


urlpatterns = [
    path('<str:username>/', ProfileView.as_view(), name='profile'),
    path('<str:username>/change/', ChangeProfileView.as_view(), name='profile_change'),
    path('<str:username>/follow/', FollowView.as_view(), name='user_follow'),
    path('<str:username>/following/', FollowingView.as_view(), name='user_following'),
]