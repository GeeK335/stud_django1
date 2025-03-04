# Generated by Django 5.1.4 on 2024-12-28 14:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('mileage', models.IntegerField()),
                ('volume', models.IntegerField()),
                ('body_type', models.CharField(choices=[('sedan', 'Седан'), ('hatchback', 'Хэтчбек'), ('SUV', 'Внедорожник'), ('wagon', 'Универсал'), ('minivan', 'Минивэн'), ('pickup', 'Пикап'), ('coupe', 'Купе'), ('cabrio', 'Кабриолет')], max_length=50)),
                ('drive_unit', models.CharField(choices=[('rear', 'Задний'), ('front', 'Передний'), ('full', 'Полный')], max_length=50)),
                ('gearbox', models.CharField(choices=[('manual', 'Механика'), ('automatic', 'Автомат'), ('вариатор', 'CVT'), ('robot', 'Робот')], max_length=50)),
                ('fuel_type', models.CharField(choices=[('gasoline', 'Бензин'), ('diesel', 'Дизель'), ('hybrid', 'Гибрид'), ('electro', 'Электро')], max_length=50)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.car')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client')),
            ],
        ),
    ]
