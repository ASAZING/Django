from typing import Reversible
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login as lg #logear
from django.contrib.auth import authenticate #verificar usuario
from tienda import models


def home(request):
    products = models.Product.objects.filter().order_by('created_at')
    return render(request, 'index.html', {
        'productos' : products,
    })
    
def productos(request):
    products = models.Product.objects.filter().order_by('created_at')
    return render(request, 'productos.html', {
        'productos' : products,
        'varible' : 'Dato',
        }
    )

def detalle(request,id_product):
    producto = get_object_or_404(models.Product, pk=id_product)
    return render(request,'detalle.html',{
        'producto' : producto
  })

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