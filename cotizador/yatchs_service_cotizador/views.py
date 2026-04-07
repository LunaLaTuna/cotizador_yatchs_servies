from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .forms import ServicioForm, EmpresaForm, ClienteForm, ProductoForm


# Create your views here.

    #template = get_template("formato-cotizacion.html")

    #html = template.render()

    # crea uan respuesta HTTP con el contenido del pdf y le dice al navegador que el archivo es un pdf para que lo abra 
    #response = HttpResponse(content_type="application/pdf") 
    
    #le dice al navegador que es una archivo y que lo abra en una pestaña y el nombre del archivo 
    #response['Content-disposition'] = 'inline; filename="cotizacion.pdf"'

    #pisa_status = pisa.CreatePDF(html, dest=response)
def cotizador (request):
    contexto = {
        'form_servicio' : ServicioForm(),
        'form_producto' : ProductoForm(),
        'form_empresa' : EmpresaForm(),
        'form_cliente' : ClienteForm()
    }
    return render(request, "base.html", contexto)

def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():   
            form.save()
            return redirect('home')
    else:
        form = ServicioForm()
    return render(request, "base.html", {"form_servicio": form})

def crear_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES)
        if form.is_valid():   
            form.save()
            return redirect('home')
    else:
        form = EmpresaForm()
    return render(request, "base.html", {"form_empresa": form})


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():   
            form.save()
            return redirect('home')
    else:
        form = ProductoForm()
    return render(request, "base.html", {"form_producto": form})



def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():   
            form.save()
            return redirect('home')
    else:
        form = ClienteForm()
    return render(request, "base.html", {"form_cliente": form})




