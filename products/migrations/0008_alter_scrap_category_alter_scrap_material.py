# Generated by Django 4.2.5 on 2023-09-26 14:27

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_scrap_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrap',
            name='category',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('Quincaillerie', 'Quincaillerie'), ('Outils', 'Outils'), ('Peinture', 'Peinture'), ('Sol', 'Sol'), ('Electricité', 'Electricité'), ('Plomberie', 'Plomberie'), ('Toiture', 'Toiture'), ('Menuiserie', 'Menuiserie'), ('Gros-œuvre', 'Gros-œuvre'), ('Jardin', 'Jardin'), ('Divers', 'Divers')], max_length=20), size=None),
        ),
        migrations.AlterField(
            model_name='scrap',
            name='material',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('Métal', 'Métal'), ('Plastique', 'Plastique'), ('Bois', 'Bois'), ('Verre', 'Verre'), ('Liquide', 'Liquide'), ('Poudre', 'Poudre'), ('Pierres', 'Pierres'), ('Autres', 'Autres')], max_length=20), size=None),
        ),
    ]
