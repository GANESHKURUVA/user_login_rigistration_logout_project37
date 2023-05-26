from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.



def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')

def Rigistration(request):
    UFO=UserForm()
    PFO=ProfileForm()
    d={'UFO':UFO,'PFO':PFO}
    if request.method=='POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=ProfileForm(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            NUFD=UFD.save(commit=False)
            NUFD.set_password(UFD.cleaned_data['password'])
            NUFD.save()
            NPFD=PFD.save(commit=False)
            NPFD.username=NUFD
            NPFD.save()
            send_mail('rigistration',
                      'rigistration successfully',
                      'ganesh.kuruva0407@gamil.com',
                      [NUFD.email],
                      fail_silently=True)
            return HttpResponse('rigisterd successfully')
        else:
            return HttpResponse('!!invalid data!!')
    return render(request,'rigistration.html',d)



def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        auo=authenticate(username=username,password=password)
        if auo and auo.is_active:
            login(request,auo)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('invalid data')
    return render(request,'user_login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))