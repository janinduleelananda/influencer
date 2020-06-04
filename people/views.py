from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from accounts.models import Profile,Pictures


# Create your views here.
def home(request):
    return render(request,'people/home.html')

def people(request):
    users = User.objects.all()
    return render(request,'people/people_list.html',{'users':users})
def detail(request,username):
    user=get_object_or_404(User,username=username)
    pictures = Pictures.objects
    return render(request,'people/showprofile.html',{'pictures': pictures,'user':user})

