from django.urls import path
from . import views


app_name = 'webbase'

urlpatterns = [
    path('', views.index, name='index'),

    path('success',views.success, name='success'),

    path('CategoriaView', views.CategoriaView, name='CategoriaView'),
    path('CategoriaDetailView', views.CategoriaDetailView, name='CategoriaDetailView'),
    path('AgregarAlCarro/<int:id_producto>/<int:cantidad>', views.AgregarAlCarro, name='AgregarAlCarro'),
    path('CarritoView', views.CarritoView, name='CarritoView'),
    path('update_cart/', views.update_cart, name='update_cart'),

    path('productoDetalle/<int:id_producto>', views.productoDetalle, name='productoDetalle'),

]