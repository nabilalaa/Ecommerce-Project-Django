# Generated by Django 4.2.19 on 2025-03-03 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0028_register'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CheckOut',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.RemoveField(
            model_name='register',
            name='username',
        ),
        migrations.DeleteModel(
            name='Total',
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
