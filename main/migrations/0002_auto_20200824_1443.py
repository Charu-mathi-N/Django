# Generated by Django 3.1 on 2020-08-24 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_Datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 24, 14, 43, 17, 321539), verbose_name='date published'),
        ),
    ]
