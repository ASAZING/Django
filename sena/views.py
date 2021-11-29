from typing import Reversible
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login as lg #logear
from django.contrib.auth import authenticate #verificar usuario

def home(request):
    return render(request, 'index.html', {
        'mensaje' : 'FELICITACIONES',
        'nonmbre' : 'matias',
        'alumnos' : [
            {'nombre' : 'malcolm', 'edad' : 21},
            {'nombre' : 'miguel', 'edad' : 18},
            {'nombre' : 'matias', 'edad' : 19},
            {'nombre' : 'yeiny', 'edad' : 16},
        ],
        'productos' : [
            {'nombre' : 'torre(completa)', 'caracteristicas': '', 'precio' : 50000, 'img': 'pc.jpg'},
            {'nombre' : 'teclado', 'caracteristicas': '', 'precio' : 18000, 'img': 'teclado.jpg'},
            {'nombre' : 'mouse', 'caracteristicas': '', 'precio' : 19000, 'img': 'mouse.png'},
            {'nombre' : 'monitor', 'caracteristicas': '', 'precio' : 600000, 'img': 'monitor.jpg'},
        ]
    })
    
def saludo2(request):
    return render(request, 'index.html', {
        'dictionario'
    })
def productos(request):
    return render(request, 'productos.html', {
        'productos' : [
            {'nombre' : 'torre(completa)', 'precio' : 50000, 'img': 'pc.jpg'},
            {'nombre' : 'teclado', 'precio' : 18000, 'img': 'teclado.jpg'},
            {'nombre' : 'mouse', 'precio' : 19000, 'img': 'mouse.png'},
            {'nombre' : 'monitor', 'precio' : 600000, 'img': 'monitor.jpg'},
        ],
        'varible' : 'Dato',
        }
    )

def login(request):
    if(request.method == 'POST'):
        user = request.POST.get('user') #capturo los valores de los campos del formulario 
        passw = request.POST.get('pass')
        usuario = authenticate(username=user, password=passw) #autentifico el usuario
        if(usuario):
            lg(request, usuario)
            return redirect('productos')
        else:
            print('No existe')
        
    return render(request, 'users/login.html', {
        'dictionario' : 'f',
    })