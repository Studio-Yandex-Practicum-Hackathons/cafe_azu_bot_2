# Generated by Django 4.2.7 on 2023-11-23 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название блюда')),
                ('description', models.CharField(max_length=256, verbose_name='Описание блюда')),
                ('image', models.ImageField(blank=True, null=True, upload_to='dishes/', verbose_name='Изображение блюда')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
            },
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Название сета')),
                ('description', models.CharField(max_length=256, verbose_name='Описание сета')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Цена сета')),
                ('image', models.ImageField(blank=True, null=True, upload_to='sets/', verbose_name='Изображение сета')),
            ],
            options={
                'verbose_name': 'Сет',
                'verbose_name_plural': 'Сеты',
                'ordering': ('price', 'name'),
            },
        ),
        migrations.CreateModel(
            name='SetDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество блюд в сете')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.dishes')),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.set')),
            ],
            options={
                'verbose_name': 'Блюд в сете',
                'verbose_name_plural': 'Блюд в сете',
            },
        ),
        migrations.AddField(
            model_name='set',
            name='dishes',
            field=models.ManyToManyField(blank=True, through='menu.SetDish', to='menu.dishes', verbose_name='Блюда'),
        ),
        migrations.AddConstraint(
            model_name='setdish',
            constraint=models.UniqueConstraint(fields=('set', 'dish'), name='unique_set_dish'),
        ),
    ]
