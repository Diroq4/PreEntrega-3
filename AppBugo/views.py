# En views.py
from django.shortcuts import render, redirect
from .models import Categoria, Producto, Cliente
from .forms import CategoriaForm, ProductoForm, ClienteForm

def categorias(request):
    # Obtener todas las categorías
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save()
            return redirect('cliente')
    else:
        form = CategoriaForm()

    # Pasar la lista de categorías al contexto
    return render(request, 'categoria.html', {'form': form, 'categorias': categorias})


def productos(request):
    # Obtener todos los productos
    productos = Producto.objects.all()

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            return redirect('cliente')
    else:
        form = ProductoForm()

    # Pasar la lista de productos al contexto
    return render(request, 'producto.html', {'form': form, 'productos': productos})


def clientes(request):
    # Obtener todos los clientes
    clientes = Cliente.objects.all()

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return redirect('cliente')
    else:
        form = ClienteForm()

    # Pasar la lista de clientes al contexto
    return render(request, 'cliente.html', {'form': form, 'clientes': clientes})
