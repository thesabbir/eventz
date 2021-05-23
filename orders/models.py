from django.db import models
from django.utils import timezone


class Orders(models.Model):
    id = models.BigAutoField()
    events = models.OneToOneRel()
    merchandise = models.OneToOneRel()
    total_price = models.IntegerField()
    service_fee = models.IntegerField()
    transaction_fee = models.IntegerField()
    user = models.OneToOneRel()
    status = models.Choices()
    last_update = models.DateTimeField(default=timezone.now())
    payment_method = models.CharField()



