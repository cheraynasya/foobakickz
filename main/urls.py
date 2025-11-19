from django.urls import path
from main.views import proxy_image, show_json, show_json_user
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('create-product/', views.create_product, name='create_product'), # Traditional Create
    path('product/<str:id>/', views.show_product, name='show_product'), # Traditional Detail
    
    # --- CRUD AJAX ENDPOINTS ---
    path('json/', show_json, name='show_json'),
    path('json/user/', show_json_user, name='show_json_user'),

    path('create-ajax/', views.add_product_entry_ajax, name='add_product_entry_ajax'), # CREATE AJAX
    path('edit-ajax/<int:product_id>/', views.edit_product_entry_ajax, name='edit_product_entry_ajax'), # UPDATE AJAX
    path('delete-ajax/<int:product_id>/', views.delete_product_entry_ajax, name='delete_product_entry_ajax'), # DELETE AJAX

    # --- Autentikasi ---
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('proxy-image/', proxy_image, name='proxy_image'),
]