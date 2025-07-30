from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as lg, logout as lt

from team.models import Team

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
        user.save()

        team = Team.objects.create(name='Nome do time', created_by=request.user)
        team.members.add(request.user)
        team.save()

        return redirect('crmanager:home') 

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')

        # 1. Tentar encontrar o usuário pelo e-mail
        user_obj = User.objects.filter(email=email).first()

        if user_obj:
            # 2. Se o usuário for encontrado pelo e-mail, tentar autenticar usando o username e a senha
            user = authenticate(request, username=user_obj.username, password=password)
            
            if user:
                lg(request, user)
                return redirect('crmanager:home') 
            else:
                # Se o usuário existe mas a senha está incorreta
                return HttpResponse('Email ou senha invalidos')
        else:
            # Se nenhum usuário foi encontrado com o e-mail fornecido
            return HttpResponse('Email ou senha invalidos')
        
def logout(request):
    lt(request)
    return redirect('login')
