from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import CustomUsuario
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from .forms import AlterarCustomUsuario
from django.http import HttpResponse


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('password')
        login_usuario = authenticate(email=email, password=senha)

        if not login_usuario:  # Se e-mail e senha são dados cadastrados
            falha_login = {
                'dados_invalidos': True  # Detecta que os dádos inseridos são inválidos
            }
            return render(request, 'login.html', falha_login)
        else:
            django_login(request, login_usuario)  # Autenticação do usuario
            return redirect('inicio')


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        email = request.POST.get('email')
        senha1 = request.POST.get('password')
        senha2 = request.POST.get('confirm-password')
        nome = request.POST.get('name').capitalize()
        sobrenome = request.POST.get('surname').capitalize()
        pais = request.POST.get('country').capitalize()
        estado = request.POST.get('state').capitalize()
        cidade = request.POST.get('city').capitalize()

        dados_usuario = [email, senha1, senha2, nome, sobrenome, pais, estado, cidade]

        # Verificação de Dados Cadastrais
        for dados in dados_usuario:
            if dados == '':
                campos_vazios = {
                    'campos_vazios': True
                }
                return render(request, 'cadastro.html', campos_vazios)

        novo_usuario = CustomUsuario.objects.filter(username=email).first()
        if email.find('@') == -1:  # Se o e-mail inserido não tiver um '@'
            email_invalido = {
                'email_invalido': True
            }
            return render(request, 'cadastro.html', email_invalido)

        elif novo_usuario:  # Verifica se o e-mail já foi cadastrado
            existe_email = {
                'existe_email': True  # E-mail já existe
            }
            return render(request, 'cadastro.html', existe_email)

        elif senha1 != senha2:  # Verifica se as senhas foram digitadas corretamente
            senhas_diferentes = {
                'senhas_diferentes': True  # Senhas não conferem entre si
            }
            return render(request, 'cadastro.html', senhas_diferentes)

        else:
            # Efetua cadastro do usuário
            novo_usuario = CustomUsuario.objects.create_user(
                email=email,
                password=senha1,
                first_name=nome,
                last_name=sobrenome,
                pais=pais,
                estado=estado,
                cidade=cidade
            )
            novo_usuario.save()
            cadastro_efetuado = {
                'cadastro_efetuado': True
            }
            return render(request, 'cadastro.html', cadastro_efetuado)


@login_required
def perfil(request):
    if request.method == "GET":
        return render(request, 'perfil.html')


def logout(request):
    django_logout(request)
    return render(request, 'inicio.html')


def gerenciar_perfil(request):
    if request.method == "GET":
        return render(request, 'gerenciar_perfil.html')
    else:
        alterar_usuario = AlterarCustomUsuario(request.POST, instance=request.user)

        if alterar_usuario.is_valid():
            alterar_usuario.save()
            return render(request, 'perfil.html')
        else:
            return HttpResponse('Erro')
