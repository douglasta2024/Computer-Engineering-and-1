from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.hi, name='home-page'),
    path('register/', views.registerPage, name='register'),
    path('', views.loginPage, name='loginpage'),
    path('survey/', views.surveyPage, name='survey'),
    path('physicalhome/', views.physicalPage, name='physical-page'),
    path('physicalgraph/', views.graphPage, name='graph-page'),
]