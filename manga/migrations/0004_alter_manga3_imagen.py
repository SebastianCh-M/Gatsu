# Generated by Django 4.2.6 on 2023-11-08 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0003_manga3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga3',
            name='imagen',
            field=models.ImageField(upload_to='D:\\Django Proyectos\\Gatsu\\static\\images'),
        ),
    ]
