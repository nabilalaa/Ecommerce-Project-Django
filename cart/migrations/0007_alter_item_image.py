# Generated by Django 4.2.19 on 2025-03-06 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_alter_item_image_alter_item_urlimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to='balls/'),
        ),
    ]
