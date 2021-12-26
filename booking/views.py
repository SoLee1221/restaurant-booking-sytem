from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Booking
from .forms import BookingForm

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
        tables = request.POST.get('tables')
        booking_dates = request.POST.get('booking_dates')
        number_of_customers = request.POST.get('number_of_customers')
        body = request.POST.get('body')
        Booking.objects.create(tables=tables, booking_dates=booking_dates, user_name=request.user, number_of_customers=number_of_customers, body=body)

        return redirect('home')

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
