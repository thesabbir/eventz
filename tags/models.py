from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now())
