# Generated by Django 3.2 on 2021-04-23 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateTimeField(default='1998-01-28'),
            preserve_default=False,
        ),
    ]
