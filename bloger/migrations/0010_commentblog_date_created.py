# Generated by Django 3.2.9 on 2021-12-12 15:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloger', '0009_auto_20211212_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentblog',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]