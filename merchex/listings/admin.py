"""Missing"""
from django.contrib import admin
from .models import Band
from .models import Listing


class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes
    """Missing"""
    list_display = ('title', 'band')  # ajouter ‘band' ici
    list_display = ('name', 'year_formed', 'genre')
    # liste les champs que nous voulons sur l'affichage de la liste


admin.site.register(Band, BandAdmin)
admin.site.register(Listing)
