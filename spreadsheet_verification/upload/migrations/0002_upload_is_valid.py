# Generated by Django 4.1.5 on 2024-05-31 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='is_valid',
            field=models.BooleanField(default=False),
        ),
    ]
