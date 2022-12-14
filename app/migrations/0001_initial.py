# Generated by Django 4.1 on 2022-09-09 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('short_name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('height', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('height_diff', models.IntegerField(default=0)),
                ('weight_diff', models.IntegerField(default=0)),
                ('attributes', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('video', models.CharField(max_length=200)),
                ('foot', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=200)),
                ('male_height', models.IntegerField(default=0)),
                ('male_weight', models.IntegerField(default=0)),
                ('female_height', models.IntegerField(default=0)),
                ('female_weight', models.IntegerField(default=0)),
            ],
        ),
    ]
