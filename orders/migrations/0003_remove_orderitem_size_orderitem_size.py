# Generated by Django 5.0.1 on 2024-01-26 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_orderitem_size_orderitem_size'),
        ('shop', '0023_alter_size_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='size',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.ManyToManyField(to='shop.size'),
        ),
    ]
