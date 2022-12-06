from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Post
from .utils import get_plot

# Create your views here.S
from .forms import CreateUserForm
from .forms import UploadForm
def hi(request):
    return render(request, 'LifeStyleApp/hi.html')
def registerPage(request):
    # Creating the form that was imported
    form = CreateUserForm()

    # Method to check if the account was created and if it was then go to the back to the login page
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('loginpage')

    # Whenever the register page is called it needs to take the user to the register.html file
    context = {'form':form}
    return render(request, 'accounts/register.html', context)
def loginPage(request):
    # Retrieves the data that was posted from the form
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Checks if the authentication is correct by passing in the username and password
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home-page')
    context = {}

    # Whenever the login page is called it needs to take the user to the login.html file
    return render(request, 'accounts/loginpage.html', context)

def surveyPage(request):
    # Whenever the survey page is called it needs to take the user to the survey.html file
    return render(request, 'LifeStyleApp/survey.html')

def physicalPage(request):
    # Takes the inputs of the form from POST which is published and the values from the physical page are used to make the graph
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('graph-page')
    return render(request, 'LifeStyleApp/physicalDataInput.html', {'form' : UploadForm}) #

def graphPage(request):
    # Does the average calculation and does the graph calculation by the objects in the model from the admin django page
    post_data_list = Post.objects.all()
    avg = 0
    num = 0
    for post in post_data_list:
        avg = avg + post.miles
        num = num + 1
    avg = avg / num
    x = [x.days for x in post_data_list]
    y = [y.miles for y in post_data_list]
    chart = get_plot(x, y)

    # Goes to the graph.html file whenever the def graphPage is called
    return render(request, 'LifeStyleApp/Graph.html', {'post_data_list':post_data_list, 'chart':chart, 'avg' : avg} )