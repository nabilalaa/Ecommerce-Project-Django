# Generated by Django 3.2.5 on 2021-07-31 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0012_alter_login_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='user',
        ),
        migrations.AddField(
            model_name='checkout',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product'),
        ),
    ]
