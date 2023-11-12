from django.contrib.auth.admin import UserAdmin, UserCreationForm
from django.contrib import admin
from users.models import CustomUser
from django.core.exceptions import ValidationError
from django import forms


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'cafe', "is_superuser")

    def clean(self):
        """
        При создании пользователя, если он не суперпользователь
        то обязательно требуется привязка к кафе
        """
        super(UserRegistrationForm, self).clean()
        user_superuser = self.cleaned_data['is_superuser']
        if not user_superuser and not self.cleaned_data['cafe']:
            raise ValidationError(
                "Персонал должен быть привязан к кафе"
            )


class CustomUserForm(forms.ModelForm):
    def clean(self):
        """
        При редактировании пользователя, если он не суперпользователь
        то обязательно требуется привязка к кафе
        """
        super(CustomUserForm, self).clean()
        user_superuser = self.cleaned_data['is_superuser']
        if not user_superuser and not self.cleaned_data['cafe']:
            raise ValidationError(
                "Персонал должен быть привязан к кафе"
            )


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "cafe", "last_login", "date_joined")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "cafe",
                    "is_active",
                    "is_superuser",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "cafe",
                    "password1",
                    "password2",
                    "is_superuser"
                ),
            },
        ),
    )
    form = CustomUserForm
    add_form = UserRegistrationForm