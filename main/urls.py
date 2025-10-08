from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('register/', views.register_user_page, name='register'),
    path('login/', views.login_user_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    path('json/', views.show_json, name='show_json'),
    path('json/<int:product_id>/', views.show_json_by_id, name='show_json_by_id'),
    path('xml/', views.show_xml, name='show_xml'),
    path('xml/<int:product_id>/', views.show_xml_by_id, name='show_xml_by_id'),
    
    path('register/ajax/', views.register_ajax, name='register_ajax'),
    path('login/ajax/', views.login_ajax, name='login_ajax'),
    path('logout/ajax/', views.logout_ajax, name='logout_ajax'),
    
    path('create-product-ajax/', views.create_product_ajax, name='create_product_ajax'),
    path('edit-product-ajax/<int:id>/', views.edit_product_ajax, name='edit_product_ajax'),
    path('delete-product-ajax/<int:id>/', views.delete_product_ajax, name='delete_product_ajax'),
]