from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request,'index.html',{
        'message': 'Listado de productos',
        'title':'D´Mare',
        'products':[
            {'title':'playera','price':5,'stock':True},
            {'title':'playera2','price':15,'stock':True},
            {'title':'playera3','price':20,'stock':False}
        ]
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        
        else:
            messages.error(request, 'Usuario o contraseña no validos')
            


    return render(request, 'users/login.html',{

    })

def logout_view(request):
    logout(request)
    messages.success(request, 'sesión cerrada exitosamente')
    return redirect('login')