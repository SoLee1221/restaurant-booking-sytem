from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<int:pk>/', views.BookingDetail.as_view(), name='booking_detail'),
    path('add_booking', views.add_booking, name='add_booking'),
    path('edit_booking/<booking_id>', views.edit_booking, name='edit_booking'),
    path('delete_booking/<booking_id>', views.delete_booking, name='delete_booking'),
]