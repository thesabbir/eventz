from django.db import models

# Create your models here.
from users.models import UserModel




class EventModel(models.Model):
    name = models.CharField()
    photo = models.ImageField()
    age_gate = models.IntegerField()
    price = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    event_link = models.CharField()
    description = models.TextField()
    merchandises = models.ManyToOneRel()
    orders = models.ManyToOneRel()
    tags = models.ManyToOneRel()
    user = models.OneToOneField(to=UserModel)

    class Meta:
        verbose_name = 'Event'
        plural_name = 'Events'

