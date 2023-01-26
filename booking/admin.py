from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')

@admin.register(Table)
class TablesAdmin(SummernoteModelAdmin):
    summernote_fields = ('seats')

