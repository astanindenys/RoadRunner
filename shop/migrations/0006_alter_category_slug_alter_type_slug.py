# Generated by Django 5.0.1 on 2024-01-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_type_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
        migrations.AlterField(
            model_name='type',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]