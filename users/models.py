from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email address'), unique=True)
    first_name = models.CharField(_('First name'), max_length=50, blank=True)
    last_name = models.CharField(_('Last name'), max_length=50, blank=True)
    country = models.CharField(_('Country'), max_length=100, blank=True)
    address = models.TextField(_('Address'), blank=True)
    postal_code = models.CharField(_('Postal Code'), max_length=20, blank=True)
    mobile = models.CharField(_('Mobile'), max_length=20, blank=True)
    date_of_birth = models.DateField(_('Date of birth'), blank=True, null=True)
    gender = models.CharField(_('Gender'), max_length=20, blank=True)
    is_performer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return f"#{self.first_name} #{self.last_name}"

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

