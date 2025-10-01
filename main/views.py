from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime

from main.forms import ProductForm
from main.models import Product

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "my":
        product_list = Product.objects.filter(user=request.user)
    else:
        product_list = Product.objects.all()

    context = {
        'npm' : '2406437571',
        'name': 'Cheryl Raynasya Adenan',
        'class': 'PBP A',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        messages.success(request, "Product berhasil dibuat.")
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)

    if product.user != request.user:
        messages.error(request, "Kamu tidak berhak mengedit produk ini.")
        return redirect('main:show_main')

    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == "POST":
        form.save()
        messages.success(request, "Product berhasil diupdate.")
        return redirect('main:show_product', id=product.id)

    context = {'form': form, 'product': product}
    return render(request, "edit_product.html", context)

@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)

    if product.user != request.user:
        messages.error(request, "Kamu tidak berhak menghapus produk ini.")
        return redirect('main:show_main')

    if request.method == "POST":
        product.delete()
        messages.success(request, "Product berhasil dihapus.")
        return redirect('main:show_main')

    return render(request, "confirm_delete.html", {"product": product})

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()
    context = {'product': product}
    return render(request, "product_detail.html", context)

@login_required(login_url='/login')
def my_products(request):
    products = Product.objects.filter(user=request.user)
    return render(request, "my_products.html", {"products":products})

@login_required(login_url='/login')
def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

@login_required(login_url='/login')
def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

@login_required(login_url='/login')
def show_xml_by_id(request, product_id):
        product_item = Product.objects.filter(pk=product_id)
        if not product_item.exists():
            return HttpResponse(status=404)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")

@login_required(login_url='/login')
def show_json_by_id(request, product_id):
        product_item = Product.objects.filter(pk=product_id)
        if not product_item.exists():
            return HttpResponse(status=404)
        json_data = serializers.serialize("json", product_item)
        return HttpResponse(json_data, content_type="application/json")
