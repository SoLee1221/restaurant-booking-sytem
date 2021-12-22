from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Booking

# Create your views here.
class PostList(View):

    def get(self, request, *args, **kwargs):
        queryset = Booking.objects.filter(name=self.request.user.id).order_by("-created_on")
        return render(
            request,
            "index.html",
            {
                "booking_list": queryset
            },
        )

class BookingDetail(View):
    
    def get(self, request, *args, **kwargs):
        queryset = Booking.objects.all()
        booking = get_object_or_404(queryset, pk=self.kwargs.get("pk"))

        return render(
            request,
            "booking_detail.html",
            {
                "booking": booking
            },
        )

    #def post(self, request, slug, *args, **kwargs):