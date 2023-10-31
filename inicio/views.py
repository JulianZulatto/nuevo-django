from django.shortcuts import render, redirect
from inicio.models import Paleta
# from django.template import loader
# from django.http import HttpResponse
from inicio.forms import CrearPaletaFormulario

# Create your views here.
def inicio(request):
    #v2
    # template = loader.get_template('inicio.html')
    # template_renderizado = template.render({})
    
    # return HttpResponse(template_renderizado)
    
    #v3
    
    return render(request, 'inicio/inicio.html', {})


def paletas(request):
    
    marca_a_buscar = request.GET.get('marca')
    
    if marca_a_buscar:
        listado_de_paletas = Paleta.objects.filter(marca__icontains=marca_a_buscar)
    else:
        listado_de_paletas = Paleta.objects.all()
        
    
    return render(request, 'inicio/paletas.html', {'listado_de_paletas': listado_de_paletas})

def crear_paleta(request):
    
    #V1 (HTML)
    # print('============')
    # print('GET')
    # print(request.GET)
    # print('============')
    # print('POST')
    # print(request.POST)
    
    # if request.method == 'POST':
    #     marca1 = request.POST.get('marca')
    #     descripcion = request.POST.get('descripcion')
    #     anio = request.POST.get('anio')
    
    #     paleta = Paleta(marca = marca1, descripcion = descripcion, anio = anio)
    #     paleta.save()
    
    #V2 DJANGO FORMS
    
    if request.method == 'POST':
        formulario = CrearPaletaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
            
            
            paleta = Paleta(marca = marca.lower(), descripcion = descripcion, anio = anio)
            paleta.save()
            
            return redirect('paletas') 
        else:
            return render(request, 'inicio/crear_paleta.html', {'formulario': formulario})
    
    formulario = CrearPaletaFormulario()
    return render(request, 'inicio/crear_paleta.html', {'formulario': formulario})
    
    