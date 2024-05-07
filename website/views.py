from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import *

#-- Render Home Page --#
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

#-- Logout User --#
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')

#-- Register User --#
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

#-- Planes --#
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
    
def add_plane(request):
    pass

#-- Cities --#    
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
    
def delete_city(request, pk):
    pass

def add_city(request):
    pass

#-- Flight Crews --#    
def view_crews(request):
    if request.user.is_authenticated:
        crews = FlightCrew.objects.all()
        return render(request, 'crews.html', {'crews': crews})

def view_crew(request, pk):
    if request.user.is_authenticated:
        #look up city
        crew = FlightCrew.objects.get(EMPNUM=pk)
        return render(request, 'crew_details.html', {'crew':crew})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_crew(request, pk):
    pass

def add_crew(request):
    pass

#-- Flights --#
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

def add_flight(request):
    return render(request, 'add_flight.html')

#-- Passenger Addresses --#    
def view_passenger_addresses(request):
    if request.user.is_authenticated:
        passenger_addresses = PassengerAddress.objects.all()
        return render(request, 'passenger_addresses.html', {'passenger_addresses': passenger_addresses})

def view_passenger_address(request, pk):
    if request.user.is_authenticated:
        #look up city
        city = City.objects.get(CITYCODE=pk)
        return render(request, 'city_details.html', {'city':city})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_passenger_address(request, pk):
    pass

def add_passenger_address(request):
    pass

#-- Passenger Bookings --#    
def view_passenger_bookings(request):
    if request.user.is_authenticated:
        cities = City.objects.all()
        return render(request, 'cities.html', {'cities': cities})

def view_passenger_booking(request, pk):
    if request.user.is_authenticated:
        #look up city
        city = City.objects.get(CITYCODE=pk)
        return render(request, 'city_details.html', {'city':city})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_passenger_booking(request, pk):
    pass

def add_passenger_booking(request):
    pass

#-- Passenger Phones --#    
def view_passenger_phones(request):
    if request.user.is_authenticated:
        cities = City.objects.all()
        return render(request, 'cities.html', {'cities': cities})

def view_passenger_phone(request, pk):
    if request.user.is_authenticated:
        #look up city
        city = City.objects.get(CITYCODE=pk)
        return render(request, 'city_details.html', {'city':city})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_passenger_phone(request, pk):
    pass

def add_passenger_phone(request):
    pass

#-- Passengers --#    
def view_passengers(request):
    if request.user.is_authenticated:
        cities = City.objects.all()
        return render(request, 'cities.html', {'cities': cities})

def view_passenger(request, pk):
    if request.user.is_authenticated:
        #look up city
        city = City.objects.get(CITYCODE=pk)
        return render(request, 'city_details.html', {'city':city})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_passenger(request, pk):
    pass

def add_passenger(request):
    pass

#-- Pilot Typeratings --#    
def view_pilot_typeratings(request):
    if request.user.is_authenticated:
        cities = City.objects.all()
        return render(request, 'cities.html', {'cities': cities})

def view_pilot_typerating(request, pk):
    if request.user.is_authenticated:
        #look up city
        city = City.objects.get(CITYCODE=pk)
        return render(request, 'city_details.html', {'city':city})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_pilot_typerating(request, pk):
    pass

def add_pilot_typerating(request):
    pass

#-- Pilots --#    
def view_pilots(request):
    if request.user.is_authenticated:
        pilots = Pilot.objects.all()
        return render(request, 'pilots.html', {'pilots': pilots})

def view_pilot(request, pk):
    if request.user.is_authenticated:
        # Look up pilot
        pilot = Pilot.objects.get(PILOTNUM=pk)
        # Get all type ratings for the pilot
        typeratings = PilotTypeRating.objects.filter(PILOTNUM=pilot)
        return render(request, 'pilot_details.html', {'pilot': pilot, 'typeratings': typeratings})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_pilot(request, pk):
    pass

def add_pilot(request):
    pass

#-- Staff Addresses --#    
def view_staff_addresses(request):
    if request.user.is_authenticated:
        cities = City.objects.all()
        return render(request, 'cities.html', {'cities': cities})

def view_staff_address(request, pk):
    if request.user.is_authenticated:
        #look up city
        city = City.objects.get(CITYCODE=pk)
        return render(request, 'city_details.html', {'city':city})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_staff_address(request, pk):
    pass

def add_staff_address(request):
    pass

#-- Staff Phones --#    
def view_staff_phones(request):
    if request.user.is_authenticated:
        cities = City.objects.all()
        return render(request, 'cities.html', {'cities': cities})

def view_staff_phone(request, pk):
    if request.user.is_authenticated:
        #look up city
        city = City.objects.get(CITYCODE=pk)
        return render(request, 'city_details.html', {'city':city})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_staff_phone(request, pk):
    pass

def add_staff_phone(request):
    pass
    
#-- Staff --#    
def view_staff(request):
    if request.user.is_authenticated:
        cities = City.objects.all()
        return render(request, 'cities.html', {'cities': cities})

def view_staff_member(request, pk):
    if request.user.is_authenticated:
        #look up city
        city = City.objects.get(CITYCODE=pk)
        return render(request, 'city_details.html', {'city':city})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_staff_member(request, pk):
    pass

def add_staff_member(request):
    pass

#-- Stretch --#    
def view_stretches(request):
    if request.user.is_authenticated:
        cities = City.objects.all()
        return render(request, 'cities.html', {'cities': cities})

def view_stretch(request, pk):
    if request.user.is_authenticated:
        #look up city
        city = City.objects.get(CITYCODE=pk)
        return render(request, 'city_details.html', {'city':city})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_stretch(request, pk):
    pass

def add_stretch(request):
    pass