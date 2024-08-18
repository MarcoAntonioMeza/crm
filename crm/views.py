from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from  .models import Cliente

from .forms import ClienteForm
# Create your views here.

"""
==================================================================
                    CRUD CLIENTES
===================================================================
"""
def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        
        if form.is_valid():
            cliente = form.save(user=request.user)  # Pasa el usuario autenticado
            return redirect('success_url')  # Reemplaza 'success_# Reemplaza 'success_url' con tu URL de éxito
    else:
        form = ClienteForm()
    return render(request, 'crm/clientes/index.html', {'form': form})
    

def cliente_create_or_update(request, cliente_id=None):
    if cliente_id:
        cliente = get_object_or_404(Cliente, id=cliente_id)
    else:
        cliente = None
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        
        if form.is_valid():
            cliente = form.save(user=request.user)  # Pasa el usuario autenticado
            return redirect('success_url')  # Reemplaza 'success_url' con tu URL de éxito
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'crm/clientes/index.html', {'form': form})