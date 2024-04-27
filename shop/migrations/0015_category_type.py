# Generated by Django 5.0.1 on 2024-01-07 19:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_category_slug_alter_type_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='shop.type'),
            preserve_default=False,
        ),
    ]
