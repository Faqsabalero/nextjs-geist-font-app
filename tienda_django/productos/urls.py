from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda, name='tienda'),
    path('carrito/', views.carrito, name='carrito'),
    path('ventas/', views.ventas, name='ventas'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add_to_cart/<int:producto_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:producto_id>/', views.remove_from_cart, name='remove_from_cart'),
]
