# Generated by Django 3.2.5 on 2021-07-25 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
