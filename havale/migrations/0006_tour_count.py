# Generated by Django 2.2.3 on 2019-07-30 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('havale', '0005_auto_20190728_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='count',
            field=models.IntegerField(default=True),
        ),
    ]
