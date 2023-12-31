# Generated by Django 4.2.5 on 2023-09-26 10:34

from django.db import migrations, models

def fill_product_location(apps, schema_editor):
    Scrap = apps.get_model('products', 'Scrap')
    for scrap in Scrap.objects.all():
        if not scrap.product_location:
            scrap.product_location = scrap.owner.city
            scrap.save()

class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_scrap_is_for_sell_remove_scrap_is_free_and_more'),
    ]

    operations = [
        migrations.RunPython(fill_product_location),
    ]
