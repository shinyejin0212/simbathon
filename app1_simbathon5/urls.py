from django.urls import path,include
from .views import *
from app1_simbathon5 import views
app_name = "app1_simbathon5"
urlpatterns = [
    path('', main, name= "main"),
    path('FAQ/', frequentlyaskedquestions , name= "frequentlyaskedquestions"),
    path('<str:id>', views.detail, name="detail"),
    path('book/', book,name="book"),
 
]