from django.db import models
from django.contrib.auth.models import user

# Create your models here.
class Booking(models.Model):
    tables = models.IntegerField(default=1)
    booking_dates = models.DateTimeField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking")
    comment = models.TextField()
    number_of_customers = models.IntegerField(default=1)


