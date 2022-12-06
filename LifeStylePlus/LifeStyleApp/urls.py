from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.hi, name='home-page'),
    path('register/', views.registerPage, name='register'),
    path('', views.loginPage, name='loginpage'), #Pathway to login page
    path('survey/', views.surveyPage, name='survey'), #Pathway to the mental health survey page
    path('physicalhome/', views.physicalPage, name='physical-page'), #Pathway to the data input page
    path('physicalgraph/', views.graphPage, name='graph-page'), #Pathway to the graph page
]