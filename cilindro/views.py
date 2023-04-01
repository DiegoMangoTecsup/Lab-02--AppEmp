from django.shortcuts import render
from .forms import CilindroForm
import math

def calcular_volumen(request):
    if request.method == 'POST':
        form = CilindroForm(request.POST)
        if form.is_valid():
            altura = form.cleaned_data['altura']
            diametro = form.cleaned_data['diametro']
            radio = diametro / 2
            volumen = math.pi * radio ** 2 * altura
            return render(request, 'resultado.html', {'volumen': volumen})
    else:
        form = CilindroForm()
    return render(request, 'formulario.html', {'form': form})