from django.shortcuts import render
from .models import *

def index(request):
    my_list = ['Элзат', 'Умар', 'Жакшылык']

    rows = StudentsModel.objects.all()

    context = {
        'students':my_list,
        'dataBaseStudents': rows
    }

    return render(request, 'main.html', context)
