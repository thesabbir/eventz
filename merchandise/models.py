from django.db import models


class Merchandise(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField()
    discount = models.IntegerField(default=0)
    price = models.IntegerField()
    tags = models.ManyToManyField('tags.Tag', null=True, blank=True)
    description = models.TextField()
    user = models.ForeignKey('users.UserModel', on_delete=models.RESTRICT)
    events = models.ManyToManyField('events.Event', null=True,blank=True)
