from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime

# Create your models here.
class Table(models.Model):
    seats = models.IntegerField(default=1)

    def __str__(self):
        return 'Table for {} [{}]'.format(self.seats, self.id)


class Booking(models.Model):
    number_of_customers = models.IntegerField(default=1)
    booking_dates = models.DateTimeField(default=datetime.now, blank=False)
    body = models.TextField(default='')
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking")
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="table", null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.user_name, self.body)


class Table_availability(models.Model):
    t_availability = models.BooleanField(default=True)


