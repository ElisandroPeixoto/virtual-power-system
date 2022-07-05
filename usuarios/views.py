from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import AlterarCustomUsuario
from .models import CustomUsuario


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

        # Verificação de Dados Cadastrais
        novo_usuario = CustomUsuario.objects.filter(username=email).first()
        dados_pessoais = [email, nome, sobrenome, pais, estado, cidade]
        for dados in dados_pessoais:
            if senha1 == dados:
                senha_facil = True
            else:
                senha_facil = False

        if email.find('@') == -1:  # Se o e-mail inserido não tiver um '@'
            email_invalido = {
                'email_invalido': True
            }
            return render(request, 'cadastro.html', email_invalido)

        elif novo_usuario:
            existe_email = {
                'existe_email': True  # E-mail já existe
            }
            return render(request, 'cadastro.html', existe_email)

        elif senha_facil:
            senhafacil = {
                'senhafacil': True  # Senha igual a algum dado pessoal
            }
            return render(request, 'cadastro.html', senhafacil)

        elif senha1.isnumeric():
            senha_numerica = {
                'senha_numerica': True  # Senha contém apenas números
            }
            return render(request, 'cadastro.html', senha_numerica)

        elif len(senha1) < 8:
            senha_curta = {
                'senha_curta': True  # Senha muito curta
            }
            return render(request, 'cadastro.html', senha_curta)

        elif senha1 != senha2:
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


def gerenciar_perfil(request):
    if request.method == "GET":
        return render(request, 'gerenciar_perfil.html')
    else:
        # Alteração de Dados
        alterar_usuario = AlterarCustomUsuario(request.POST, instance=request.user)
        if alterar_usuario.is_valid():
            alterar_usuario.save()
            return render(request, 'perfil.html')


def logout(request):
    django_logout(request)
    return render(request, 'inicio.html')


def alterar_senha(request):
    if request.method == "GET":
        return render(request, 'alterar_senha.html')
    else:
        # Alteração de Senha
        nova_senha = PasswordChangeForm(data=request.POST, user=request.user)
        if nova_senha.is_valid():
            nova_senha.save()
            update_session_auth_hash(request, nova_senha.user)
            alterado_sucesso = {
                'alterado_sucesso': True
            }
            return render(request, 'alterar_senha.html', alterado_sucesso)
        else:
            falha_alteracao = {
                'falha_alteracao': True
            }
            return render(request, 'alterar_senha.html', falha_alteracao)


@login_required()
def selecao_simulacao(request):
    return render(request, 'menu_simu.html')
