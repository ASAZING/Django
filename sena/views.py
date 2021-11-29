from typing import Reversible
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login as lg #logear
from django.contrib.auth import authenticate #verificar usuario
from tienda import models


def home(request):
    return render(request, 'index.html', {
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
    products = models.Product.objects.filter().order_by('created_at')
    return render(request, 'productos.html', {
        'productos' : products,
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