from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
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

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'Electronics/delete_product.html', {'product': product})

