# Generated by Django 5.0.1 on 2024-01-12 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_alter_size_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.FloatField(unique=True),
        ),
    ]
