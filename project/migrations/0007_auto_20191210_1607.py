# Generated by Django 2.2.7 on 2019-12-10 21:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20191210_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dateIn',
            field=models.DateField(default=datetime.datetime(2019, 12, 10, 16, 7, 52, 839209)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dateOut',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 9, 16, 7, 52, 839209)),
        ),
        migrations.AlterField(
            model_name='review',
            name='timestamp',
            field=models.DateField(default=datetime.datetime(2019, 12, 10, 16, 7, 52, 843204)),
        ),
    ]
