from django.urls import path
from . import views

app_name = "bibliotheque"

urlpatterns = [
    path('', views.index, name='index'),
    path('bibliotheque', views.bibliotheque, name='bibliotheque'),
    path('<int:id>/', views.livre, name='livre'),
]