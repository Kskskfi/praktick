from django.urls import path
from .views import index, login, register, profile

app_name = 'main'

urlpatterns = [
    path('accounts/profile/', profile, name='profile'),
    path('login', login, name='login'),
    path('register', register, name='register'),
   path('', index, name='index')
]