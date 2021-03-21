from django.urls import path
from .views import ProfileView, FollowView, FollowingView, UpdateProfileView


urlpatterns = [
    path('<str:username>/', ProfileView.as_view(), name='profile'),
    path('<str:username>/update/', UpdateProfileView.as_view(), name='profile_update'),
    path('<str:username>/follow/', FollowView.as_view(), name='user_follow'),
    path('<str:username>/following/', FollowingView.as_view(), name='user_following'),
]