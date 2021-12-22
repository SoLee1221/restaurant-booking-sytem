from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<int:pk>/', views.BookingDetail.as_view(), name='booking_detail'),
]