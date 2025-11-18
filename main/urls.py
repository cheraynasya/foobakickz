from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('create-product/', views.create_product, name='create_product'), # Traditional Create
    path('product/<str:id>/', views.show_product, name='show_product'), # Traditional Detail
    
    # --- CRUD AJAX ENDPOINTS ---
    path('json/', views.show_json, name='show_json'), # READ ALL AJAX
    path('json/<int:product_id>/', views.show_json_by_id, name='show_json_by_id'), # READ BY ID AJAX
    
    path('create-ajax/', views.add_product_entry_ajax, name='add_product_entry_ajax'), # CREATE AJAX
    path('edit-ajax/<int:product_id>/', views.edit_product_entry_ajax, name='edit_product_entry_ajax'), # UPDATE AJAX
    path('delete-ajax/<int:product_id>/', views.delete_product_entry_ajax, name='delete_product_entry_ajax'), # DELETE AJAX

    # --- Autentikasi ---
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]