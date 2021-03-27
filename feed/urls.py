from django.urls import path
from .views import FollowPostsView, PostDetailView, PostDeleteView, SearchView


urlpatterns = [
    path('', FollowPostsView.as_view(), name='posts'),
    path('search/', SearchView.as_view(), name='search'),
    path('<uuid:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<uuid:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]