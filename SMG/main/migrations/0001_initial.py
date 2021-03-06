# Generated by Django 3.2.8 on 2021-10-12 12:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('image1', models.ImageField(upload_to='blogs')),
                ('image2', models.ImageField(upload_to='blogs')),
                ('title', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('writer', models.CharField(max_length=100)),
                ('short_desc', models.CharField(max_length=80)),
                ('date', models.DateField()),
                ('p1', models.TextField(blank=True, default='')),
                ('p2', models.TextField(blank=True, default='')),
                ('p3', models.TextField(blank=True, default='')),
                ('p4', models.TextField(blank=True, default='')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='CarouselCategory',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('ordering', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='StoneType',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='category_image')),
                ('ordering', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='Stone',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='stone_image')),
                ('image2', models.ImageField(upload_to='stone_image')),
                ('desc', models.TextField(blank=True, default='')),
                ('ordering', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.stonetype')),
            ],
            options={
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='CarouselImages',
            fields=[
                ('image', models.ImageField(upload_to='gallery_image')),
                ('ordering', models.IntegerField(default=1, primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1)])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.carouselcategory')),
            ],
            options={
                'ordering': ['ordering'],
            },
        ),
    ]
