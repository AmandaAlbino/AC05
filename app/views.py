from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

# pagina inicial
def home(request):
    return render(request,'home.html')

#Formulario para cadastro
def create(request):
    return render(request,'create.html')

#coleta de dados dos usuarios
def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
       data['msg']= 'Senha e confirmação de senha diferentes!'
       data['class']= 'alert-danger'
    else:
       user = User.objects.create_user(request.POST['name'], request.POST['email'], request.POST['password'])
       user.first_name = request.POST['name']
       user.save()
       data['msg']= 'Usuario cadastrado com sucesso!'
       data['class']= 'alert-sucess'

    return render(request,'create.html',data)

#Formulário do painel de login
def painel(request):
    return render(request,'painel.html')

#Processa o login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request,'painel.html',data)

#Página inicial do dashboard
def dashboard(request):
    return render(request,'dashboard/home.html')

#Logout do sistema
def logouts(request):
    logout(request)
    return redirect('/painel/')

#Alterar a senha
def changePassword(request):
    user = User.objects.get(email=request.user.email)
    user.set_password('123456')
    user.save()
    logout(request)
    return redirect('/painel/')

#Inserção dos dados dos usuários no banco
def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        user.user_permissions.add(27)
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request,'create.html',data)

def contato(request):
  form = ContatoForm(request.POST or None)
  if form.is_valid():
    contato = form.save()
    return render(request, 'contato_sucesso.html', {'contato': contato})
  return render(request, 'contato.html', {'form': form})