# Generated by Django 3.1.6 on 2022-08-11 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0019_auto_20220629_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livre',
            name='date_update',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 11, 11, 55, 30, 740615)),
        ),
    ]
