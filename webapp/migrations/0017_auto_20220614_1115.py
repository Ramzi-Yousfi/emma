# Generated by Django 3.1.6 on 2022-06-14 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_contact_sujet_alter_livre_date_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='galeries',
            name='background_photo',
            field=models.ImageField(blank=True, null=True, upload_to='galeries_images/'),
        ),
        migrations.AlterField(
            model_name='galeries',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='galeriesimage',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='galeriesimage',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='galeries_images/'),
        ),
        migrations.AlterField(
            model_name='livre',
            name='date_update',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 11, 15, 32, 480059)),
        ),
        migrations.AlterField(
            model_name='livre',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='presentationcard',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='publicationimage',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='publicationimage',
            name='photo_url',
            field=models.ImageField(upload_to='publication_images/'),
        ),
    ]