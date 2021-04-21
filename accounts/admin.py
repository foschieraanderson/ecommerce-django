from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.utils.translation import ugettext_lazy as _

from .forms import UserChangeForm, UserCreationForm
from .models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    add_form = UserCreationForm
    add_fieldsets = (
        (None, {"fields": ("username", "email", "password1", "password2")}),
    )
    form = UserChangeForm
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (
            _("Information"),
            {
                "fields": (
                    "cpf",
                    "cnpj",
                    "postal_code",
                    "address",
                    "district",
                    "state",
                    "city",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    list_display = ["username", "email", "is_staff", "date_joined"]
