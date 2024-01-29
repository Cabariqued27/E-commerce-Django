from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.models import User
from django.contrib import messages
from .forms import SignUpForm
from products.models import Product



def index(request):
    products = Product.objects.all().order_by('-id')
    return render(request,'index.html',{
        'message': 'Listado de productos',
        'title':'D´Mare',
        'products':products
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

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

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = SignUpForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        user = form.save()# with this def create a user
        if user:
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')
    
    return render(request, 'users/singup.html',{
        'form':form
    })