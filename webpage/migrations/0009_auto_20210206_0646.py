# Generated by Django 3.1.5 on 2021-02-06 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0008_auto_20210206_0522'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItems',
            new_name='OrderItem',
        ),
    ]
