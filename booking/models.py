from django.db import models

# Create your models here.
class Booking(models.Model):
    tables = models.IntegerField(default=1)
    booking_dates = models.DateTimeField()
    customer = models.Foreignkey(User, on_delete=models.CASCADE, related_name="booking")
    comment = models.TextField()
    number_of_customers = models.IntegerField(default=1)


