# Generated by Django 5.0.1 on 2024-01-07 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_category_options_alter_product_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]