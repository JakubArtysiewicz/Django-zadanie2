from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Store
# Create your views here.

def index(request):
    employees = Employee.objects.all()
    return render(request, 'index.html', {'employees': employees})

# Views który po wpisaniu pola ID z modelu Store wyświetli odpowiednie dane w HttpResponse
def store(request, id):
    dane_z_id_store = Store.objects.filter(id=id)
    return HttpResponse(str(dane_z_id_store))
