# Generated by Django 3.1.7 on 2021-04-06 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantApp', '0005_auto_20210406_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodAllergens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergen_name', models.CharField(max_length=50)),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RestaurantApp.menuitem')),
            ],
        ),
    ]
