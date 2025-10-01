from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('create-product/', views.create_product, name='create_product'),
    path('product/<int:id>/', views.show_product, name='show_product'),
    path('product/<int:id>/edit/', views.edit_product, name='edit_product'),
    path('product/<int:id>/delete/', views.delete_product, name='delete_product'),

    path("my-products/", views.my_products, name="my_products"),


    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<int:product_id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:product_id>/', views.show_json_by_id, name='show_json_by_id'),
]