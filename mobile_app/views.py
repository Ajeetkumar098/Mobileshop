from django.shortcuts import render,redirect
from .models import phone,Service,profileimage,Apple,Types
from.forms import profileimageform,contact_us_form,phone_form,Apple_form
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash



# Create your views here.

def index(request):
    return render(request,'index.html') 

@login_required(login_url='login')
def home(request):
    data= phone.objects.all()
    return render(request,'home.html',{'data':data})

@login_required(login_url='login')
def service_fil(request,service1):
    s = Service.objects.filter(service=service1)
    for i in s:
        data = phone.objects.filter(service=i.id)

        return render(request,'show.html',{'data':data,'s':s})


@login_required(login_url='login')
def types_fil(request,types1):
    s = Types.objects.filter(types=types1)
    for i in s:
        data = Apple.objects.filter(types=i.id)

        return render(request,'show_two.html',{'data':data,'s':s})


def register(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']

        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,"user already exists")
                return redirect('login')
            
            elif User.objects.filter(email=email).exists():
                messages.error(request,"email already exists")
                return redirect('login')
            
            else:
                data = User.objects.create_user(username=username,email=email,password=password)
                return redirect('login')
            
        else:
            messages.error(request,"password does not match")
            return redirect('login')
    
    return render(request,'register.html')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        User = authenticate(username=username,password=password)

        if User is None:
            messages.error(request,"username/password does not match")
            return redirect('register')
        
        else:
            auth.login(request,User)
            return redirect('home')
        
    return render(request,'login.html')

def logout(request):
    # import os
    # os.system("poweroff")
    auth.logout(request)
    return redirect('index')

@login_required(login_url='login')
def readmore(request,id):
    data = phone.objects.get(id=id)
    return render(request,'readmore.html',{'data':data})

@login_required(login_url='login')
def show(request):
    data = phone.objects.all()
    return render(request,'show.html',{'data':data})


@login_required(login_url='login')
def readmore_two(request,id):
    data = Apple.objects.get(id=id)
    return render(request,'readmore_two.html',{'data':data})

@login_required(login_url='login')
def show_two(request):
    data = Apple.objects.all()
    return render(request,'show_two.html',{'data':data})

@login_required(login_url='login')
def contact(request):
    if request.method=='GET':
        form = contact_us_form()
        return render(request,'contact.html',{'form':form})
    
    else:
        data = contact_us_form(request.POST,request.FILES)
        if data.is_valid():
            data.save()
            messages.success(request,'Data is Save')
            return redirect('contact')
        else:
         return render(request,'contact.html')
        
@login_required(login_url='login')
def profile(request):
    dat = User.objects.filter(username=request.user)
    dat1 = profileimage.objects.all()
    dat3 = {
        'da1':dat,
        'da2':dat1
    }
    return render(request,'profile.html',dat3)


@login_required(login_url='login')
def changep(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changep.html', {'form': form})

@login_required(login_url='login')
def profile_image(request):
    if request.method == 'GET':
        form = profileimageform()
        return render(request,'profile_image.html',{'form':form})
    else:
        form = profileimageform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
    return render(request,'profile_image.html')

@login_required(login_url='login')
def update(request,id):
    data=profileimage.objects.get(id=id)
    if request.method == 'GET':
        form = profileimageform(instance=data)
        return render(request,'profile_image.html',{'form':form})
    else:
        form = profileimageform(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
    return render(request,'profile_image.html')

@login_required(login_url='login')
def form(request):
    if request.method =='GET':
        data = phone_form()
        return render(request,'form.html',{'data':data})
    
    else:
        data = phone_form(request.POST,request.FILES)
        if data.is_valid():
            data.save()
            return redirect('form')
        else:
            return render(request,'form.html')