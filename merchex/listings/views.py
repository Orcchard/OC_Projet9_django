"""Missing"""
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm
# from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect  # ajoutez cet import
from django.core.mail import send_mail


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
    # ...nous pouvons supprimer les déclarations de
    # journalisation qui étaient ici...

    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir
        # avec les données POST
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
                )
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
        return redirect('email-sent')  # ajoutez cette instruction de retour
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
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


def received(request):
    """Affiche une page confirmant l'envoi de l'email"""
    return render(request, 'listings/email_sent.html')
