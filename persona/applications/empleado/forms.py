from django import forms
from .models import Empleado
from django.contrib.auth import authenticate



class LoginForm(forms.Form):
    username = forms.CharField(
        label='username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'username',
            }
        )
    )
    password = forms.CharField(
        label='Contrasenia',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'contrasenia'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')
        
        return self.cleaned_data

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

