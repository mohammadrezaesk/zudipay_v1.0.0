# Generated by Django 2.2.3 on 2019-07-19 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zudipayadmin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminpaneluser',
            name='user',
        ),
        migrations.AddField(
            model_name='adminpaneluser',
            name='password',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='adminpaneluser',
            name='username',
            field=models.CharField(default='', max_length=30, unique=True),
        ),
    ]
