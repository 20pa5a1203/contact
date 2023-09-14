from django.shortcuts import render,redirect
from django.urls import reverse
from .models import User_Master
from contacts.models import Contacts

# Create your views here.

def home(request):
    return render(request,'index.html')


# sign in 

def signin(request):
    if request.method == 'POST' :
        # request.sessions['mail']=''
        email = request.POST['email']
        password = request.POST['password']
        data = User_Master.objects.get(Email = email ).Email
        request.session['mail']=data
        contact = Contacts.objects.filter(Owner = data)
        return render(request,'contacts.html',{'contact':contact})
    else:
        return render(request,'index.html')


# display signup

def signup(request) :
    return render(request,'signup.html')

# signup 

def createuser(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        secret = request.POST['secret']
        ins = User_Master.objects.create(Email = email,Password = password,Secret = secret)
        ins.save()
        return redirect('signin')