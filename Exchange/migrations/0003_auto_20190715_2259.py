# Generated by Django 2.2.3 on 2019-07-15 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exchange', '0002_auto_20190715_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricecard',
            name='ishow',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='pricecard',
            name='price',
            field=models.IntegerField(max_length=30),
        ),
    ]
