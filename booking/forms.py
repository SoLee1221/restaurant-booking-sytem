from .models import Booking
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('tables', 'booking_dates', 'number_of_customers', 'body')
