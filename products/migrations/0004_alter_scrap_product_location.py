# Generated by Django 4.2.5 on 2023-09-26 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20230926_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrap',
            name='product_location',
            field=models.CharField(max_length=45),
        ),
    ]
