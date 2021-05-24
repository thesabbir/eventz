from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField()
    age_gate = models.IntegerField()
    price = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    event_link = models.CharField(max_length=200)
    description = models.TextField()
    merchandises = models.ManyToManyField('merchandise.Merchandise', null=True, blank=True)
    orders = models.ManyToManyField('orders.Order', null=True, blank=True)
    tags = models.ManyToManyField('tags.Tag', null=True, blank=True)
    user = models.OneToOneField('users.UserModel', on_delete=models.RESTRICT)
