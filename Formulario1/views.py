from django.shortcuts import render

from django import forms

class CalculadoraForm(forms.Form):
    numero1 = forms.DecimalField()
    numero2 = forms.DecimalField()
    operacion = forms.ChoiceField(choices=[('suma', 'Suma'), ('resta', 'Resta'), ('multiplicacion', 'Multiplicación')])

def calcular(request):
    if request.method == 'POST':
        form = CalculadoraForm(request.POST)
        if form.is_valid():
            numero1 = form.cleaned_data['numero1']
            numero2 = form.cleaned_data['numero2']
            operacion = form.cleaned_data['operacion']

            if operacion == 'suma':
                resultado = numero1 + numero2
            elif operacion == 'resta':
                resultado = numero1 - numero2
            else:
                resultado = numero1 * numero2

            return render(request, 'calcular.html', {'form': form, 'resultado': resultado})
    else:
        form = CalculadoraForm()
    return render(request, 'calcular.html', {'form': form})