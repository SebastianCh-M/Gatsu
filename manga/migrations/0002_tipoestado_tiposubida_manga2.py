# Generated by Django 4.2.6 on 2023-11-08 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipoEstado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='tipoSubida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subida', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Manga2',
            fields=[
                ('idManga', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nombreManga', models.CharField(max_length=50)),
                ('ano_publicacion', models.CharField(max_length=50)),
                ('mangaka', models.CharField(max_length=50)),
                ('sinopsis', models.CharField(max_length=500)),
                ('editorial', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=50)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manga.tipoestado')),
                ('tsubida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manga.tiposubida')),
            ],
        ),
    ]
