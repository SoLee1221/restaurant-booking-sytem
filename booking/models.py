from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Booking(models.Model):
    tables = models.IntegerField(default=1)
    booking_dates = models.DateTimeField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking")
    number_of_customers = models.IntegerField(default=1)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField(default='')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"comment {self.body} by {self.name}"


class Table_availability(models.Model):
    t_availability = models.BooleanField(default=True)

