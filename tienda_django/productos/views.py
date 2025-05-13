from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Producto, Venta

def login_view(request):
    """
    Vista para el login de usuarios
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("tienda")
        else:
            return render(request, "productos/login.html", {"error": "Credenciales inválidas"})
    return render(request, "productos/login.html")

@login_required
def logout_view(request):
    """
    Vista para cerrar sesión
    """
    logout(request)
    return redirect("login")

@login_required
def tienda(request):
    """
    Vista para mostrar la tienda con productos
    """
    productos = Producto.objects.all()
    return render(request, "productos/tienda.html", {"productos": productos})

@login_required
def carrito(request):
    """
    Vista para mostrar el carrito de compras
    """
    carrito = request.session.get("carrito", {})
    productos_carrito = []
    total = 0
    for producto_id, cantidad in carrito.items():
        try:
            producto = Producto.objects.get(id=producto_id)
            subtotal = producto.precio * cantidad
            total += subtotal
            productos_carrito.append({
                "producto": producto,
                "cantidad": cantidad,
                "subtotal": subtotal,
            })
        except Producto.DoesNotExist:
            pass
    return render(request, "productos/carrito.html", {"productos_carrito": productos_carrito, "total": total})

@login_required
def ventas(request):
    """
    Vista para mostrar la tabla de ventas con costo y ganancia
    """
    ventas = Venta.objects.all()
    return render(request, "productos/ventas.html", {"ventas": ventas})

@login_required
def add_to_cart(request, producto_id):
    """
    Añadir un producto al carrito usando sesión
    """
    carrito = request.session.get("carrito", {})
    carrito[str(producto_id)] = carrito.get(str(producto_id), 0) + 1
    request.session["carrito"] = carrito
    return redirect("tienda")

@login_required
def remove_from_cart(request, producto_id):
    """
    Remover un producto del carrito usando sesión
    """
    carrito = request.session.get("carrito", {})
    if str(producto_id) in carrito:
        del carrito[str(producto_id)]
        request.session["carrito"] = carrito
    return redirect("carrito")
