from django.urls import path
from .views import FirstView


urlpatterns = [
    path('', FirstView.as_view(), name='feed'),
]