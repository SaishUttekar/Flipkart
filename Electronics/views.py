from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm, CreateUserForm
from django.http import HttpResponseRedirect
from django. contrib. auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout as auth_logout


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user + ' Account was created for you!')
            return redirect('login')
        else:
            form = CreateUserForm()
        return render(request, 'Electronics/register.html', {'form': form})
    

def login_view(request):  # Renamed from loginpage to login_view
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'Electronics/login.html', context)
    
def logout_view(request):
    auth_logout(request)
    return redirect('login')
    
@login_required(login_url='login')
def home(request):
   
    prod = Product.objects.all()
    fm = ProductForm()
    if request.method == "POST":
        fm = ProductForm(request.POST, request.FILES)
    if fm.is_valid():
        fm.save()
        return redirect ("home")
    else:
        fm = ProductForm()
    return render(request, 'Electronics/home.html' , {'prod':prod,'fm':fm})

@login_required(login_url='login')
def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm(instance=product)
    return render(request, 'Electronics/edit_product.html', {'form': form})

@login_required(login_url='login')
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'Electronics/delete_product.html', {'product': product})

