from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi, name='home-page'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='loginpage'),
    path('survey/', views.surveyPage, name='survey')
]