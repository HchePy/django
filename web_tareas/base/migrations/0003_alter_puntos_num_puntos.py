# Generated by Django 5.0.7 on 2024-07-29 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_puntos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puntos',
            name='num_puntos',
            field=models.IntegerField(),
        ),
    ]
