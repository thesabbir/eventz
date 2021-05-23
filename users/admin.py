from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm, USER_FIELDS
from .models import UserModel


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = UserModel
    list_display = ('email', 'get_full_name', 'is_staff', 'is_active', 'is_performer')
    list_filter = ('email', 'is_staff', 'is_active', 'is_performer')
    fieldsets = (
        (None, {'fields': USER_FIELDS + ('password',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_performer')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': USER_FIELDS + ('password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(UserModel, CustomUserAdmin)
