from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext as _

class UserCustom(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False, error_messages={
        'unique': _("Un utilisateur est déjà inscrit avec cette adresse e-mail."),
    })
    phone_number = models.CharField(unique=True, max_length=15, error_messages={
        'unique': _("Un utilisateur est déjà inscrit avec ce numéro de téléphone."),
    })
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
        ('Gros-œuvre', 'Gros-œuvre'),
        ('Jardin', 'Jardin'),
        ('Divers', 'Divers'),
    ]
    
    MATERIAL_CHOICES = [
        ('Métal', 'Métal'),
        ('Plastique', 'Plastique'),
        ('Bois', 'Bois'),
        ('Verre', 'Verre'),
        ('Liquide', 'Liquide'),
        ('Poudre', 'Poudre'),
        ('Pierres', 'Pierres'),
        ('Autres', 'Autres'),
    ]

    WEIGHT_CHOICES = [
        ("Moins de 1kg", "Moins de 1kg"),
        ("Entre 1kg et 5kg", "Entre 1kg et 5kg"),
        ("Entre 5kg et 10kg", "Entre 5kg et 10kg"),
        ("Entre 10kg et 20kg", "Entre 10kg et 20kg"),
        ("Entre 20kg et 50kg", "Entre 20kg et 50kg"),
        ("Entre 50kg et 100kg", "Entre 50kg et 100kg"),
        ("Plus de 100kg", "Plus de 100kg"),
    ]
    photo1 = models.ImageField(upload_to='scraps_photos/')
    photo2 = models.ImageField(upload_to='scraps_photos/', blank=True, null=True)
    photo3 = models.ImageField(upload_to='scraps_photos/', blank=True, null=True)
    photo4 = models.ImageField(upload_to='scraps_photos/', blank=True, null=True)
    photo5 = models.ImageField(upload_to='scraps_photos/', blank=True, null=True)
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=300)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.CharField(max_length=30, choices=WEIGHT_CHOICES)
    material = ArrayField(models.CharField(max_length=20, choices=MATERIAL_CHOICES))
    category = ArrayField(models.CharField(max_length=20, choices=CATEGORY_CHOICES))
    home_pickup = models.BooleanField(default=True)
    sending = models.BooleanField(default=False)
    product_location = models.CharField(max_length=45, default="Some Default City")
    owner = models.ForeignKey('products.UserCustom', on_delete=models.CASCADE, related_name='scraps')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name