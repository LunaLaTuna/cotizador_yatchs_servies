from django import forms
from .models import Servicio, Producto,  Empresa, Cliente, Agente

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'precio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Servicio'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio del servicio'}),
        }  
        

class ProductoForm(forms.ModelForm):
    class Meta:
        model =  Producto
        fields = ['nombre', 'codigo', 'precio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Producto'}),
            'codigo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Codigo del Producto'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio del Producto'}),
        }  
       

class EmpresaForm(forms.ModelForm):
    class Meta: 
        model= Empresa
        fields = ['nombre', 'tipo','dueño' , 'direccion', 'logo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la empresa'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo de Empresa'}),
            'dueño': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dueño de la Empresa '}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Direccion'}),
            'logo': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Logo de la Empresa'}),
        }  
        


class ClienteForm(forms.ModelForm):
    class Meta:
        model= Cliente
        fields = ['nombre', 'apellido', 'direccion' , 'telefono', 'correo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Cliente'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'correo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo'}),
        }   
    

class AgenteForm(forms.ModelForm):
    class Meta:
        model= Agente
        fields = ['nombre', 'apellido', 'telefono' , 'empresa']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre '}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'empresa': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Empresa'}),
        }   

class BuscarForm(forms.Form):
    query = forms.CharField(label="Busqueda", max_length=100)
