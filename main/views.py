from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from main.forms import ProductForm, CustomUserCreationForm
import datetime
import json

from main.models import Product

@login_required(login_url='/login')
def show_main(request):
    product_form = ProductForm() 
    context = {
        'npm' : '2406437571',
        'name': 'Cheryl Raynasya Adenan',
        'class': 'PBP A',
        'form': product_form, 
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)

def register_user_page(request):
    form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user_page(request):
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required
def show_json(request): 
    product_list = Product.objects.all().select_related('user')
    data = []
    
    for product in product_list:
        data.append({
            'pk': product.pk,
            'fields': {
                'user': product.user.username,
                'user_id': product.user_id, 
                'name': product.name,
                'amount': product.amount,
                'description': product.description,
                'date_added': product.date_added.isoformat() if product.date_added else None,
            }
        })
    
    return JsonResponse(data, safe=False)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        data = {
            'pk': product.pk,
            'fields': {
                'user': product.user.username,
                'user_id': product.user_id,
                'name': product.name,
                'amount': product.amount,
                'description': product.description,
                'date_added': product.date_added.isoformat() if product.date_added else None,
            }
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product not found'}, status=404)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_xml_by_id(request, product_id):
    product_item = Product.objects.filter(pk=product_id)
    if not product_item.exists():
        return HttpResponse(status=404)
    xml_data = serializers.serialize("xml", product_item)
    return HttpResponse(xml_data, content_type="application/xml")


def register_ajax(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Account created successfully!'}, status=201)
        else:
            errors = dict(form.errors.items())
            error_message = next(iter(errors.values()))[0] if errors else 'Registration failed'
            return JsonResponse({'status': 'error', 'message': error_message, 'errors': errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

def login_ajax(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            response = JsonResponse({'status': 'success', 'message': 'Login successful!', 'username': user.username}, status=200)
            
            # Tambahkan logika setting cookie di sini (sama seperti fungsi login lama)
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid username or password'}, status=401)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


def logout_ajax(request):
    logout(request)
    return JsonResponse({'status': 'success', 'message': 'Logout successful!'}, status=200)

@login_required
def create_product_ajax(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.user = request.user 
            new_product.save()
            
            return JsonResponse({"status": "ok", "message": "Product created successfully!"}, status=201)
        else:
            errors = dict(form.errors.items())
            return JsonResponse({"status": "error", "message": "Validation failed", "errors": errors}, status=400)
    
    return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)

def edit_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    
    if not request.user.is_authenticated or product.user != request.user:
        return JsonResponse({'status': 'error', 'message': 'Not authorized to edit this product'}, status=403)
        
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': f'Product "{product.name}" updated successfully.'}, status=200)
        else:
            errors = dict(form.errors.items())
            return JsonResponse({'status': 'error', 'message': 'Form validation failed', 'errors': errors}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

def delete_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    
    if not request.user.is_authenticated or product.user != request.user:
        return JsonResponse({'status': 'error', 'message': 'Not authorized to delete this product'}, status=403)
    
    if request.method == 'POST':
        product_name = product.name
        product.delete()
        return JsonResponse({'status': 'success', 'message': f'Product "{product_name}" deleted successfully.'}, status=200)
        
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)