# Generated by Django 2.2.3 on 2019-07-28 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('havale', '0004_tour_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traveler',
            name='birthmonth',
            field=models.CharField(default=True, max_length=20),
        ),
    ]
