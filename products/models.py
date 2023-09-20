from django.contrib.auth.models import AbstractUser
from django.db import models

class UserCustom(AbstractUser):
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Scrap(models.Model):
    CONDITION_CHOICES = [
        ('Comme neuf', 'Comme neuf'),
        ('Très bon état', 'Très bon état'),
        ('Correct', 'Correct'),
        ('Abîmé', 'Abîmé'),
        ('Très abîmé', 'Très abîmé'),
    ]

    CATEGORY_CHOICES = [
        ('Quincaillerie', 'Quincaillerie'),
        ('Outils', 'Outils'),
        ('Peinture', 'Peinture'),
        ('Sol', 'Sol'),
        ('Electricité', 'Electricité'),
        ('Plomberie', 'Plomberie'),
        ('Toiture', 'Toiture'),
        ('Menuiserie', 'Menuiserie'),
        ('Gros-oeuvre', 'Gros-oeuvre'),
        ('Jardin', 'Jardin'),
        ('Divers', 'Divers'),
    ]
    
    MATERIAL_CHOICES=[('Metal','Metal'),('Plastic','Plastic'),('Wood','Wood'),('Glass','Glass'),('Liquid','Liquid'),('Powders','Powders'),('Stones','Stones'),('Others','Others')]

    name = models.CharField(max_length=40)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    description = models.TextField(max_length=300)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_free = models.BooleanField(default=False)
    is_for_sell = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    home_pickup = models.BooleanField(default=True)
    sending = models.BooleanField(default=False)
    weight = models.CharField(max_length=20)
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES)

    owner = models.ForeignKey('products.UserCustom', on_delete=models.CASCADE, related_name='scraps')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name