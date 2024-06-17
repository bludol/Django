from django.shortcuts import render, get_object_or_404, redirect

from .forms import PisnickaForm
from .models import Kapela, Osoba, Pisnicka

def index(request):
    return render(request, 'RFPapp/index.html')

def kapely_list(request):
    kapely = Kapela.objects.all()
    return render(request, 'RFPapp/kapely_list.html', {'kapely': kapely})

def osoby_list(request):
    osoby = Osoba.objects.all()
    return render(request, 'RFPapp/osoby_list.html', {'osoby': osoby})

def pisnicky_list(request):
    pisnicky = Pisnicka.objects.all()
    return render(request, 'RFPapp/pisnicky_list.html', {'pisnicky': pisnicky})

def pridej_pisnicku(request):
    if request.method == 'POST':
        form = PisnickaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pisnicky_list')
    else:
        form = PisnickaForm()
    return render(request, 'RFPapp/pridej_pisnicku.html', {'form': form})