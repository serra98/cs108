# Generated by Django 2.2.7 on 2019-11-07 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0002_auto_20191107_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='mini_fb',
            name='home_town',
            field=models.TextField(blank=True),
        ),
    ]