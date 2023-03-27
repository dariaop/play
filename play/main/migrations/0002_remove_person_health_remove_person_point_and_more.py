# Generated by Django 4.1.7 on 2023-03-26 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='health',
        ),
        migrations.RemoveField(
            model_name='person',
            name='point',
        ),
        migrations.RemoveField(
            model_name='person',
            name='power',
        ),
        migrations.RemoveField(
            model_name='person',
            name='skill',
        ),
        migrations.AlterField(
            model_name='person',
            name='height',
            field=models.IntegerField(verbose_name='Рост'),
        ),
        migrations.AlterField(
            model_name='person',
            name='login',
            field=models.EmailField(max_length=254, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(max_length=20, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(max_length=10, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='person',
            name='user_name',
            field=models.CharField(max_length=100, verbose_name='Имя игрока'),
        ),
        migrations.AlterField(
            model_name='person',
            name='weight',
            field=models.IntegerField(verbose_name='Вес'),
        ),
    ]
