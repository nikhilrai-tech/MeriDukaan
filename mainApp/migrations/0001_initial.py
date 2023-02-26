# Generated by Django 4.0.1 on 2022-02-02 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('basePrice', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('finalPrice', models.IntegerField()),
                ('color', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('stock', models.BooleanField(default=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('pic1', models.ImageField(upload_to='images/')),
                ('pic2', models.ImageField(upload_to='images/')),
                ('pic3', models.ImageField(upload_to='images/')),
                ('pic4', models.ImageField(upload_to='images/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.brand')),
                ('maincat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.maincategory')),
                ('subcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.subcategory')),
            ],
        ),
    ]
