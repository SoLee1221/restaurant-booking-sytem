from django.shortcuts import render
from django.views import generic, View
from .models import Booking

# Create your views here.
class PostList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6