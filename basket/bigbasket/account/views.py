from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages

# Create your views here.
def register(request):

    if request.method=='POST':

        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Exists')
                return render(request,"register.html",{'label':'danger'})
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Exists')
                return render(request,"register.html",{'label':'danger'})
                # return redirect('register')

            else:
                user = User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
                user.save();
                messages.info(request,'Your account created successfully')
                # return render(request,"login.html",{'label':'success'})
                return redirect('login')
        else:
            messages.info(request,"Passwords does'nt Match")
            return render(request,"register.html",{'label':'danger'})        

    else:
        return render(request,"register.html")

def login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials Invalid')
            # return redirect('login')
            return render(request,"login.html",{'label':'danger'})       
    else:
        return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')        
    
def cart_add(request):
    return render(request,"login.html")