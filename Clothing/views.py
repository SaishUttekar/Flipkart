from django.shortcuts import render, redirect
from .models import CloProduct
from .forms import ProductForm

# Create your views here.
def home(request):
   
    prod = CloProduct.objects.all()
    fm = ProductForm()
    if request.method == "POST":
        fm = ProductForm(request.POST, request.FILES)
    if fm.is_valid():
        fm.save()
        return redirect ("home")
    else:
        fm = ProductForm()
    return render(request, 'Clothing/home.html' , {'prod':prod,'fm':fm})

def edit_product(request, product_id):
    product = CloProduct.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm(instance=product)
    return render(request, 'Clothing/edit_product.html', {'form': form})

def delete_product(request, product_id):
    product = CloProduct.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('Clothing:home')  # Use the Clothing namespace
    return render(request, 'Clothing/delete_product.html', {'product': product})

