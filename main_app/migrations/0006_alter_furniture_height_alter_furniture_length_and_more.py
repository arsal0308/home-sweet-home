# Generated by Django 4.2.4 on 2023-08-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_furniture_description_home_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='height',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='length',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='width',
            field=models.CharField(max_length=100),
        ),
    ]
