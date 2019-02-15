from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Cliente, Imovel
from . forms import ClienteForm, ImovelForm

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

def imovel_form(request):
    if (request.method == 'POST'):
        form = ImovelForm(request.POST)
        form.save()
        return redirect('/imoveis/imovel/')     

    else:
        form = ImovelForm()
        return render(request, 'imovel/form.html', {'form':form})

def imovel_edit(request, imovel_id):
    if (request.method == 'POST'):
        imovel = Imovel.objects.get(pk=imovel_id)
        form = ImovelForm(request.POST, instance=imovel)
        if (form.is_valid()):
            form.save()
            return redirect('/imoveis/imovel/')
        else:
            return render(request, 'imovel/edit.html', {'form':form, 'imovel_id':imovel_id})   
    else:
        imovel = Imovel.objects.get(pk=imovel_id)
        form = ImovelForm(instance=imovel)       
        return render(request, 'imovel/edit.html', {'form':form, 'imovel_id':imovel_id})
