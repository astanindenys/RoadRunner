# Generated by Django 5.0.2 on 2024-05-17 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0032_alter_size_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.FloatField(unique=True),
        ),
    ]
