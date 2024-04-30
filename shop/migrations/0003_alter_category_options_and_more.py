# Generated by Django 5.0.1 on 2024-01-07 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_type_category_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.RemoveIndex(
            model_name='category',
            name='shop_catego_name_289c7e_idx',
        ),
        migrations.RemoveIndex(
            model_name='product',
            name='shop_produc_id_f21274_idx',
        ),
        migrations.RemoveIndex(
            model_name='product',
            name='shop_produc_name_a2070e_idx',
        ),
        migrations.RemoveIndex(
            model_name='product',
            name='shop_produc_created_ef211c_idx',
        ),
        migrations.RemoveIndex(
            model_name='type',
            name='shop_type_name_6853a0_idx',
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]