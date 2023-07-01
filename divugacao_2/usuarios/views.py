from django.shortcuts import render, redirect
from django.contrib import messages
from.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def novo_usuario(request):
    #tipo da requisacao
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)
        #validar as informaçoes
        if formulario.is_valid():
            #salvar as informaçoes
            formulario.save()
            #pegando o usuario
            usuario = formulario.cleaned_data.get('username')
            # informar ao usuario
            messages.success(request,f'O usuario {usuario} foi cadastrado com sucesso !')
            return redirect('login')
            
    else:
        formulario = UserRegisterForm()
        
    return render(request, 'usuarios/registrar.html', {'formulario':formulario})