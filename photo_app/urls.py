from django.contrib import admin
from django.urls import path
from .views import default, welcome, register, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', default, name='default'),
    path('welcome', welcome, name='welcome'),
    path('login', login, name='login'),
    path('register', register, name='register'),
]
