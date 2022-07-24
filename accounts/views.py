from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import RegisterForm,LoginForm
from .models import Accounts,ForgetPassword
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate ,login,logout
from django.contrib import messages
from .helper import send_forgetpassword_mail
import datetime
import uuid


# Create your views here.

def index(request):
   now = datetime.datetime.now()
   title="Home"
   data={'title':title,'today':now}
   return render(request,'home.html',data)
  

def signin(request):
  if not request.user.is_authenticated:
    if request.method=="POST":
      loginfm=LoginForm(request=request,data=request.POST)
      if loginfm.is_valid():
        username= loginfm.cleaned_data['username']
        password=loginfm.cleaned_data['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'loged In successfully !')
            return redirect('/dashboard')
        else:
            messages.error(request, 'Username and Password does not exist!')
            return redirect('/signin')
      else:
        data={'title':'signin','loginfm':loginfm}
        return render(request,'signin.html',data)
    else:
      loginfm=LoginForm()
      data={'title':'signin','loginfm':loginfm}
      return render(request,'signin.html',data)
  else:
    return redirect('/dashboard')

def signup(request):
  if not request.user.is_authenticated:

    if request.method=="POST":
      regfm=RegisterForm(request.POST)
      if regfm.is_valid():
        account=Accounts()
        account.first_name=regfm.cleaned_data['first_name']
        account.last_name=regfm.cleaned_data['last_name']
        account.email=regfm.cleaned_data['email']
        account.mobile=regfm.cleaned_data['mobile']
        account.password= make_password(regfm.cleaned_data['password2'])
        account.save()
        return redirect('/signin')
      else:
        data={'title':'SignUp','regfm':regfm}
        return render(request,'signup.html',data)
    else:
      regfm=RegisterForm()
      data={'title':'SignUp','regfm':regfm}
      return render(request,'signup.html',data)
  else:
    return redirect('/dashboard')

def forgetpassword(request):
  if request.method=="POST":
    email=request.POST.get('email')
    accounts=Accounts.objects.filter(email=email).first()
    if accounts !=None:
      token=str(uuid.uuid4())
      accounts.token=token
      accounts.save()
      if send_forgetpassword_mail(accounts,token):
        print(accounts.id)
        messages.success(request,"Email successfully send!")
        title="Forget Password"
        data={'title':title}
        return render(request,'forgetpassword.html')
    else:
      title="Forget Password"
      data={'title':title}
      messages.error(request,"Email does not Exist!")
      return render(request,'forgetpassword.html')
  else:
    title="Forget Password"
    data={'title':title}
    return render(request,'forgetpassword.html')

def resetpassword(request,token):
  forgetdata=ForgetPassword.objects.get(token=token)
  title="Reset Password"
  data={'title':title,'user':forgetdata}
  return render(request,'resetpassword.html',data)

def dashboard(request):
  if request.user.is_authenticated:
    title="dashboard"
    data={'title':'dashboard'}
    return render(request,'dashboard.html',data)
  else:
    return redirect('/signin')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logout Successfully!')
    return redirect('/signin')

