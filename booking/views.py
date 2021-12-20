from django.shortcuts import render
from django.views import generic, View
from .models import Booking

# Create your views here.
class PostList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3

class BookingDetail(View):
    
    def get(self, request, *args, **kwargs):
        queryset = Booking.objects.all()
        booking = get_object_or_404(queryset)

        return render(
            request,
            "booking_detail.html",
            {
                "booking": booking
            },
        )