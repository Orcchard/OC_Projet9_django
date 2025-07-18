"""
- name (CharField) : Nom du groupe.
    - description (CharField) : Description courte du groupe.
    - biography (CharField) : Biographie détaillée du groupe.
    - genre (CharField) : Genre musical, choisi parmi une liste
    prédéfinie (Genre).
    - year_formed (IntegerField) : Année de formation du groupe,
    entre 1300 et 2021.
    - active (BooleanField) : Indique si le groupe est toujours actif.
    - official_homepage (URLField) : URL officielle du groupe (optionnel).
    - sold (BooleanField) : Indique si le produit est vendu.
    - type (CharField) : Type de produit associé, parmi
    une liste prédéfinie (Type).
    - like_new (BooleanField) : Indique si l'objet est en état "comme neuf".
    """
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Band(models.Model):
    """Création des champs de la table band """
    class Genre(models.TextChoices):
        """Missing"""
        ALTERNATIVE_ROCK = 'AR'
        BLUES = 'BL'
        CLASSICAL = 'CL'
        HIP_HOP = 'HH'
        HARD_ROCK = 'HR'
        REGGAE = 'RG'
        SYNTH_POP = 'SP'

    class Type(models.TextChoices):
        """Missing"""
        DISQUES = 'Records'
        VETEMENTS = "Clothing"
        AFFICHES = 'Posters'
        DIVERS = 'Miscellaneous'

    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=100)
    # default="Sans titre"
    biography = models.fields.CharField(max_length=1000)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    # ou un choix, par exemple
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1300), MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    sold = models.fields.BooleanField(default=False)
    type = models.fields.CharField(choices=Type.choices, max_length=15)
    like_new = models.fields.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class Listing(models.Model):
    """Missing"""
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'

    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
