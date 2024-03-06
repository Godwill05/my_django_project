from django.urls import path
from . import views

app_name = "mangalib"

urlpatterns  = [
    path('',views.index, name='index'), 
    
    path('<int:book_id>/', views.show, name='show'),
    
    path('ajouter-livre/', views.add, name='add')
]