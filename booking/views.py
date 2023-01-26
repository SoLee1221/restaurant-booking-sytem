from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib import messages
from .models import *
from .forms import BookingForm
from datetime import timedelta
# Create your views here.
class PostList(View):

    def get(self, request, *args, **kwargs):
        queryset = Booking.objects.filter(user_name=self.request.user.id).order_by("-created_on")
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
                "booking": booking,
            },
        )

    def post(self, request, *args, **kwargs):

        queryset = Booking.objects.filter(user_name=self.request.user.id).order_by("-created_on")

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )

def add_booking(request):
    if request.method == "POST":
        number_of_customers = request.POST.get('number_of_customers')
        booking_dates = datetime.fromisoformat(request.POST.get('booking_dates'))
        body = request.POST.get('body')

        available_tables = Table.objects.filter(seats__gte=number_of_customers)
        if available_tables.count() == 0:
            messages.error(request, 'No available table.')
            return redirect('add_booking')
            
        other_bookings = Booking.objects.filter(booking_dates__gt=booking_dates-timedelta(minutes=59))
        other_bookings = other_bookings.filter(booking_dates__lt=booking_dates+timedelta(minutes=59))
        booked_tables = other_bookings.values_list('table', flat=True)
        available_tables = available_tables.exclude(id__in=booked_tables)
        table = available_tables.order_by('seats').first() or None

        if table:
            Booking.objects.create(number_of_customers=number_of_customers, booking_dates=booking_dates, body=body, user_name=request.user, table=table)
            return redirect('home')
        else:
            messages.error(request, 'No available table at this time.')
            return redirect('add_booking')

    return render(request, 'add_booking.html', {'booking_forms': BookingForm()})


def edit_booking(request, booking_id):
    queryset = Booking.objects.all()
    booking = get_object_or_404(queryset, pk=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_detail', pk=booking_id)

    return render(request, 'edit_booking.html', {'booking': booking, 'booking_forms': BookingForm(instance=booking)})

def delete_booking(request, booking_id):
    queryset = Booking.objects.all()
    booking = get_object_or_404(queryset, pk=booking_id)
    booking.delete()
    return redirect('home')
