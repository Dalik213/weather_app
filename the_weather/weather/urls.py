from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    
]

def lol():
    print("lol")