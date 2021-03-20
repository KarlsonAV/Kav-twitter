from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Follow, User, Profile
from .forms import CustomUserChangeForm, CustomUserCreationForm

CustomUser = User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Follow)
admin.site.register(Profile)
