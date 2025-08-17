from django import forms
from .models import Colaboradoes, Maquinas

class ColaboradoresForm(forms.ModelForm):
    class Meta:
        model = Colaboradoes
        fields = '__all__'

class MaquinasForm(forms.ModelForm):
    class Meta:
        model = Maquinas
        fields = '__all__'
