from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

STATUS_CHOICES = (
    (1, _("Approved")),
    (2, _("Pending")),
    (3, _("Shipping")),
    (4, _("Processing")),
    (5, _("Cancelled"))
)


class Order(models.Model):
    # id = models.BigAutoField()
    events = models.ManyToManyField('events.Event')
    merchandise = models.ManyToManyField('merchandise.Merchandise')
    total_price = models.IntegerField()
    service_fee = models.IntegerField()
    transaction_fee = models.IntegerField()
    user = models.ForeignKey('users.UserModel', on_delete=models.RESTRICT)
    status = models.IntegerField(choices=STATUS_CHOICES)
    last_update = models.DateTimeField(default=timezone.now())
    payment_method = models.CharField(max_length=50)



