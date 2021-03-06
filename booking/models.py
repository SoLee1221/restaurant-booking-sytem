from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Booking(models.Model):
    tables = models.IntegerField(default=1)
    booking_dates = models.DateTimeField()
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking")
    number_of_customers = models.IntegerField(default=1)
    body = models.TextField(default='')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.user_name, self.body)


class Table_availability(models.Model):
    t_availability = models.BooleanField(default=True)
