from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Cliente, Imovel
from . forms import ClienteForm

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/list.html', {'clientes':clientes})

def cliente_show(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    return render(request, 'cliente/show.html', {'cliente':cliente})     

def cliente_form(request):
    if (request.method == 'POST'):
        form = ClienteForm(request.POST)
        form.save()
        return redirect('/imoveis/cliente/')     

    else:
        form = ClienteForm()
        return render(request, 'cliente/form.html', {'form':form})

def cliente_edit(request, cliente_id):
    if (request.method == 'POST'):
        cliente = Cliente.objects.get(pk=cliente_id)
        form = ClienteForm(request.POST, instance=cliente)
        if (form.is_valid()):
            form.save()
            return redirect('/imoveis/cliente/')
        else:
            return render(request, 'cliente/edit.html', {'form':form, 'cliente_id':cliente_id})   
    else:
        cliente = Cliente.objects.get(pk=cliente_id)
        form = ClienteForm(instance=cliente)       
        return render(request, 'cliente/edit.html', {'form':form, 'cliente_id':cliente_id})

def imovel_list(request):
    imoveis = Imovel.objects.all()
    return render(request, 'imovel/list.html', {'imoveis':imoveis})

def imovel_show(request, imovel_id):
    imovel = Imovel.objects.get(pk=imovel_id)
    return render(request, 'imovel/show.html', {'imovel':imovel}) 