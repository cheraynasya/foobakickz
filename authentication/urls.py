from django.urls import path
from authentication.views import login, register, logout, get_user_info

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('get_user_info/', get_user_info, name='get_user_info'),
]