from django import forms
from models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'cpf', 'genero', 'telefone', 'idade', 'cidade', 'estado' ]
        widgets = {
            'nome' : forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'cpf' : forms.TextInput(attrs={'class':'form-control'}),
            'telefone': forms.TextInput(attrs={'class':'form-control'}),
            'idade' : forms.TextInput(attrs={'class':'form-control'}),
            'cidade' : forms.TextInput(attrs={'class':'form-control'}),
            'genero' : forms.Select(attrs={'class':'form-control'}),
            'estado' : forms.Select(attrs={'class':'form-control'}),
        }
