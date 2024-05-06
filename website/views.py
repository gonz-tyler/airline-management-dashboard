from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import *

def home(request):
    flights = Flight.objects.all()
    cities = City.objects.all()
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error loggin in please try again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'flights': flights})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered. Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})

def view_flights(request):
    if request.user.is_authenticated:
        flights = Flight.objects.all()
        return render(request, 'home.html', {'flights': flights})

def view_flight(request, pk):
    if request.user.is_authenticated:
        #look up flight
        flight = Flight.objects.get(FLIGHTNUM=pk)
        return render(request, 'flight_details.html', {'flight':flight})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_flight(request, pk):
    if request.user.is_authenticated:
        delete_it = Flight.objects.get(FLIGHTNUM=pk)
        flight_number = delete_it.FLIGHTNUM
        delete_it.delete()
        messages.success(request, f"Flight {flight_number} Deleted Successfully")
        flight_number = None
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to perform this action.")
        return redirect('home')
    
def view_cities(request):
    if request.user.is_authenticated:
        cities = City.objects.all()
        return render(request, 'cities.html', {'cities': cities})

def view_city(request, pk):
    if request.user.is_authenticated:
        #look up city
        city = City.objects.get(CITYCODE=pk)
        return render(request, 'city_details.html', {'city':city})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def view_pilots(request):
    if request.user.is_authenticated:
        pilots = Pilot.objects.all()
        return render(request, 'pilots.html', {'pilots': pilots})

def view_pilot(request, pk):
    if request.user.is_authenticated:
        #look up plane
        pilot = Pilot.objects.get(PILOTNUM=pk)
        return render(request, 'pilot_details.html', {'pilot':pilot})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')

def view_planes(request):
    if request.user.is_authenticated:
        planes = Airplane.objects.all()
        return render(request, 'planes.html', {'planes': planes})

def view_plane(request, pk):
    if request.user.is_authenticated:
        #look up plane
        plane = Airplane.objects.get(SERIALNUM=pk)
        return render(request, 'plane_details.html', {'plane':plane})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_plane(request, pk):
    if request.user.is_authenticated:
        delete_it = Airplane.objects.get(SERIALNUM=pk)
        plane_number = delete_it.SERIALNUM
        delete_it.delete()
        messages.success(request, f"Plane {plane_number} Deleted Successfully")
        flight_number = None
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to perform this action.")
        return redirect('home')