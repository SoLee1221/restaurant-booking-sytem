# Generated by Django 3.2.9 on 2021-12-23 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20211209_1826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='name',
            new_name='user',
        ),
    ]