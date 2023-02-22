from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def inicio(request):
    return render(request, 'paginas/inicio.html')

@login_required
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

@login_required
def libros(request):
    libros = Libro.objects.all() # Traemos todos los datos del objeto
    return render(request, 'libros/index.html', {'Libros':libros})

@login_required
def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        return redirect('libros') 
    return render(request, 'libros/crear.html', {'formulario': formulario})

@login_required
def editar(request, id):
    libro1 = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro1)
    if formulario.is_valid and request.POST:
        formulario.save()
        return redirect('libros') 
    return render(request, 'libros/editar.html', {'formulario':formulario})

def borrar(request, id):
   record = Libro.objects.get(id = id)
   record.delete()
   return redirect('libros')