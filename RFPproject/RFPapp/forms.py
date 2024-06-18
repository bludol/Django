from django import forms
from .models import Pisnicka

class PisnickaForm(forms.ModelForm):
    class Meta:
        model = Pisnicka
        fields = ['jmeno_pisne', 'zanr', 'kapela_jmeno']