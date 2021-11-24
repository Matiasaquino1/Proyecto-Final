from django.shortcuts import redirect, render

from .forms import Entrenadorfrom, Sociosfrom, Salasfrom, Actividadfrom, Aparatosfrom, Clasesfrom, clases_sociosfrom, entrenador_tipoactividadfrom

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def Home(request):

    if request.method == 'POST':
        aparatosform = Aparatosfrom(request.POST)
        if aparatosform.is_valid():
            aparatosform.save()
            return redirect('/libro')
    else:
        aparatosform = Aparatosfrom()
    return render(request, 'Libro/aparatos.html', {'form': aparatosform})

def Home1(request):
    if request.method == 'POST':
        salasform = Salasfrom(request.POST)
        if salasform.is_valid():
            salasform.save()
            return redirect('/libro')
    else:
        salasform = Salasfrom()
    return render(request, 'Libro/salas.html',{'form': salasform})

def Home2(request):
    if request.method == 'POST':
        usuarioform = Sociosfrom(request.POST)
        if usuarioform.is_valid():
            usuarioform.save()
            return redirect('/libro')
    else:
        usuarioform = Sociosfrom()
    return render(request, 'Libro/socios.html',{'form': usuarioform})

def Home3(request):
    if request.method == 'POST':
        entrenadorform = Entrenadorfrom(request.POST)
        if entrenadorform.is_valid():
            entrenadorform.save()
            return redirect('/libro')
    else:
        entrenadorform = Entrenadorfrom()
    return render(request, 'Libro/entrenador.html',{'form': entrenadorform})


def Home4(request):
    if request.method == 'POST':
        clasesform = Clasesfrom(request.POST)
        if clasesform.is_valid():
            clasesform.save()
            return redirect('/libro')
    else:
        clasesform = Clasesfrom()
    return render(request, 'Libro/clases.html',{'form': clasesform})

def Home5(request):
    if request.method == 'POST':
        actividadform = Actividadfrom(request.POST)
        if actividadform.is_valid():
            actividadform.save()
            return redirect('/libro')
    else:
        actividadform = Actividadfrom()
    return render(request, 'Libro/actividad.html',{'form': actividadform})


def Home6(request):
    if request.method == 'POST':
        clase_socio = clases_sociosfrom(request.POST)
        if clase_socio.is_valid():
            clase_socio.save()
            return redirect('/libro')
    else:
        clase_socio = clases_sociosfrom()
    return render(request, 'Libro/clase_socio.html',{'form': clase_socio})

def Home7(request):
    if request.method == 'POST':
        entrenador_activ = entrenador_tipoactividadfrom(request.POST)
        if entrenador_activ.is_valid():
            entrenador_activ.save()
            return redirect('/libro')
    else:
        entrenador_activ = entrenador_tipoactividadfrom()
    return render(request, 'Libro/entrenador_tipoactividad.html',{'form': entrenador_activ})
    

