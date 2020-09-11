from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ships
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


def index(request):
    dest = ships.objects.all()
    return render(request,'museum/index.html',{'dest':dest})

def about(request):
    dest = ships.objects.all()
    return render(request,'museum/about.html',{'dest':dest})
    
def shi(request):
    data = ships.objects.all()
    return render(request,'museum/ship.html',{'data':data})

def info(request):
    return render(request,'museum/info.html')

def add(request):
    val1 = request.POST['num']
    return render(request,'museum/info.html',{'result':val1})

def myfun(request):
    val2 = request.POST['var']
    #print(val2)
    query_result=ships.objects.get(ship_name=val2)
    #query_result=ships.objects.filter(ship_name='var')
    #query_result=ships.objects.filter(Q(ship_name="var"))
    #val2=ships.objects.all()

    #instead of returning value here i want to return the data belongong to the ship
    return render(request,'museum/info.html',{'result':query_result})


def ship_data(request):
    val=request.POST['var12']
    return render(request,'museum/select_ship.html',{'ship_seleted':val})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("index")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "museum/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "museum/register.html",
                  context={"form":form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "museum/login_request.html",
                    context={"form":form})
def logout_request(request):
     logout(request)
     messages.info(request, "Logged out successfully!")
     return redirect("museum:index")
     #return render(request,'museum/index.html')

def photos_gallery(request):
    return render(request,'museum/photos_gallery.html')

