from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from .models import Pictures
from django.utils import timezone
from django.contrib.auth.decorators import login_required
def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html',{'error':'Username already exists'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'],email=request.POST['email'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
    else:
         return render(request,'accounts/signup.html')

def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error':'username or password is invalid'})
    else:
        return render(request,'accounts/login.html')


def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')
def profile(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'your account has been updated!')
            return redirect('profile_view')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'accounts/profile.html',context)

def profile_view(request):
    pictures = Pictures.objects
    user1 = request.user
    return render(request, 'accounts/profile_view.html', {'pictures': pictures, 'user1': user1})

@login_required(login_url="/accounts/signup/")
def create(request):
    if request.method=='POST':
        if request.FILES['image'] and request.POST['caption']:
            picture=Pictures()
            picture.image=request.FILES['image']
            picture.caption=request.POST['caption']
            picture.pub_date=timezone.datetime.now()
            picture.owner=request.user
            picture.save()
            return redirect('profile_view')


def delete_picture(request,picture_id):
    if request.method == 'POST':
        picture = get_object_or_404(Pictures, pk=picture_id)
        picture.delete()
        return redirect('profile_view')



