# Generated by Django 4.2.5 on 2023-10-09 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_usercustom_email_alter_usercustom_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrap',
            name='product_location',
        ),
    ]