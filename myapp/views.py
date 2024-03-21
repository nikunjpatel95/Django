from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Feature
## the User below is the User that is in admin panel, auth is the method hat allows us to authenticate
from django.contrib.auth.models import User,auth  
from django.contrib import messages


# Create your views here.
def index(request):
    #return HttpResponse("<h1> Welcome to my first Django</h1>")

    """context={
        'name': "Nikunj's",
        'age': 25,
        'nationality': "Indian"
    }

    return render(request,'index.html',context)"""


    
    """feature1=Feature()
    feature1.id=0
    feature1.name="Fast"
    feature1.details="I am Fast and Furious"
    feature1.is_rich=None

    feature2=Feature()
    feature2.id=1
    feature2.name="Lightnin McQueen"
    feature2.details="I am Speed"
    feature2.is_rich=False

    feature3=Feature()
    feature3.id=2
    feature3.name="Spiderman"
    feature3.details="With Great Power, comes Great Responsibility"
    feature3.is_rich=False

    feature4=Feature()
    feature4.id=3
    feature4.name="Batman"
    feature4.details="I am Batman"
    feature4.is_rich=True"""

    #return render(request,'index.html',{'feature1':feature1,'feature2':feature2,'feature3':feature3,'feature4':feature4})
    """context={
        'feature':feature1,
        'feature2':feature2,
        'feature3':feature3,
        'feature4':feature4
    }
    return render(request,'index.html',context)"""

    ##features=[feature1,feature2,feature3,feature4]

    ##IMP
    features=Feature.objects.all()  ## here, we called the Feature model and called all the objects that are in db  
    return render(request,"index.html",{'features':features})

    

def counter(request):
    words=request.POST['text']
    total_words=len(words.split(" "))
    return render(request,'counter.html',{"amount":total_words})


def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        repeat_password=request.POST['repeat_password']

        if password==repeat_password:
            if User.objects.filter(email=email).exists(): ## this checks if email exists in db
                messages.info(request, 'Email Already Used')  ## this will show the message in the template that is here
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('register')
            
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password is not same")
            return redirect('register')
    else:
        return render(request,'register.html')


def login(request):
    if request.method=="POST":
        username1=request.POST["username"]
        password=request.POST["password"]

        user=auth.authenticate(username=username1,password=password)
        ##the above line checks the if the username and password matches to any users username and password is in db 
        ## left username and password is for username and password  in db
        ##while right username1 and password is the variable that we have mentioned that is what user has provided  
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Credentials Invalid")
            return redirect('login')
    else:
        return render(request,'login.html')