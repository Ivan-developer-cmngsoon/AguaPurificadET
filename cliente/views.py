from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Producto
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate


def index(request):
    return render(request, 'cliente/indexBefine.html')

@login_required
def crud(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'cliente/clientes_list.html', context)

@login_required
def clientes_add(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre_completo', '')
        telefono = request.POST.get('telefono', '')
        email = request.POST.get('email', '')
        direccion = request.POST.get('direccion', '')
        contrasena = request.POST.get('contraseña', '')  # Asegúrate de que el nombre del campo es 'contrasena'

        nuevo_cliente = Cliente(
            nombre=nombre,
            telefono=telefono,
            email=email,
            direccion=direccion,
            contrasena=contrasena  # Usar el nombre correcto del campo
        )
        nuevo_cliente.save()

        return redirect('crud')

    return render(request, 'cliente/clientes_add.html')

@login_required
def clientes_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        cliente.nombre = request.POST.get('nombre_completo', cliente.nombre)
        cliente.contrasena = request.POST.get('contraseña', cliente.contrasena)
        cliente.telefono = request.POST.get('telefono', cliente.telefono)
        cliente.email = request.POST.get('email', cliente.email)
        cliente.direccion = request.POST.get('direccion', cliente.direccion)
        cliente.save()
        return redirect('crud')
    return render(request, 'cliente/clientes_edit.html', {'cliente': cliente})

@login_required
def clientes_del(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        cliente.delete()
        return redirect('crud')
    return render(request, 'cliente/clientes_del.html', {'cliente': cliente})


def nosotros(request):
    return render(request, 'cliente/nosotros.html')

def productos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'cliente/productos.html', context)

def productos_list(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'cliente/productos_list.html', context)

@login_required
def producto_add(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        stock = request.POST['stock']

        nuevo_producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock
        )
        nuevo_producto.save()

        return redirect('productos_list')

    return redirect('productos_list')

@login_required
def producto_edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.save()
        return redirect('productos_list')

    productos = Producto.objects.all()
    context = {'productos': productos, 'producto': producto}
    return render(request, 'cliente/productos_list.html', context)

@login_required
def producto_del(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('productos_list')

def servicios(request):
    return render(request, 'cliente/servicios.html')

def contacto(request):
    return render(request, 'cliente/contacto.html')

def recarga(request):
    return render(request, 'cliente/recarga.html')

#login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'cliente/login.html', {'form': form})