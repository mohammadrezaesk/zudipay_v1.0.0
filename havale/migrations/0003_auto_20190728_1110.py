# Generated by Django 2.2.3 on 2019-07-28 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('havale', '0002_traveler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traveler',
            name='ischild',
            field=models.BooleanField(default=False),
        ),
    ]