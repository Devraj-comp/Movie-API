# Generated by Django 3.2.11 on 2022-01-29 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('created', models.DateField()),
                ('rated', models.CharField(choices=[('5', '5 Star'), ('4', '4 Star'), ('3', '3 Star'), ('2', '2 Star'), ('1', '1 Star')], max_length=1)),
                ('duration', models.CharField(max_length=10)),
                ('actors', models.CharField(max_length=400)),
                ('country', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('movie', 'movie'), ('series', 'series'), ('episode', 'episode')], max_length=15)),
                ('poster', models.ImageField(upload_to='')),
                ('director', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=30)),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.genre')),
            ],
        ),
    ]
