# Generated by Django 3.2.9 on 2023-01-24 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_auto_20230124_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='seats2',
        ),
    ]