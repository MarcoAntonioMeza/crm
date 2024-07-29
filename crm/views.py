from django.shortcuts import render, redirect
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
    

