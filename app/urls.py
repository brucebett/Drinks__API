from django.urls import path
from app import views

urlpatterns = [
    path('drinks/', views.drink_list),
    path('drinks/<int:id>', views.drink_detail)
    
]
