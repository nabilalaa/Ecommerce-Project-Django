# Generated by Django 3.2.5 on 2021-07-31 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0018_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1, max_length=8, null=True),
        ),
    ]
