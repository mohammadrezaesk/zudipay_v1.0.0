# Generated by Django 2.2.3 on 2019-07-16 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exchange', '0003_auto_20190715_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricecard',
            name='price',
            field=models.FloatField(max_length=30),
        ),
    ]
