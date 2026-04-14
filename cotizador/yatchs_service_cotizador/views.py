from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .forms import ServicioForm, EmpresaForm, ClienteForm, ProductoForm, AgenteForm
from .models import Servicio, Empresa, Cliente, Producto, Agente, Cotizacion, DetalleCotizacion,  Cotizacion
from django.conf import settings
import os

# Create your views here.

def cotizador (request):
    #queryset de los datos para las tablas

    servicios = Servicio.objects.all()
    productos = Producto.objects.all()
    empresas = Empresa.objects.all()
    clientes = Cliente.objects.all()
    agentes = Agente.objects.all()


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
        'form_agente' : AgenteForm(),
        'servicios' : servicios,
        'productos' : productos,
        'empresas' : empresas,
        'agentes' : agentes,
        'clientes' : clientes,
        'items': items,
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

def crear_agente(request):
    if request.method == 'POST':
        agente_id = request.POST.get("id")
        if agente_id:
            agente = Agente.objects.get(id=agente_id)
            form = AgenteForm(request.POST, instance=agente)
        else:
            form = AgenteForm(request.POST)
        if form.is_valid():   
            form.save()
            return redirect('home')
    return render(request, "base.html", {"agente_form": form})

def eliminar_agente(request, agente_id):
    agente = Agente.objects.get(id=agente_id)
    agente.delete()
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

def guardar_cotizacion(request):
    if request.method == 'POST':
        try:
            # Crear la cotización
            cliente_id = request.POST.get('cliente_id')
            empresa_id = request.POST.get('empresa_id')
            agente_id = request.POST.get('agente_id')
            
            cotizacion = Cotizacion.objects.create(
                cliente_id=cliente_id,
                empresa_id=empresa_id,
                fecha=request.POST.get('fecha'),
                subtotal=request.POST.get('input_subtotal_general'),
                iva=request.POST.get('input_iva'),
                total=request.POST.get('input_total'),
                numero_cotizacion=1,
                agente_id=agente_id
            )
            
            nombres = request.POST.getlist('detalle_nombre')
            tipos  = request.POST.getlist('detalle_tipo')
            codigos = request.POST.getlist('detalle_codigo')
            cantidades = request.POST.getlist('detalle_cantidad')
            precios = request.POST.getlist('detalle_precio')
            subtotales = request.POST.getlist('detalle_subtotal')

            for i in range(len(nombres)):
                # Determinar si es producto o servicio
                producto = None
                servicio = None
                
                if tipos[i] == "Producto":
                    try:
                        producto = Producto.objects.get(nombre=nombres[i], codigo=codigos[i])
                    except Producto.DoesNotExist:
                        pass
                elif tipos[i] == "Servicio":
                    try:
                        servicio = Servicio.objects.get(nombre=nombres[i])
                    except Servicio.DoesNotExist:
                        pass
                
                # Crear el detalle de la cotización
                DetalleCotizacion.objects.create(
                    cotizacion=cotizacion,
                    producto=producto,
                    servicio=servicio,
                    cantidad=int(cantidades[i]),
                    subtotal=float(subtotales[i])
                )
            
            return redirect('crear_pdf', cotizacion_id=cotizacion.id)
        except Exception as e:
            print(f"Error al guardar la cotización: {str(e)}")
            return render(request, "base.html", {"error": str(e)})
    

def detalle_cotizacion(request, cotizacion_id):
    cotizacion = Cotizacion.objects.get(id=cotizacion_id)
    return render(request, "base.html", {"cotizacion": cotizacion})

def crear_pdf(request, cotizacion_id):
    cotizacion = Cotizacion.objects.get(id=cotizacion_id)
    detalles = cotizacion.detallecotizacion_set.all()
    empresa = cotizacion.empresa
    logo_path = os.path.join(settings.MEDIA_ROOT, str(empresa.logo))

    template = get_template("cotizacion-pdf.html")
    html = template.render({"cotizacion": cotizacion, "detalles" : detalles, "logo_path" : logo_path})

    #crea uan respuesta HTTP con el contenido del pdf y le dice al navegador que el archivo es un pdf para que lo abra 
    response = HttpResponse(content_type="application/pdf") 
    
    #le dice al navegador que es una archivo y que lo abra en una pestaña y el nombre del archivo 
    response['Content-disposition'] = 'inline; filename="cotizacion.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse("Error en el pdf", status=500)
    return response








