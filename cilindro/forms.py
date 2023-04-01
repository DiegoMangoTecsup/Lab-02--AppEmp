from django import forms

class CilindroForm(forms.Form):
    altura = forms.FloatField(label='Altura (m)')
    diametro = forms.FloatField(label='Diámetro (m)')