# Generated by Django 5.0.1 on 2024-01-15 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_remove_category_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.DecimalField(decimal_places=1, max_digits=10, unique=True),
        ),
    ]
