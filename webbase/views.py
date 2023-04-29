from django.shortcuts import render,redirect 
from django.urls import reverse
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import Producto,Categoria,Carro
import random
from django.core.exceptions import ObjectDoesNotExist

from django.http import JsonResponse


def index(request):
    prods = Producto.objects.order_by('?')[:5] 
    user = request.user
    prods_list = Carro.objects.filter(id_usuario=request.user.id).values('id_producto')
    cart_count = Carro.objects.filter(id_usuario=request.user.id).count()
    context={'prods': prods,'cart_count':cart_count,'prods_list':prods_list}
    
    return render(request, 'index.html',context )

def CategoriaView(request):
    cate = Categoria.objects.all()
    return render(request, 'categorias/categorias.html',{'cate':cate})

def CategoriaDetailView(request):
    return render(request, 'categorias/categoriasGrid.html')



def AgregarAlCarro(request,id_producto,cantidad):
    user_id = request.user.id

    try:
        carroXusuarioXproducto = Carro.objects.get(id_usuario=user_id, id_producto=id_producto)
        carroXusuarioXproducto.cantidad = carroXusuarioXproducto.cantidad + 1
        carroXusuarioXproducto.save()
        success_message = "item agregado exitosamente"
        print(success_message)
        return HttpResponseRedirect(reverse('webbase:success'))
    except ObjectDoesNotExist:
        print('id_producto',id_producto)
        nuevoItem = Carro.objects.create(
            id_usuario=user_id,
            id_producto=id_producto,
            cantidad=cantidad
        )
        nuevoItem.save()
        success_message = "item agregado exitosamente"
        return HttpResponseRedirect(reverse('webbase:success'))


def success(request):
    return render(request,'success.html')


def CarritoView(request):
    user_id = request.user.id
    productos = Carro.objects.filter(id_usuario=user_id)
    productos_list = []
    total = 0

    for producto in productos:
        prod = Producto.objects.get(id=producto.id_producto)
        prod.cantidad = producto.cantidad
        prod.subtotal = prod.precio * producto.cantidad
        productos_list.append(prod)

        # Add the subtotal of this product to the total if it is selected
        if str(producto.id) in request.POST.getlist('selected_items'):
            total += prod.subtotal

    return render(request, 'carrito.html',{'productos':productos_list, 'total': total})

def update_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        action = request.POST.get('action')
        
        product = Producto.objects.get(id=product_id)
        
        if action == 'add':
            item = Carro.objects.get(id_producto=product_id, id_usuario=request.user.id)
            item.cantidad += 1
            item.save()
        elif action == 'remove':
            item = Carro.objects.get(id_producto=product_id, id_usuario=request.user.id)
            item.cantidad -= 1
            item.save()
        elif action == 'delete':
            item = Carro.objects.get(id_producto=product_id, id_usuario=request.user.id)
            item.delete()
        return redirect('webbase:CarritoView')

    user_id = request.user.id
    productos = Carro.objects.filter(id_usuario=user_id)
    productos_list = []

    for producto in productos:
        prod = Producto.objects.get(id=producto.id_producto)
        prod.cantidad = producto.cantidad
        prod.subtotal = prod.precio * producto.cantidad
        productos_list.append(prod)

    return render(request, 'carrito.html', {'productos': productos_list})


def productoDetalle(request,id_producto):
    user_id = request.user.id
    producto = Producto.objects.get(id=id_producto)

    return render(request, 'productoDetalle.html',{'producto':producto})