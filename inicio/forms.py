from django import forms 


class BasePaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)
    anio = forms.IntegerField()

class CrearPaletaFormulario(BasePaletaFormulario): #herencia
    ...
    
class ActualizarPaletaFormulario(BasePaletaFormulario): #herencia
    ...
    
# class BsuquedaPaletaFormulario(forms.Form):  #ver after class anterior a la clase 22
#     marca = forms.CharField(max_length=30, required=False)