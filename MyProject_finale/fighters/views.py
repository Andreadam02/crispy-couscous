from django.shortcuts import render, redirect
from .models import Fighter 
from django.http import JsonResponse, HttpResponseRedirect
from django.conf import settings
import os
from .forms import FighterForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def fighters(request):
    fighters = Fighter.objects.all()
    return render(request, 'fighters/sito web.html', {'fighters': fighters})

def statistiche(request):
    return render(request, 'fighters/statistiche.html')

from django.conf import settings
import os

def input(request):
    if request.method == 'POST':
        form = FighterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FighterForm()
    return render(request, 'fighters/input.html', {'form': form})

@csrf_exempt  # Applica il decoratore csrf_exempt per le richieste AJAX (assicurati di importarlo)
def vota_fighter(request):
    if request.method == 'POST':
        fighter_id = request.POST.get('fighter_id')
        rating = request.POST.get('rating')

        # Verifica che i dati ricevuti siano validi
        if fighter_id and rating:
            try:
                fighter = Fighter.objects.get(pk=fighter_id)
                # Aggiorna il punteggio del lottatore
                fighter.rating = rating
                fighter.save()
                # Restituisci la risposta JSON
                return JsonResponse({'success': True, 'rating': rating})
            except Fighter.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'Lottatore non trovato'})
        else:
            return JsonResponse({'success': False, 'message': 'Dati non validi'})

    return JsonResponse({'success': False, 'message': 'Richiesta non valida'})