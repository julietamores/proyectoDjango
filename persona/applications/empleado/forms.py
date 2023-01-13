from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Empleado
        fields = (
            'apellidos',
            'nombres',
            'nombre_completo',
            'dni',
            'area',
            'habilidades', 
            'avatar', 
        )
        widgets = {
            'habilidades':forms.CheckboxSelectMultiple() 
        }

