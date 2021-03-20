from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.forms import TextInput


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'username',]


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['email', 'username', ]