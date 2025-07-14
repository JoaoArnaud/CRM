from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as lg
# Create your views here.

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email).first()

        if user:
            return HttpResponse('Já existe um usuárico com esse e-mail!')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.saver()

        return HttpResponse('Usuário cadastrado com sucesso!')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
         email = request.POST.get('email')
         password = request.POST.get('password')

         user = authenticate(email=email, password=password)

         if user:
             lg(request, user)
             return HttpResponse('Autenticado')
         else:
             return HttpResponse('Email ou senha invalidos')
        
# na hora de crar o CRM eu crio um: if request.user.is_authenticated: return CRM else: vc precisa logar
#decorar a função da pagina com @login_required(login_url='/auth/login/')