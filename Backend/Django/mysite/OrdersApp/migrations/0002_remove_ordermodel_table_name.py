# Generated by Django 3.1.7 on 2021-05-25 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrdersApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='table_name',
        ),
    ]