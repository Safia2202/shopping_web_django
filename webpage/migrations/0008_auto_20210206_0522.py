# Generated by Django 3.1.5 on 2021-02-06 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0007_auto_20210206_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
