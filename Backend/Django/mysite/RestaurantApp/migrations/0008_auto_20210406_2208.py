# Generated by Django 3.1.7 on 2021-04-06 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantApp', '0007_auto_20210406_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodallergen',
            name='food_item',
        ),
        migrations.AddField(
            model_name='foodallergen',
            name='food_item',
            field=models.ManyToManyField(to='RestaurantApp.MenuItem'),
        ),
    ]
