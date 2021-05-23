from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserModel

USER_FIELDS = ('email', 'first_name', 'last_name', 'country', 'gender', 'date_of_birth', 'mobile', 'address')


class UserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = USER_FIELDS


class UserChange(UserChangeForm):
    class Meta:
        model = UserModel
        fields = USER_FIELDS
