# Generated by Django 2.2.7 on 2019-12-10 21:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20191210_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dateIn',
            field=models.DateField(default=datetime.datetime(2019, 12, 10, 16, 51, 3, 865807)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dateOut',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 9, 16, 51, 3, 865807)),
        ),
        migrations.AlterField(
            model_name='review',
            name='laptop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Laptop'),
        ),
        migrations.AlterField(
            model_name='review',
            name='timestamp',
            field=models.DateField(default=datetime.datetime(2019, 12, 10, 16, 51, 3, 865807)),
        ),
    ]