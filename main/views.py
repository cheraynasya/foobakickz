import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import datetime
import requests

from main.forms import ProductForm
from main.models import Product

@login_required(login_url='/login')
def show_main(request):
    context = {
        'npm' : '2406437571',
        'name': 'Cheryl Raynasya Adenan',
        'class': 'PBP A',
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'user': request.user,
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
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()
    context = {'product': product}
    return render(request, "product_detail.html", context)

@login_required
def my_products(request):
    products = Product.objects.filter(user=request.user)
    return render(request, "my_products.html", {"products":products})

@login_required(login_url='/login')
def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

# @login_required(login_url='/login')
def show_json(request):
    # 1. Terapkan batasan (limit) 20 produk dan urutkan berdasarkan ID/waktu terbaru
    # Mengasumsikan ID yang lebih besar adalah produk yang lebih baru
    product_list = Product.objects.select_related('user').all().order_by('-id')[:20] 
    
    # Jika Anda menggunakan field DateTimeField bernama 'created_at', lebih baik gunakan:
    # product_list = Product.objects.select_related('user').order_by('-created_at')[:20]
    
    data = [
        {
            'id': str(p.id),
            'user_id': p.user_id,
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'thumbnail': p.thumbnail,
            'category': p.category,
            'is_featured': p.is_featured,
            'stock': p.stock,
            'views': p.views,
            'created_at': p.created_at.isoformat() if p.created_at else None,
            'user_username': p.user.username,
        }
        for p in product_list
    ]
    # Mengembalikan data yang sudah dibatasi
    return JsonResponse(data, safe=False)

@login_required(login_url='/login')
def show_xml_by_id(request, product_id):
        product_item = Product.objects.filter(pk=product_id)
        if not product_item.exists():
            return HttpResponse(status=404)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")

# @login_required(login_url='/login')
# def show_json_user(request, product_id):
#     try:
#         product = Product.objects.select_related('user').get(pk=product_id)
#         data = {
#             'id': str(product.id),
#             'user_id': product.user_id,
#             'name': product.name,
#             'price': product.price,
#             'description': product.description,
#             'thumbnail': product.thumbnail,
#             'category': product.category,
#             'is_featured': product.is_featured,
#             'stock': product.stock,
#             'views': product.views,
#             'created_at': product.created_at.isoformat() if product.created_at else None,
#             'user_username': product.user.username if product.user_id else 'Anonymous',
#         }
#         return JsonResponse(data)
#     except Product.DoesNotExist:
#         return JsonResponse({'detail': 'Not found'}, status=404)
@login_required(login_url='/login')
def show_json_user(request):
    """
    Menampilkan HANYA produk yang terasosiasi dengan user yang sedang login.
    Membutuhkan user terotentikasi.
    """
    # 1. Filter produk: Hanya ambil objek yang field 'user' nya sama dengan request.user
    product_list = Product.objects.filter(user=request.user).select_related('user').all().order_by('-id')
    
    # 2. Serialize data menggunakan fungsi helper (diasumsikan _serialize_product sudah didefinisikan)
    data = [_serialize_product(p) for p in product_list]
    
    # 3. Kembalikan data dalam format JSON
    return JsonResponse(data, safe=False)   

def _serialize_product(p):
    """Fungsi helper untuk membuat dictionary produk yang konsisten sesuai model Flutter"""
    return {
        # Menggunakan str(p.id) karena di model Flutter Anda 'id' adalah String
        'id': str(p.id),
        'user_id': p.user_id,
        'name': p.name,
        'price': p.price,
        'description': p.description,
        'thumbnail': p.thumbnail,
        'category': p.category,
        'is_featured': p.is_featured,
        'stock': p.stock,
        'views': p.views,
        # Pastikan p.created_at adalah DateTimeField yang valid
        'created_at': p.created_at.isoformat() if p.created_at else None, 
        # Menggunakan p.user.username yang diambil dari relasi
        'user_username': p.user.username if p.user_id else 'Anonymous', 
    }

@login_required
@require_POST
@csrf_exempt
def add_product_entry_ajax(request):
    if request.method == 'POST':
        # Asumsi Anda menggunakan model form
        # Ganti ProductForm dengan nama Form yang sebenarnya
        from .forms import ProductForm 
        
        form = ProductForm(request.POST or None) 
        
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.user = request.user # Pastikan request.user adalah user yang benar
            new_product.save()
            
            # Sukses: Beri status 201 (Created)
            return HttpResponse(b"CREATED", status=201) 
        else:
            # Gagal Validasi: Beri status 400 (Bad Request) dan kirim error dalam JSON
            errors = dict(form.errors.items())
            print("!!! VALIDATION ERRORS (400) !!!")
            print(errors)
            
            return HttpResponseBadRequest(
                json.dumps(errors), 
                content_type="application/json"
            )
            
    # Jika method bukan POST
    return HttpResponse(b"Method Not Allowed", status=405)

# 4. UPDATE AJAX
@csrf_exempt
@login_required
@require_POST
def edit_product_entry_ajax(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    # Verifikasi kepemilikan
    if product.user != request.user:
        return HttpResponse("Unauthorized: You do not own this product.", status=403)
        
    # Sanitasi data sebelum disimpan
    product.name = strip_tags(request.POST.get("name"))
    product.description = strip_tags(request.POST.get("description"))
    
    try:
        product.price = int(request.POST.get("price", product.price))
        product.stock = int(request.POST.get("stock", product.stock))
    except (TypeError, ValueError):
        return HttpResponse("Invalid price or stock value", status=400)
    
    product.thumbnail = request.POST.get("thumbnail")
    product.category = request.POST.get("category")
    product.is_featured = request.POST.get("is_featured") == 'on'
    
    product.save()

    return HttpResponse(b"UPDATED", status=200)

# 5. DELETE AJAX
@csrf_exempt
@login_required
@require_POST
def delete_product_entry_ajax(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    # Verifikasi kepemilikan
    if product.user != request.user:
        return HttpResponse("Unauthorized: You do not own this product.", status=403)

    product.delete()
    return HttpResponse(b"DELETED", status=200)

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)