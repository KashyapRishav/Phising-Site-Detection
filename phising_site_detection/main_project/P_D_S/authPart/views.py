
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.shortcuts import render,redirect
from django.http import HttpResponse
import joblib,os
import pickle

phish_model = open('phishing.pkl','rb')
phish_model_ls = joblib.load(phish_model)

def home(request):
    return render(request,"home.html")

def index(request):
    return render(request,"index.html")

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content) <4:
            messages.error(request,"Please Fill the Form Correctly ")
            return redirect('contact')
        else:
            contact=Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"Your Message has been successfully sent")
            return redirect('contact')
    else:
        return render(request,'contact.html')
def result(features):
	X_predict = []
	X_predict.append(str(features))
	y_Predict = phish_model_ls.predict(X_predict)
	if y_Predict == 'bad':
		result = "ALERT!! PHISHING SITE DETECTED"
	else:
		result = "LEGITMATE SITE DETECTED"

	return render(features, "result.html",{'result' : result})


def handleSignup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if len(username)<6 or len(username)>15 :
            messages.error(request, " Your user name must be under 6 to 15 characters")
            return redirect('index')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('index')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('index')
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('index')
    else:
        return HttpResponse('404 - Not found')
def handleLogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request, " Successfully Logged In.")
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('index')

    else:
        return HttpResponse('404 - Not found')


def handleLogout(request):
    logout(request)
    messages.success(request, " Successfully Logged Out.")
    return redirect('index')
