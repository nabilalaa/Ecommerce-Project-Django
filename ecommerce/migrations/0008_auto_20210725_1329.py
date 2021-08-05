# Generated by Django 3.2.5 on 2021-07-25 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_alter_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('password', models.TextField(max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]