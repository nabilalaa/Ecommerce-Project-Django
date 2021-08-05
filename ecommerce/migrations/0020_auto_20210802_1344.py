# Generated by Django 3.2.5 on 2021-08-02 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0019_alter_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='total',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1, null=True),
        ),
    ]