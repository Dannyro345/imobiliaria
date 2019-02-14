from django.forms import ModelForm, TextInput
from .models import Cliente 

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'cpf': TextInput(attrs={'class':'form-control'}),
            'nome': TextInput(attrs={'class':'form-control'}),
            'dt_nasc': TextInput(attrs={'class':'form-control'}),
            'sexo': TextInput(attrs={'class':'form-control'})
        }
