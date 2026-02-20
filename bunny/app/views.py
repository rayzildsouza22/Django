from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Students
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages


# Create your views here.
#def hello(request):
    #return HttpResponse("<h1>Hello Panda</h1>")
#def hello(request):
    #return render(request,"hello.html")
from .models import Students

def hello(request):
    if(request.method=='POST'):
        data =request.POST
        name=data.get('name')
        email=data.get('email')
        age=data.get('age')
        address=data.get('address')

        Students.objects.create(
            name = name,
            email = email,
            age = age,
            address = address
        )
        print("the data is added successfully")
    stu=Students.objects.all()
    if(request.GET.get('search')):
        stu=Students.objects.filter(name__icontains=request.GET.get('search'))

    print(stu)
        
    hello12 = "This is a string"
    con = {'hell':stu}

    return render(request,"form.html",con)

def dell(request, id):
    student = Students.objects.get(id=id)
    student.delete()
    return redirect('/')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
def upda(request,id):
    record=Students.objects.all().get(id=id)
    if(request.method=='POST'):
        data =request.POST
        name=data.get('name')
        email=data.get('email')
        age=data.get('age')
        address=data.get('address')
        record.name=name
        record.email=email
        record.age=age
        record.address=address

        record.save()
        print("The data is updated successfully")
        return redirect('/')
    return render(request, 'update.html', {'hell': record})

def register(req):
    if (req.method == "POST"):
        data =req.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        password = data.get("password")

        user=User.objects.filter(username = username)
        if(user.exists()):
            messages.error(req,"User already exists")
            return redirect('/register/')

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
           
        )
        user.set_password(password)
        user.save()
        messages.info(req,"User added successfully")

        return redirect("/") 

    return render(req, "register.html")

def login(req):
    if (req.method == "POST"):
        data =req.POST
        username = data.get("username")
        password = data.get("password")

        user=User.objects.filter(username = username)
        if not user.exists():
            messages.error(req,"Username is invalid")
            return redirect('/login/')

        user=authenticate(req,username=username,password=password)
        if user is not None:
            return redirect("/") 
        else:
            messages.error(req,"Password is invalid")
            return redirect("/login/")
    return render(req, "login.html")

    


      

    