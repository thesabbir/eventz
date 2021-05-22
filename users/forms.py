from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserModel


class UserForm(UserCreationForm):

    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name')


class UserChange(UserChangeForm):

    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name')
