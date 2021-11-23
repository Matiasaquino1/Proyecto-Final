from django import forms

from .models import Socios, clases_socios, entrenador, aparatos, clases, actividad, entrenador_tipoactividad,  salas

class Sociosfrom(forms.ModelForm):
    
    class Meta:
        model = Socios
        fields = ['nombre','apellido','telefono','profesion','CBU','direcciòn',]

class Entrenadorfrom(forms.ModelForm):

    class Meta:
        model = entrenador
        fields = ['nombre','telefono','experiencia','titulacion','Codigo_clase',]

class Aparatosfrom(forms.ModelForm):
    
    class Meta:
        model = aparatos
        fields = ['estado','descripcion',]

class Clasesfrom(forms.ModelForm):
    
    class Meta:
        model = clases
        fields = ['dia','hora',]

class Actividadfrom(forms.ModelForm):
    
    class Meta:
        meta = actividad
        fields = ['descripcion',]

class Salasfrom(forms.ModelForm):
    
    class meta:
        model = salas
        fields = ['metros','tipo','ubicacion','Codigo_clas','codigoA',]

class clases_sociosfrom(forms.ModelForm):
    
    class Meta:
        meta = clases_socios
        fields = ['codigo_clas','dni_socio','descripcion',]

class entrenador_tipoactividadfrom(forms.ModelForm):
    
    class Meta:
        meta = entrenador_tipoactividad
        fields = ['dni_e','id_actividad','descripcion',]