from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import *
import bcrypt

def index(request):
    return render(request, "main.html")

def success(request):
    loggedinUser  = User.objects.get( id = request.session['loggedinUserID'])
    all_trips = Trip.objects.all().exclude(Q(creator = loggedinUser) | Q(join =loggedinUser))
    context={
        'loggedinUser': loggedinUser,
        'all_trips_currentUser': Trip.objects.filter(Q(creator = loggedinUser) | Q(join =loggedinUser)),
        'all_trips': all_trips
    }
    print(all_trips)
    return render(request, "success.html", context)

def registration(request):
    print(request.POST)
    errors = User.objects.registration_validator(request.POST)
    print (errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/main')
    passwordFromForm = request.POST['password']
    hashed_password=  bcrypt.hashpw(passwordFromForm.encode(), bcrypt.gensalt())
    newuser = User.objects.create(name = request.POST['name'], username = request.POST['username'], password = hashed_password.decode())
    request.session['loggedinUserID'] = newuser.id
    return redirect('/travels')


def login(request):
    print (request.POST)
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/main')
    else:
        loggedinUser = User.objects.filter(username = request.POST['username'])
        loggedinUser = loggedinUser[0]
        request.session["loggedinUserID"] = loggedinUser.id
        return redirect ('/travels')


def plan(request):
    loggedinUser  = User.objects.get( id = request.session['loggedinUserID'])
    all_trips =  Trip.objects.filter(id = request.session['loggedinUserID'])

    context={
        'loggedinUser': loggedinUser,
        'all_trips': all_trips,
        'all_trips_currentUser': Trip.objects.filter(creator = loggedinUser),
    }
    
    return render(request, "plan.html", context)

def planning(request):
    print(request.POST)
    loggedinUser =  User.objects.get( id = request.session['loggedinUserID'])
    errors = Trip.objects.tripValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/travels/add')
    trip = Trip.objects.create( destination = request.POST['destination'], startDate = request.POST['startDate'],endDate= request.POST['endDate'], plan = request.POST['plan'], creator = loggedinUser)
    print(trip)
    return redirect("/travels")

def info(request, trip_id):
    loggedinUser =  User.objects.get( id = request.session['loggedinUserID'])
    trip = Trip.objects.get(id = trip_id)
    context={
        'loggedinUser': loggedinUser,
        'trip': trip,
        "users": trip.join.all()
    }
    return render(request, "info.html", context)

def join(request, trip_id):
    loggedinUser = User.objects.get(id = request.session['loggedinUserID'])
    jointrip = Trip.objects.get(id = trip_id)
    jointrip.join.add(loggedinUser)
    print(jointrip.join )
    return redirect("/travels")


def logout(request):
    request.session.clear()
    return redirect('/main')

# def removeitem(request, trip_id):
#     print(request.method)
#     itemToRemove = Trip.objects.get(id = trip_id)
#     itemToRemove.delete()
#     return redirect("/travels")
