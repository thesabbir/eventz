from django.db import models

# Create your models here.

class Merchandise(models.Model):
    name = models.CharField()
    photo = models.ImageField()
    discount = models.IntegerField()
    price = models.IntegerField()
    tags = models.CharField()
    description = models.TextField()
    user = models.OneToOneRel()
    events = models.OneToOneRel()
    orders = models.ManyToOneRel()



