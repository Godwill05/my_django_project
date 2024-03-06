from django.urls import path
from . import views

app_name = 'bases'

urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.handle_404),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]