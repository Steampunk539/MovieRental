# Generated by Django 4.0.1 on 2022-01-24 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
