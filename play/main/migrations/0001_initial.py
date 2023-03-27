# Generated by Django 4.1.7 on 2023-03-25 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('login', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('point', models.IntegerField()),
                ('power', models.IntegerField()),
                ('health', models.IntegerField()),
                ('skill', models.IntegerField()),
            ],
        ),
    ]