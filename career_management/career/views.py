import razorpay
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

from django.conf import settings
from django.core.mail import send_mail

from .models import registration, login, courses
from django.db.models import Q



def loginpage(request):
    return render(request, 'index.html')

def home(request):
    data = courses.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        if q!=None:
            filtered = courses.objects.filter(Q(cousename__icontains=q) | Q(category__icontains=q) | Q(institutename__icontains=q) | Q(location__icontains=q))
            return render(request, 'searches.html', {'filtered': filtered})
    else:
        return render(request, 'home.html')


def adminhome(request):
    if request.method == 'POST':
        username = request.POST['aname']
        password = request.POST['apass']
        if User.objects.filter(username=username, password=password).exists():
            data = User.objects.all().values('email')
            print("success")
            return redirect('/admins')
        else:
            messages.info(request, 'Invalid Credentials')
            print("error")
            return redirect('/adminhp')
    else:
        return render(request, 'adminhome.html')


def loginform(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['pass1']
        if User.objects.filter(email=email, password=password1).exists():
            data = registration.objects.all().values('email')
            print("success")
            return redirect('/home/allcourse')
        else:
            messages.info(request, 'Invalid Credentials')
            print("error")
            return redirect('/login')

    else:
       return render(request, 'index.html')

def register(request,):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        if password1 == password2:
            if User.objects.filter(username=name).exists():
                messages.info(request, 'Username already exists')
                print("Username already registered")
                return redirect('/login')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                print("Email already registered")
                return redirect('/login')
            else:
                user = User(username=name, email=email, password=password1)
                user.save()
                print("user created")
                return redirect('/login')
        else:
            messages.info(request, 'Password does not match')
            print("Password is not matching")
        return redirect('/login')

    else:
        return render(request, 'index.html')



def homepage(request):
    return render(request, 'home.html')


def addcourse(request):
    if request.method == 'POST':
        name = request.POST['cname']
        duration = request.POST['duration']
        mode = request.POST['mode']
        iname = request.POST['iname']
        location = request.POST['location']
        cat = request.POST['cat']
        phone = request.POST['phone']
        cdetails = request.POST['cdetails']
        room = request.POST['room']
        data = courses(cousename=name, duration=duration, mode=mode, institutename=iname, location=location, category=cat, phone=phone, details=cdetails, rooms=room)
        data.save()
        print("course added")
        return redirect('/home')
    else:
        return render(request, 'addcourse.html')

def searchcourse(request):
    data = courses.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        filtered = courses.objects.filter(Q(cousename__icontains=q) | Q(institutename__icontains=q))
        return render(request, 'searches.html', {'filtered':filtered})
    else:
        data = courses.objects.all()
        return render(request, 'showcourse.html', {'data': data})

def searchresult(request):
    return render(request, 'searches.html')

def allcourses(request):
    data = courses.objects.all()
    return render(request, 'allcourses.html', {'data':data})

@login_required()
def adminshow(request):

    data = courses.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        if q != None:
            filtered = courses.objects.filter(
                Q(cousename__icontains=q) | Q(category__icontains=q) | Q(institutename__icontains=q) | Q(
                    location__icontains=q))
            return render(request, 'adminsearch.html', {'filtered': filtered})
    else:
        data = courses.objects.all()
        return render(request, "adminshow.html", {'data': data})

def admindelete(request, id):
    employee = courses.objects.get(id=id)
    employee.delete()
    return redirect("/admins")

def adminaddcourse(request):
    if request.method == 'POST':
        name = request.POST['cname']
        duration = request.POST['duration']
        mode = request.POST['mode']
        iname = request.POST['iname']
        location = request.POST['location']
        cat = request.POST['cat']
        phone = request.POST['phone']
        cdetails = request.POST['cdetails']
        room = request.POST['room']
        data = courses(cousename=name, duration=duration, mode=mode, institutename=iname, location=location, category=cat, phone=phone, details=cdetails, rooms=room)
        data.save()
        print("course added")
        return redirect('/admins')
    else:
        return render(request, 'adminadd.html')

