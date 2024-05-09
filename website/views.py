from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
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
    form = AddAirplaneForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_plane = form.save()
                messages.success(request, f"Record Added...")
                return redirect("home")
        return render(request, 'add_plane.html', {"form": form})
    else:
        messages.success(request, f"You must be logged in...")
        return redirect("home")

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
    if request.user.is_authenticated:
        delete_it = City.objects.get(CITYCODE=pk)
        city_code = delete_it.CITYCODE
        delete_it.delete()
        messages.success(request, f"City {city_code} Deleted Successfully")
        city_code = None
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to perform this action.")
        return redirect('home')

def add_city(request):
    form = AddCityForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_city = form.save()
                messages.success(request, f"Record Added...")
                return redirect("home")
        return render(request, 'add_city.html', {"form": form})
    else:
        messages.success(request, f"You must be logged in...")
        return redirect("home")

#-- Flight Crews --#    
def view_crews(request):
    if request.user.is_authenticated:
        crews = FlightCrew.objects.all()
        return render(request, 'crews.html', {'crews': crews})

def view_crew(request, flight_number, employee_number):
    if request.user.is_authenticated:
        #look up city
        crew = FlightCrew.objects.get(FLIGHTNUM=flight_number, EMPNUM=employee_number)
        return render(request, 'crew_details.html', {'crew':crew})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_crew(request, flight_number, employee_number):
    if request.user.is_authenticated:
        # Get the FlightCrew object with the given flight number and employee number
        delete_it = FlightCrew.objects.get(FLIGHTNUM=flight_number, EMPNUM=employee_number)
        # Delete the FlightCrew object
        delete_it.delete()
        # Add a success message
        messages.success(request, f"Flight crew with flight number {flight_number} and employee number {employee_number} deleted successfully.")
        # Redirect to the desired page (e.g., home)
        return redirect('home')
    else:
        # Add a message for unauthenticated users
        messages.error(request, "You must be logged in to perform this action.")
        return redirect('home')

def add_crew(request):
    form = AddFlightCrewForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_crew = form.save()
                messages.success(request, f"Record Added...")
                return redirect("home")
        return render(request, 'add_crew.html', {"form": form})
    else:
        messages.success(request, f"You must be logged in...")
        return redirect("home")

#-- Flights --#
def view_flights(request):
    if request.user.is_authenticated:
        flights = Flight.objects.all()
        return render(request, 'home.html', {'flights': flights})

def view_flight(request, pk):
    if request.user.is_authenticated:
        #look up flight
        flight = Flight.objects.get(FLIGHTNUM=pk)
        passengers = PassengerBooking.objects.filter(FLIGHTNUM=pk)
        crew = FlightCrew.objects.filter(FLIGHTNUM=pk)
        return render(request, 'flight_details.html', {'flight':flight, 'passengers': passengers, 'crew': crew})
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
    form = AddFlightForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_flight = form.save()
                messages.success(request, f"Record Added...")
                return redirect("home")
        return render(request, 'add_flight.html', {"form": form})
    else:
        messages.success(request, f"You must be logged in...")
        return redirect("home")

#-- Passenger Addresses --#    
def view_passenger_addresses(request):
    if request.user.is_authenticated:
        passenger_addresses = PassengerAddress.objects.all()
        return render(request, 'passenger_addresses.html', {'passenger_addresses': passenger_addresses})

def view_passenger_address(request, passenger_num, passenger_address):
    if request.user.is_authenticated:
        #look up address
        address = PassengerAddress.objects.get(PASSENGERNUM=passenger_num, ADDRESSDETAILS=passenger_address)
        return render(request, 'passenger_address_details.html', {'address':address})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_passenger_address(request, passenger_num, passenger_address):
    if request.user.is_authenticated:
        delete_it = PassengerAddress.objects.get(PASSENGERNUM=passenger_num, ADDRESSDETAILS=passenger_address)
        delete_it.delete()
        # Add a success message
        messages.success(request, f"Passenger address with address {passenger_address} and passenger number {passenger_num} deleted successfully.")
        # Redirect to the desired page (e.g., home)
        return redirect('home')
    else:
        # Add a message for unauthenticated users
        messages.error(request, "You must be logged in to perform this action.")
        return redirect('home')

def add_passenger_address(request):
    form = AddPassengerAddressForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_passenger_address = form.save()
                messages.success(request, f"Record Added...")
                return redirect("home")
        return render(request, 'add_passenger_address.html', {"form": form})
    else:
        messages.success(request, f"You must be logged in...")
        return redirect("home")

#-- Passenger Bookings --#    
def view_passenger_bookings(request):
    if request.user.is_authenticated:
        bookings = PassengerBooking.objects.all()
        return render(request, 'bookings.html', {'bookings': bookings})

def view_passenger_booking(request, passenger_num, flight_num):
    if request.user.is_authenticated:
        #look up booking
        booking = PassengerBooking.objects.get(PASSENGERNUM=passenger_num, FIGHTNUM=flight_num)
        return render(request, 'booking_details.html', {'booking':booking})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_passenger_booking(request, passenger_num, flight_num):
    if request.user.is_authenticated:
        delete_it = PassengerBooking.objects.get(PASSENGERNUM=passenger_num, FIGHTNUM=flight_num)
        delete_it.delete()
        # Add a success message
        messages.success(request, f"Passenger booking with flight number {flight_num} and passenger number {passenger_num} deleted successfully.")
        # Redirect to the desired page (e.g., home)
        return redirect('home')
    else:
        messages.success(request, 'You must be logged in to perform this action.')
        return redirect('home')

def add_passenger_booking(request):
    form = AddPassengerBookingForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_passenger_booking = form.save()
                messages.success(request, f"Record Added...")
                return redirect("home")
        return render(request, 'add_passenger_booking.html', {"form": form})
    else:
        messages.success(request, f"You must be logged in...")
        return redirect("home")

#-- Passenger Phones --#    
def view_passenger_phones(request):
    if request.user.is_authenticated:
        passenger_phones = PassengerPhone.objects.all()
        return render(request, 'passenger_phones.html', {'passenger_phones': passenger_phones})

def view_passenger_phone(request, pk):
    if request.user.is_authenticated:
        #look up city
        passenger_phone = PassengerPhone.objects.get(PHONE=pk)
        return render(request, 'passenger_phone_details.html', {'passenger_phone':passenger_phone})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_passenger_phone(request, pk):
    if request.user.is_authenticated:
        delete_it = PassengerPhone.objects.get(PHONE=pk)
        delete_it.delete()
        messages.success(request, f"Phone number {pk} Deleted Successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to perform this action.")
        return redirect('home')

def add_passenger_phone(request):
    form = AddPassengerPhoneForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_passenger_phone = form.save()
                messages.success(request, f"Record Added...")
                return redirect("home")
        return render(request, 'add_passenger_phone.html', {"form": form})
    else:
        messages.success(request, f"You must be logged in...")
        return redirect("home")

#-- Passengers --#    
def view_passengers(request):
    if request.user.is_authenticated:
        passengers = Passenger.objects.all()
        return render(request, 'passengers.html', {'passengers': passengers})

def view_passenger(request, pk):
    if request.user.is_authenticated:
        passenger = Passenger.objects.get(PASSENGERNUM=pk)
        bookings = PassengerBooking.objects.filter(PASSENGERNUM=pk)
        addresses = PassengerAddress.objects.filter(PASSENGERNUM=pk)
        phones = PassengerPhone.objects.filter(PASSENGERNUM=pk)
        return render(request, 'passenger_details.html', {'passenger': passenger, 'bookings': bookings, 'addresses': addresses, 'phones': phones})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_passenger(request, pk):
    if request.user.is_authenticated:
        delete_it = Passenger.objects.get(PASSENGERNUM=pk)
        delete_it.delete()
        messages.success(request, f"Passenger with passenger number {pk} Deleted Successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to perform this action.")
        return redirect('home')

def add_passenger(request):
    form = AddPassengerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_passenger = form.save()
                messages.success(request, f"Record Added...")
                return redirect("home")
        return render(request, 'add_passenger.html', {"form": form})
    else:
        messages.success(request, f"You must be logged in...")
        return redirect("home")

#-- Pilot Typeratings --#
def view_pilot_typeratings(request):
    if request.user.is_authenticated:
        typeratings = PilotTypeRating.objects.all()
        return render(request, 'typeratings.html', {'typeratings': typeratings})

def view_pilot_typerating(request, pilot_num, typerating):
    if request.user.is_authenticated:
        pilot_typerating = PilotTypeRating.objects.get(PILOTNUM=pilot_num, TYPERATING=typerating)
        return render(request, 'typerating_details.html', {'pilot_typerating': pilot_typerating})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_pilot_typerating(request, pilot_num, typerating):
    if request.user.is_authenticated:
        delete_it = PilotTypeRating.objects.get(PILOTNUM=pilot_num, TYPERATING=typerating)
        delete_it.delete()
        # Add a success message
        messages.success(request, f"Pilot type rating with pilot number {pilot_num} and type rating {typerating} deleted successfully.")
        # Redirect to the desired page (e.g., home)
        return redirect('home')
    else:
        messages.success(request, 'You must be logged in to perform this action.')
        return redirect('home')

def add_pilot_typerating(request):
    form = AddPilotTypeRatingForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_pilot_typerating = form.save()
                messages.success(request, f"Record Added...")
                return redirect("home")
        return render(request, 'add_pilot_typerating.html', {"form": form})
    else:
        messages.success(request, f"You must be logged in...")
        return redirect("home")

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
        addresses = StaffAddress.objects.filter(EMPNUM=pilot.EMPNUM)
        phones = StaffPhone.objects.filter(EMPNUM=pilot.EMPNUM)
        flights = Flight.objects.filter(PILOTNUM=pk)
        return render(request, 'pilot_details.html', {'pilot': pilot, 'typeratings': typeratings, 'addresses': addresses, 'phones': phones, 'flights': flights})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_pilot(request, pk):
    if request.user.is_authenticated:
        delete_it = Pilot.objects.get(PILOTNUM=pk)
        delete_it.delete()
        messages.success(request, f"Pilot with pilot number {pk} Deleted Successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to perform this action.")
        return redirect('home')

def add_pilot(request):
    form = AddPilotForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_pilot = form.save()
                messages.success(request, f"Record Added...")
                return redirect("home")
        return render(request, 'add_pilot.html', {"form": form})
    else:
        messages.success(request, f"You must be logged in...")
        return redirect("home")

#-- Staff Addresses --#
def view_staff_addresses(request):
    if request.user.is_authenticated:
        staff_addresses = StaffAddress.objects.all()
        return render(request, 'staff_addresses.html', {'staff_addresses': staff_addresses})

def view_staff_address(request, emp_num, address_details):
    if request.user.is_authenticated:
        #look up city
        staff_address = StaffAddress.objects.get(EMPNUM=emp_num, ADDRESSDETAILS=address_details)
        return render(request, 'staff_address_details.html', {'staff_address':staff_address})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_staff_address(request, empnum, address):
    if request.user.is_authenticated:
        # Get the FlightCrew object with the given flight number and employee number
        delete_it = StaffAddress.objects.get(EMPNUM=empnum, ADDRESSDETAILS=address)
        # Delete the FlightCrew object
        delete_it.delete()
        # Add a success message
        messages.success(request, f"Staff address with employee number {empnum} and address details {address} deleted successfully.")
        # Redirect to the desired page (e.g., home)
        return redirect('home')
    else:
        # Add a message for unauthenticated users
        messages.error(request, "You must be logged in to perform this action.")
        return redirect('home')

def add_staff_address(request):
    form = AddStaffAddressForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_staff_address = form.save()
                messages.success(request, f"Record Added...")
                return redirect("home")
        return render(request, 'add_staff_address.html', {"form": form})
    else:
        messages.success(request, f"You must be logged in...")
        return redirect("home")

#-- Staff Phones --#    
def view_staff_phones(request):
    if request.user.is_authenticated:
        phones = StaffPhone.objects.all()
        return render(request, 'staff_phones.html', {'phones': phones})

def view_staff_phone(request, pk):
    if request.user.is_authenticated:
        #look up staff phone
        staff_phone = StaffPhone.objects.get(PHONE=pk)
        return render(request, 'staff_phone_details.html', {'staff_phone': staff_phone})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_staff_phone(request, pk):
    if request.user.is_authenticated:
        delete_it = StaffPhone.objects.get(PHONE=pk)
        delete_it.delete()
        messages.success(request, f"Phone number {pk} Deleted Successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to perform this action.")
        return redirect('home')

def add_staff_phone(request):
    form = AddStaffPhoneForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_staff_phone = form.save()
                messages.success(request, f"Record Added...")
                return redirect("home")
        return render(request, 'add_staff_phone.html', {"form": form})
    else:
        messages.success(request, f"You must be logged in...")
        return redirect("home")
    
#-- Staff --#    
def view_staff(request):
    if request.user.is_authenticated:
        staff = Staff.objects.all()
        return render(request, 'staff.html', {'staff': staff})

def view_staff_member(request, pk):
    if request.user.is_authenticated:
        #look up staff_member
        staff_member = Staff.objects.get(EMPNUM=pk)
        addresses = StaffAddress.objects.filter(EMPNUM=pk)
        phones = StaffPhone.objects.filter(EMPNUM=pk)
        flights = Flight.objects.filter(flightcrew__EMPNUM=pk)
        return render(request, 'staff_details.html', {'staff_member': staff_member, 'addresses': addresses, 'phones': phones, 'flights': flights})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_staff_member(request, pk):
    if request.user.is_authenticated:
        delete_it = Staff.objects.get(EMPNUM=pk)
        delete_it.delete()
        messages.success(request, f"Staff member with employee number {pk} Deleted Successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to perform this action.")
        return redirect('home')

def add_staff_member(request):
    form = AddStaffForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_staff_member = form.save()
                messages.success(request, f"Record Added...")
                return redirect("home")
        return render(request, 'add_staff_member.html', {"form": form})
    else:
        messages.success(request, f"You must be logged in...")
        return redirect("home")

#-- Stretch --#    
def view_stretches(request):
    if request.user.is_authenticated:
        stretches = Stretch.objects.all()
        return render(request, 'stretches.html', {'stretches': stretches})

def view_stretch(request, pk):
    if request.user.is_authenticated:
        #look up stretch
        stretch = Stretch.objects.get(STRETCHNUM=pk)
        return render(request, 'stretch_details.html', {'stretch':stretch})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
def delete_stretch(request, pk):
    if request.user.is_authenticated:
        delete_it = Stretch.objects.get(STRETCHNUM=pk)
        delete_it.delete()
        messages.success(request, f"Stretch with stretch number {pk} Deleted Successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to perform this action.")
        return redirect('home')

def add_stretch(request):
    form = AddStretchForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_stretch = form.save()
                messages.success(request, f"Record Added...")
                return redirect("home")
        return render(request, 'add_stretch.html', {"form": form})
    else:
        messages.success(request, f"You must be logged in...")
        return redirect("home")