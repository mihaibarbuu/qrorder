# Generated by Django 3.1.7 on 2021-05-17 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantApp', '0013_restaurant_restaurant_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='food_price',
            field=models.FloatField(),
        ),
    ]
