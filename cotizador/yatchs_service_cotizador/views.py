from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .forms import ServicioForm, EmpresaForm, ClienteForm, ProductoForm
from .models import Servicio, Empresa, Cliente, Producto


# Create your views here.

    #template = get_template("formato-cotizacion.html")

    #html = template.render()

    # crea uan respuesta HTTP con el contenido del pdf y le dice al navegador que el archivo es un pdf para que lo abra 
    #response = HttpResponse(content_type="application/pdf") 
    
    #le dice al navegador que es una archivo y que lo abra en una pestaña y el nombre del archivo 
    #response['Content-disposition'] = 'inline; filename="cotizacion.pdf"'

    #pisa_status = pisa.CreatePDF(html, dest=response)
def cotizador (request):
    #queryset de los datos para las tablas

    servicios = Servicio.objects.all()
    productos = Producto.objects.all()
    empresas = Empresa.objects.all()
    clientes = Cliente.objects.all()

    #diccionario para juntar tanto el servicio como los productos 
    items = []

    for p in productos:
        items.append({
            "id": p.id,
            "tipo": "Producto",
            "nombre": p.nombre,
            "codigo": p.codigo,
            "precio": p.precio,
        })
    
    for s in servicios:
        items.append({
            "id": s.id,
            "tipo": "Servicio",
            "nombre": s.nombre,
            "codigo": None,
            "precio" : s.precio,
        })


    #formularios 
    contexto = {
        'form_servicio' : ServicioForm(),
        'form_producto' : ProductoForm(),
        'form_empresa' : EmpresaForm(),
        'form_cliente' : ClienteForm(),
        'servicios' : servicios,
        'productos' : productos,
        'empresas' : empresas,
        'clientes' : clientes,
        'items': items
    }
    return render(request, "base.html", contexto)

def crear_servicio(request):
    if request.method == 'POST':
        servicio_id = request.POST.get("id")
        if servicio_id:
            servicio = Servicio.objects.get(id=servicio_id)
            form = ServicioForm(request.POST, instance=servicio)
        else:
            form = ServicioForm(request.POST)
        if form.is_valid():   
            form.save()
            return redirect('home')
    else:
        form = ServicioForm()
    return render(request, "base.html", {"form_servicio": form})

def eliminar_servicio(request, servicio_id):
    servicio = Servicio.objects.get(id=servicio_id)
    servicio.delete()
    return redirect("home")

def crear_empresa(request):
    if request.method == 'POST':
        empresa_id = request.POST.get("id")
        if empresa_id:
            empresa = Empresa.objects.get(id=empresa_id)
            form = EmpresaForm(request.POST, request.FILES, instance=empresa)
        else:
        #request.FILES es para poder subir el logo de la empresa
            form = EmpresaForm(request.POST, request.FILES) 
        if form.is_valid():   
            form.save()
            return redirect('home')
    return render(request, "base.html", {"form_empresa": form})

def eliminar_empresa(request, empresa_id):
    empresa = Empresa.objects.get(id=empresa_id)
    empresa.delete()
    return redirect('home')


def crear_producto(request):
    if request.method == 'POST':
        producto_id = request.POST.get("id")
        if producto_id:
            producto = Producto.objects.get(id=producto_id)
            form = ProductoForm(request.POST, instance=producto)
        else:
            form = ProductoForm(request.POST)
        if form.is_valid():   
            form.save()
            return redirect('home')
    return render(request, "base.html", {"form_producto": form})

def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()
    return redirect('home')


def crear_cliente(request):
    if request.method == 'POST':
        cliente_id = request.POST.get("id")
        if cliente_id:
            cliente = Cliente.objects.get(id=cliente_id)
            form = ClienteForm(request.POST, instance=cliente)
        else:
            form = ClienteForm(request.POST)
            
        if form.is_valid():   
            form.save()
            return redirect('home')
    
    return render(request, "base.html", {"form_cliente": form})


def eliminar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    cliente.delete()
    return redirect('home')








