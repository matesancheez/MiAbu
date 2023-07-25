from usuario.models import Gasto
from django import forms
from django.forms import ModelForm

class GastoForm(ModelForm):
    class Meta:
        model = Gasto
        fields = '__all__'
