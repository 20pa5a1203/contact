from django.shortcuts import render,redirect
from .models import Contacts
from user.models import User_Master

# Create your views here.

def save_info(request):
    if request.method == 'POST' :
        email = request.POST['email']
        phone = request.POST['phone']
        name = request.POST['name']
        # data = User_Master.objects.get(Email = email ).Email
        mail = request.session['mail']
        contact = Contacts.objects.filter(Owner = mail)
        data = Contacts.objects.create(Name=name,Phone=phone,Email=email,Owner=mail)
        data.save()
        return render(request,'contacts.html',{'contact':contact})
