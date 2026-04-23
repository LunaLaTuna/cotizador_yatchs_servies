from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
import io
from django.core.files.base import ContentFile
from xhtml2pdf import pisa
from .forms import ServicioForm, EmpresaForm, ClienteForm, ProductoForm, AgenteForm, BuscarForm
from .models import Servicio, Empresa, Cliente, Producto, Agente, Cotizacion, DetalleCotizacion
from django.conf import settings
import os
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Q
from django.contrib import messages
from django.views.decorators.cache import never_cache

# Create your views here.

def cotizador (request):
    #queryset de los datos para las tablas

    servicios = Servicio.objects.all()
    productos = Producto.objects.all()
    empresas = Empresa.objects.all()
    clientes = Cliente.objects.all()
    agentes = Agente.objects.all()
    cotizaciones = Cotizacion.objects.all()


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


     #obtener el numero de cotizacion
    ultimo = Cotizacion.objects.order_by("-id").first()
    siguiente_numero = 1 if not ultimo else ultimo.id + 1
    numero_front = f"COT-{siguiente_numero:05d}"

    #formularios 
    contexto = {
        'form_servicio' : ServicioForm(),
        'form_producto' : ProductoForm(),
        'form_empresa' : EmpresaForm(),
        'form_cliente' : ClienteForm(),
        'form_agente' : AgenteForm(),
        'form_buscar' :BuscarForm(),
        'servicios' : servicios,
        'productos' : productos,
        'empresas' : empresas,
        'agentes' : agentes,
        'clientes' : clientes,
        'items': items,
        'cotizaciones' : cotizaciones,
        'numero_front' : numero_front
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
            nombre = form.cleaned_data.get("nombre")
            if not servicio_id and Servicio.objects.filter(nombre=nombre).exists():
                messages.error(request, f"Ya existe un servicio con el nombre '{nombre}'.")
                return redirect('home')
            else:
                form.save()
                messages.success(request, "Servicio guardado correctamente.")
                return redirect('home')
        else:
            messages.error(request, "Revisa los errores en el formulario.")
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
            nombre = form.cleaned_data.get("nombre")
            if not empresa_id and Empresa.objects.filter(nombre=nombre).exists():
                messages.error(request, f"Ya existe una empresa con el nombre '{nombre}'.")
                return redirect('home')
            else:
                form.save()
                messages.success(request, "Empresa guardada correctamente.")
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
            codigo = form.cleaned_data.get("codigo")
            if not producto_id and Producto.objects.filter(codigo=codigo).exists():
                messages.error(request, f"Ya existe un producto con el código '{codigo}'.")
                return redirect('home')
            else:
                form.save()
                messages.success(request, "Producto guardado correctamente.")
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
            telefono = form.cleaned_data.get("telefono")
            if not agente_id and Agente.objects.filter(telefono=telefono).exists():
                messages.error(request, f"Ya existe un Agente con el teléfono: '{telefono}'.")
                return redirect('home')
            else:
                form.save()
                messages.success(request, "Agente guardado correctamente.")
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
            correo = form.cleaned_data.get("correo")
            if not cliente_id and Cliente.objects.filter(correo=correo).exists():
                messages.error(request, f"Ya existe un Cliente con el correo:'{correo}'.")
                return redirect('home')
            else:
                form.save()
                messages.success(request, "Cliente guardado correctamente.")
                return redirect('home')
    
    return render(request, "base.html", {"form_cliente": form})


def eliminar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    cliente.delete()
    return redirect('home')

def guardar_cotizacion(request):
    if request.method == 'POST':
        try:

            cliente_id = request.POST.get('cliente_id')
            empresa_id = request.POST.get('empresa_id')
            agente_id = request.POST.get('agente_id')
            
            cotizacion = Cotizacion.objects.create(
                cliente_id=cliente_id,
                empresa_id=empresa_id,
                fecha_creacion=request.POST.get('fecha'),
                subtotal=request.POST.get('input_subtotal_general'),
                iva=request.POST.get('input_iva'),
                total=request.POST.get('input_total'),
                agente_id=agente_id,
                fecha_caducidad = request.POST.get('fecha_caducidad')
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

    #guardar pdf
    pdf_file = io.BytesIO()
    pisa.CreatePDF(io.StringIO(html), dest=pdf_file)

    ruta = os.path.join(settings.MEDIA_ROOT, "pdfs", f"cotizacion_{cotizacion.id}.pdf")
    os.makedirs(os.path.dirname(ruta), exist_ok=True)

    
    cotizacion.pdf_file.save(
        f"cotizacion_{cotizacion.id}.pdf",
        ContentFile(pdf_file.getvalue()),
        save=True
    )

    #crea uan respuesta HTTP con el contenido del pdf y le dice al navegador que el archivo es un pdf para que lo abra 
    response = HttpResponse(content_type="application/pdf") 
    
    #le dice al navegador que es una archivo y que lo abra en una pestaña y el nombre del archivo 
    response['Content-disposition'] = 'inline; filename="cotizacion.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse("Error en el pdf", status=500)
    return response



def busqueda_ajax(request):
    q = request.GET.get("q", "")
    page = request.GET.get("page", 1)

    cotizaciones = Cotizacion.objects.filter(
        Q(numero_cotizacion__icontains=q) | 
        Q(cliente__nombre__icontains=q)| 
        Q(empresa__nombre__icontains=q) | 
        Q(agente__nombre__icontains=q) | 
        Q(fecha_caducidad__icontains=q) | 
        Q(fecha_creacion__icontains=q) | 
        Q(subtotal__icontains=q) | 
        Q(iva__icontains=q) | 
        Q(total__icontains=q)
        )
    paginator = Paginator(cotizaciones, 10)
    page_obj = paginator.get_page(page)

    data = {
        "resultados" : [{"numero_cotizacion" : p.numero_cotizacion, 
                        "empresa" : p.empresa.nombre, 
                        "cliente" : p.cliente.nombre, 
                        "fecha_caducidad": p.fecha_caducidad.strftime("%Y-%m-%d"),
                        "fecha_creacion": p.fecha_creacion.strftime("%Y-%m-%d"), 
                        "agente" : p.agente.nombre,
                        "subtotal" : float(p.subtotal), 
                        "iva" : float(p.iva), 
                        "total": float(p.total),
                        "pdf_url" : p.pdf_file.url if p.pdf_file else None,
                        
                        } for p in page_obj],
        "num_paginas" : paginator.num_pages,
        "paginas_actial": page_obj.number,
    }
    return JsonResponse(data)

