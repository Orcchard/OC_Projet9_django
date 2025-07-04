"""Missing"""
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm
# from django.http import HttpResponse
from django.shortcuts import render


def band_list(request):
    """Missing"""
    bands = Band.objects.all()
    return render(
        request,
        'listings/band_list.html',
        {'bands': bands})


def about(request):
    """ Affiche Nous adorons merch sur la page web"""
    return render(request, 'listings/about.html')


def listing(request):
    """Missing"""
    listing_data = Listing.objects.all()
    return render(request, 'listings/listing.html', {'listing': listing_data})


def contact(request):
    """Missing"""
    # ajoutez ces instructions d'impression afin que nous
    # puissions jeter un coup d'oeil à « request.method »
    # et à « request.POST »
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)
    form = ContactUsForm()  # ajout d’un nouveau formulaire ici
    return render(
        request,
        'listings/contact.html',
        {'form': form})  # passe ce formulaire au gabarit)


def band_detail(request, band_id):  # notez le paramètre id supplémentaire
    """Missing"""
    band = Band.objects.get(id=band_id)  # on utilise band_id ici
    return render(
        request,
        'listings/band_detail.html',
        {'band': band})  # nous passons l'id au modèle
