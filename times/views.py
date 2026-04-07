from django.shortcuts import render
from .models import Time

def lista_times(request):
    times_cadastrados = Time.objects.all()
    return render(request, 'times/lista_times.html', {'times': times_cadastrados})