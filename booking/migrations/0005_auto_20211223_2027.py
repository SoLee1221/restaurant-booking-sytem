# Generated by Django 3.2.9 on 2021-12-23 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_rename_name_booking_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='customer',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
    ]