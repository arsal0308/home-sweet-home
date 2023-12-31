# Generated by Django 4.2.4 on 2023-08-14 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='tour date')),
                ('time', models.TimeField()),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.home')),
            ],
            options={
                'ordering': ['-date', '-time'],
            },
        ),
    ]
