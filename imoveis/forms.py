from django.forms import ModelForm, TextInput
from .models import Cliente, Imovel 

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

class ImovelForm(ModelForm):
    class Meta:
        model = Imovel
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class':'form-control'}),
            'valor': TextInput(attrs={'class':'form-control'}),
            'localizacao': TextInput(attrs={'class':'form-control'}),
            'cidade': TextInput(attrs={'class':'form-control'})
        }
