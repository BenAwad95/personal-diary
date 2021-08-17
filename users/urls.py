from django.urls import path, include
from .views import index, register, index

app_name = 'users'
urlpatterns = [
    path('', index),
    path('account/', include('django.contrib.auth.urls')),
    path('register_new/', register, name='register')
]
