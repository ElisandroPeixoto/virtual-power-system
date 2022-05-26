from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CustomUsuario
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('password')
        login_usuario = authenticate(email=email, password=senha)

        if login_usuario:
            django_login(request, login_usuario)
            return redirect('inicio')
        else:
            return HttpResponse('Dados Invalidos')


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('password')
        nome = request.POST.get('name')
        sobrenome = request.POST.get('surname')
        pais = request.POST.get('country')
        estado = request.POST.get('state')
        cidade = request.POST.get('city')

        novo_usuario = CustomUsuario.objects.filter(username=email).first()
        if novo_usuario:
            return HttpResponse('E-mail já cadastrado')

        novo_usuario = CustomUsuario.objects.create_user(
            email=email,
            password=senha,
            first_name=nome,
            last_name=sobrenome,
            pais=pais,
            estado=estado,
            cidade=cidade
        )
        novo_usuario.save()
        return redirect('inicio')
