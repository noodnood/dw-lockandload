# Generated by Django 2.2.11 on 2020-03-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createbooking', '0003_auto_20200308_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingmodel',
            name='end',
            field=models.DateTimeField(default='2000-01-01 00:00:00'),
        ),
        migrations.AlterField(
            model_name='bookingmodel',
            name='start',
            field=models.DateTimeField(default='2000-01-01 00:00:00'),
        ),
    ]
