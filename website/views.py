from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.forms import formset_factory
from django.contrib import messages
from django.urls import reverse
from .forms import *
from .models import *
import json


#-- Messages --#
admin_required = "You must be logged in as an admin user to perform this action."
record_added = "Record has been added successfully."
record_deleted = "Record has been deleted successfully."
record_updated = "Record has been updated successfully."

class UserManagement:
    def list_users(request):
        if request.user.is_superuser:
            users = User.objects.all()
            return render(request, 'users_list.html', {'users': users})
        else:
            messages.success(request, admin_required)
            return redirect('home')

    def add_user(request):
        if request.user.is_superuser:
            if request.method == 'POST':
                form = SignUpForm(request.POST)
                if form.is_valid():
                    user = form.save(commit=False)
                    password = form.cleaned_data['password1']
                    if password:
                        user.set_password(password)
                    user.save()
                    messages.success(request, "User added successfully!")
                    return redirect('list_users')
            else:
                form = SignUpForm()
            return render(request, 'user_form.html', {'form': form, 'title': 'Add User'})
        else:
            messages.success(request, admin_required)
            return redirect('home')

    def edit_user(request, user_id):
        if request.user.is_superuser:
            user = get_object_or_404(User, id=user_id)
            if request.method == 'POST':
                form = UserForm(request.POST, instance=user)
                if form.is_valid():
                    user = form.save(commit=False)
                    password = form.cleaned_data['password']
                    if password:
                        user.set_password(password)
                    user.save()
                    messages.success(request, "User updated successfully!")
                    return redirect('list_users')
            else:
                form = UserForm(instance=user)
            return render(request, 'user_form.html', {'form': form, 'title': 'Edit User'})
        else:
            messages.success(request, admin_required)
            return redirect('home')

    def delete_user(request, user_id):
        if request.user.is_superuser:
            user = get_object_or_404(User, id=user_id)
            if request.method == 'POST':
                user.delete()
                messages.success(request, "User deleted successfully!")
                return redirect('list_users')
            return render(request, 'users_confirm_delete.html', {'user': user})
        else:
            messages.success(request, admin_required)
            return redirect('home')

#-- Render Home Page --#
def home(request):
    flights = Flight.objects.all()
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
class PlaneClass:
    def view_planes(request):
        if request.user.is_authenticated:
            planes = Airplane.objects.all()
            return render(request, 'planes.html', {'planes': planes})

    def view_plane(request, serial_num):
        if request.user.is_authenticated:
            #look up plane
            plane = Airplane.objects.get(SERIALNUM=serial_num)
            return render(request, 'plane_details.html', {'plane':plane})
        else:
            messages.success(request, 'You must be logged in to view this page.')
            return redirect('home')
        
    def delete_plane(request, serial_num):
        if request.user.is_superuser:
            delete_it = Airplane.objects.get(SERIALNUM=serial_num)
            delete_it.delete()
            messages.success(request, record_deleted)
            return redirect('home')
        else:
            messages.success(request, admin_required)
            return redirect('home')
        
    def add_plane(request):
        form = AddAirplaneForm(request.POST or None)
        if request.user.is_superuser:
            if request.method == "POST":
                if form.is_valid():
                    add_plane = form.save()
                    messages.success(request, record_added)
                    return redirect("home")
            return render(request, 'add_plane.html', {"form": form})
        else:
            messages.success(request, admin_required)
            return redirect("home")

    def update_plane(request, serial_num):
        if request.user.is_superuser:
            current_record = Airplane.objects.get(SERIALNUM=serial_num)
            form = AddAirplaneForm(request.POST or None, instance=current_record)
            form.fields['SERIALNUM'].widget = forms.HiddenInput()
            if form.is_valid():
                form.save()
                messages.success(request, record_updated)
                return redirect(reverse('view_plane', kwargs={'serial_num': serial_num}))
            return render(request, 'update_plane.html', {'form':form})
        else:
            messages.success(request, admin_required)
            return redirect('home')

#-- Cities --# 
class CityClass:  
    def view_cities(request):
        if request.user.is_authenticated:
            cities = City.objects.all()
            return render(request, 'cities.html', {'cities': cities})

    def view_city(request, city_code):
        if request.user.is_authenticated:
            #look up city
            city = City.objects.get(CITYCODE=city_code)
            return render(request, 'city_details.html', {'city':city})
        else:
            messages.success(request, 'You must be logged in to view this page.')
            return redirect('home')
        
    def delete_city(request, city_code):
        if request.user.is_superuser:
            delete_it = City.objects.get(CITYCODE=city_code)
            city_code = delete_it.CITYCODE
            delete_it.delete()
            messages.success(request, record_deleted)
            city_code = None
            return redirect('home')
        else:
            messages.success(request, admin_required)
            return redirect('home')

    def add_city(request):
        form = AddCityForm(request.POST or None)
        if request.user.is_superuser:
            if request.method == "POST":
                if form.is_valid():
                    add_city = form.save()
                    messages.success(request, record_added)
                    return redirect("home")
            return render(request, 'add_city.html', {"form": form})
        else:
            messages.success(request, admin_required)
            return redirect("home")
        
    def update_city(request, city_code):
        if request.user.is_superuser:
            current_record = City.objects.get(CITYCODE=city_code)
            form = AddCityForm(request.POST or None, instance=current_record)
            form.fields['CITYCODE'].widget = forms.HiddenInput()
            if form.is_valid():
                form.save()
                messages.success(request, record_updated)
                return redirect(reverse('view_city', kwargs={'city_code': city_code}))
            return render(request, 'update_city.html', {'form':form})
        else:
            messages.success(request, admin_required)
            return redirect('home')

#-- Flights --#
class FlightClass:
    def view_flights(request):
        if request.user.is_authenticated:
            flights = Flight.objects.all()
            return render(request, 'home.html', {'flights': flights})

    def view_flight(request, flight_num):
        if request.user.is_authenticated:
            #look up flight
            flight = Flight.objects.get(FLIGHTNUM=flight_num)
            passengers = PassengerBooking.objects.filter(FLIGHTNUM=flight_num)
            crew = FlightCrew.objects.filter(FLIGHTNUM=flight_num)
            intermediate_cities = IntermediateCity.objects.filter(FLIGHTNUM=flight_num)
            return render(request, 'flight_details.html', {'flight':flight, 'passengers': passengers, 'crew': crew, 'intermediate_cities': intermediate_cities})
        else:
            messages.success(request, 'You must be logged in to view this page.')
            return redirect('home')
        
    def delete_flight(request, flight_num):
        if request.user.is_superuser:
            delete_it = Flight.objects.get(FLIGHTNUM=flight_num)
            flight_number = delete_it.FLIGHTNUM
            delete_it.delete()
            messages.success(request, record_deleted)
            flight_number = None
            return redirect('home')
        else:
            messages.success(request, admin_required)
            return redirect('home')

    def add_flight(request):
        form = AddFlightForm(request.POST or None)
        if request.user.is_superuser:
            if request.method == "POST":
                if form.is_valid():
                    add_flight = form.save()
                    messages.success(request, record_added)
                    return redirect("home")
            return render(request, 'add_flight.html', {"form": form})
        else:
            messages.success(request, admin_required)
            return redirect("home")
        
    def update_flight(request, flight_num):
        if request.user.is_superuser:
            current_record = Flight.objects.get(FLIGHTNUM=flight_num)
            form = AddFlightForm(request.POST or None, instance=current_record)
            form.fields['FLIGHTNUM'].widget = forms.HiddenInput()
            if form.is_valid():
                form.save()
                messages.success(request, record_updated)
                return redirect(reverse('view_flight', kwargs={'flight_num': flight_num}))
            return render(request, 'update_flight.html', {'form':form, "flight": current_record})
        else:
            messages.success(request, admin_required)
            return redirect('home')
        
    def delete_crew(request, flight_num, employee_num):
        if request.user.is_superuser:
            # Get the FlightCrew object with the given flight number and employee number
            delete_it = FlightCrew.objects.get(FLIGHTNUM=flight_num, EMPNUM=employee_num)
            # Delete the FlightCrew object
            delete_it.delete()
            # Add a success message
            #messages.success(request, f"Flight crew with flight number {flight_number} and employee number {employee_number} deleted successfully.")
            messages.success(request, "Crew Member Removed...")
            return redirect(reverse('view_flight', kwargs={'flight_num': flight_num}))
        else:
            # Add a message for unauthenticated users
            messages.success(request, admin_required)
            return redirect('home')

    def add_crew(request, flight_num):
        if request.user.is_superuser:
            flight = Flight.objects.get(FLIGHTNUM=flight_num)
            form = AddFlightCrewForm(request.POST or None, initial={'FLIGHTNUM': flight})
            form.fields['FLIGHTNUM'].widget = forms.HiddenInput()
            if request.method == "POST":
                if form.is_valid():
                    crew = form.save(commit=False)
                    crew.FLIGHTNUM = flight
                    crew.save()
                    messages.success(request, "Crew Member Added...")
                    #return redirect("url 'view_flight' flight_num")
                    return redirect(reverse('view_flight', kwargs={'flight_num': flight_num}))
            return render(request, 'add_crew.html', {"form": form, "flight": flight})
        else:
            messages.success(request, admin_required)
            return redirect("home")
        
    def delete_passenger_booking(request, flight_num, passenger_num):
        if request.user.is_superuser:
            delete_it = PassengerBooking.objects.get(PASSENGERNUM=passenger_num, FLIGHTNUM=flight_num)
            delete_it.delete()
            # Add a success message
            messages.success(request, "Passenger Removed...")
            return redirect(reverse('view_flight', kwargs={'flight_num': flight_num}))
        else:
            messages.success(request, admin_required)
            return redirect('home')

    def add_passenger_booking(request, flight_num):
        if request.user.is_superuser:
            flight = Flight.objects.get(FLIGHTNUM=flight_num)
            form = AddPassengerBookingForm(request.POST or None, initial={'FLIGHTNUM': flight})
            form.fields['FLIGHTNUM'].widget = forms.HiddenInput()
            if request.method == "POST":
                if form.is_valid():
                    passenger_booking = form.save(commit=False)
                    passenger_booking.FLIGHTNUM = flight
                    passenger_booking.save()
                    messages.success(request, "Passenger Added...")
                    return redirect(reverse('view_flight', kwargs={'flight_num': flight_num}))
            return render(request, 'add_passenger_booking.html', {"form": form, "flight": flight})
        else:
            messages.success(request, admin_required)
            return redirect("home")

    def delete_intermediate_city(request, stretch_num):
        if request.user.is_superuser:
            delete_it = IntermediateCity.objects.get(STRETCHNUM=stretch_num)
            flight_num = delete_it.FLIGHTNUM.FLIGHTNUM
            delete_it.delete()
            messages.success(request, "Intermediate City Removed...")
            return redirect(reverse('view_flight', kwargs={'flight_num': flight_num}))
        else:
            messages.success(request, admin_required)
            return redirect('home')

    def add_intermediate_city(request, flight_num):
        if request.user.is_superuser:
            flight = Flight.objects.get(FLIGHTNUM=flight_num)
            form = AddIntermediateCityForm(request.POST or None, initial={'FLIGHTNUM': flight})
            form.fields['FLIGHTNUM'].widget = forms.HiddenInput()
            if request.method == "POST":
                if form.is_valid():
                    intermediate_city = form.save(commit=False)
                    intermediate_city.FLIGHTNUM = flight
                    intermediate_city.save()
                    messages.success(request, "Intermediate City Added...")
                    return redirect(reverse('view_flight', kwargs={'flight_num': flight_num}))
            return render(request, 'add_intermediate_city.html', {"form": form, "flight": flight})
        else:
            messages.success(request, admin_required)
            return redirect("home")

#-- Passengers --#
class PassengerClass: 
    def view_passengers(request):
        if request.user.is_authenticated:
            passengers = Passenger.objects.all()
            return render(request, 'passengers.html', {'passengers': passengers})

    def view_passenger(request, passenger_num):
        if request.user.is_authenticated:
            passenger = Passenger.objects.get(PASSENGERNUM=passenger_num)
            bookings = PassengerBooking.objects.filter(PASSENGERNUM=passenger_num)
            addresses = PassengerAddress.objects.filter(PASSENGERNUM=passenger_num)
            phones = PassengerPhone.objects.filter(PASSENGERNUM=passenger_num)
            return render(request, 'passenger_details.html', {'passenger': passenger, 'bookings': bookings, 'addresses': addresses, 'phones': phones})
        else:
            messages.success(request, 'You must be logged in to view this page.')
            return redirect('home')
        
    def delete_passenger(request, passenger_num):
        if request.user.is_superuser:
            delete_it = Passenger.objects.get(PASSENGERNUM=passenger_num)
            delete_it.delete()
            messages.success(request, record_deleted)
            return redirect('home')
        else:
            messages.success(request, admin_required)
            return redirect('home')

    def add_passenger(request):
        if request.user.is_superuser:
            form = AddPassengerForm(request.POST or None)
            AddressFormSet = formset_factory(AddPassengerAddressForm)
            PhoneFormSet = formset_factory(AddPassengerPhoneForm)
            address_forms = AddressFormSet(request.POST or None, prefix='addresses')
            phone_forms = PhoneFormSet(request.POST or None, prefix='phones')
            if request.method == "POST":
                #data = json.loads(request.body)
                print(request.body)

                # Extracting data from POST request
                passenger_num = request.POST.get('PASSENGERNUM')
                name = request.POST.get('NAME')
                surname = request.POST.get('SURNAME')

                # Extracting addresses
                addresses = request.POST.getlist('addresses-0-ADDRESSDETAILS')

                # Extracting phones
                phones = request.POST.getlist('phones-0-PHONE')

                # Creating and saving Passenger object
                passenger = Passenger.objects.create(PASSENGERNUM=passenger_num, NAME=name, SURNAME=surname)

                # Creating and saving PassengerAddress objects
                for address in addresses:
                    PassengerAddress.objects.create(PASSENGERNUM=passenger, ADDRESSDETAILS=address)

                # Creating and saving PassengerPhone objects
                for phone in phones:
                    PassengerPhone.objects.create(PASSENGERNUM=passenger, PHONE=phone)

                messages.success(request, record_added)
                return redirect("home")

        else:
            messages.success(request, admin_required)
            return redirect("home")
        return render(request, 'add_passenger.html', {"form": form, "address_formset": address_forms, "phone_formset": phone_forms})

    def update_passenger(request, passenger_num):
        if request.user.is_superuser:
            current_record = Passenger.objects.get(PASSENGERNUM=passenger_num)
            form = AddPassengerForm(request.POST or None, instance=current_record)
            form.fields['PASSENGERNUM'].widget = forms.HiddenInput()
            if form.is_valid():
                form.save()
                messages.success(request, record_updated)
                return redirect(reverse('view_passenger', kwargs={'passenger_num': passenger_num}))
            return render(request, 'update_passenger.html', {'form':form})
        else:
            messages.success(request, admin_required)
            return redirect('home')
        
    def delete_passenger_address(request, passenger_num, address):
        if request.user.is_superuser:
            delete_it = PassengerAddress.objects.get(PASSENGERNUM=passenger_num, ADDRESSDETAILS=address)
            delete_it.delete()
            # Add a success message
            messages.success(request, "Address Removed...")
            return redirect(reverse('view_passenger', kwargs={'passenger_num': passenger_num}))
        else:
            # Add a message for unauthenticated users
            messages.success(request, admin_required)
            return redirect('home')

    def add_passenger_address(request, passenger_num):
        if request.user.is_superuser:
            passenger = Passenger.objects.get(PASSENGERNUM=passenger_num)
            form = AddPassengerAddressForm(request.POST or None, initial={'PASSENGERNUM': passenger})
            if request.method == "POST":
                if form.is_valid():
                    passenger_address = form.save(commit=False)
                    passenger_address.PASSENGERNUM = passenger
                    # Check for duplicates
                    if PassengerAddress.objects.filter(PASSENGERNUM=passenger, ADDRESSDETAILS=passenger_address.ADDRESSDETAILS).exists():
                        messages.error(request, "The address for this passenger already exists.")
                        return render(request, 'add_passenger_address.html', {"form": form})
                    passenger_address.save()
                    messages.success(request, f"Address Added...")
                    return redirect(reverse('view_passenger', kwargs={'passenger_num': passenger.PASSENGERNUM}))
            return render(request, 'add_passenger_address.html', {"form": form})
        else:
            messages.success(request, admin_required)
            return redirect("home")
    
    def delete_passenger_phone(request, phone):
        if request.user.is_superuser:
            delete_it = PassengerPhone.objects.get(PHONE=phone)
            passenger_num = delete_it.PASSENGERNUM.PASSENGERNUM
            delete_it.delete()
            messages.success(request, "Phone Removed...")
            return redirect(reverse('view_passenger', kwargs={'passenger_num': passenger_num}))
        else:
            messages.success(request, admin_required)
            return redirect('home')

    def add_passenger_phone(request, passenger_num):
        if request.user.is_superuser:
            passenger = Passenger.objects.get(PASSENGERNUM=passenger_num)
            form = AddPassengerPhoneForm(request.POST or None, initial={'PASSENGERNUM': passenger})
            if request.method == "POST":
                if form.is_valid():
                    passenger_phone = form.save(commit=False)
                    passenger_phone.PASSENGERNUM = passenger
                    valid_chars = set('0123456789-+')
                    for char in passenger_phone.PHONE:
                        if char not in valid_chars:
                            messages.error(request, "Invalid Phone Number, must only include 0-9, -, +")
                            form.data = form.data.copy()  # Make the form data mutable
                            form.data['PHONE'] = ""
                            return render(request, 'add_passenger_phone.html', {"form": form})
                    if PassengerPhone.objects.filter(PHONE=passenger_phone.PHONE).exists():
                        messages.error(request, "This phone number is already being used.")
                        form.data = form.data.copy()  # Make the form data mutable
                        form.data['PHONE'] = ""
                        return render(request, 'add_passenger_phone.html', {"form": form})
                    passenger_phone.save()
                    messages.success(request, f"Phone Added...")
                    return redirect(reverse('view_passenger', kwargs={'passenger_num': passenger.PASSENGERNUM}))
            return render(request, 'add_passenger_phone.html', {"form": form})
        else:
            messages.success(request, admin_required)
            return redirect("home")

#-- Pilots --#  
class PilotClass:  
    def view_pilots(request):
        if request.user.is_authenticated:
            pilots = Pilot.objects.all()
            return render(request, 'pilots.html', {'pilots': pilots})

    def view_pilot(request, pilot_num):
        if request.user.is_authenticated:
            # Look up pilot
            pilot = Pilot.objects.get(PILOTNUM=pilot_num)
            # Get all type ratings for the pilot
            typeratings = PilotTypeRating.objects.filter(PILOTNUM=pilot)
            addresses = StaffAddress.objects.filter(EMPNUM=pilot.EMPNUM)
            phones = StaffPhone.objects.filter(EMPNUM=pilot.EMPNUM)
            flights = Flight.objects.filter(PILOTNUM=pilot_num)
            return render(request, 'pilot_details.html', {'pilot': pilot, 'typeratings': typeratings, 'addresses': addresses, 'phones': phones, 'flights': flights})
        else:
            messages.success(request, 'You must be logged in to view this page.')
            return redirect('home')
        
    def delete_pilot(request, pilot_num):
        if request.user.is_superuser:
            delete_it = Pilot.objects.get(PILOTNUM=pilot_num)
            delete_it.delete()
            messages.success(request, record_deleted)
            return redirect('home')
        else:
            messages.success(request, admin_required)
            return redirect('home')

    def add_pilot(request):
        form = AddPilotForm(request.POST or None)
        if request.user.is_superuser:
            if request.method == "POST":
                if form.is_valid():
                    add_pilot = form.save()
                    messages.success(request, record_added)
                    return redirect("home")
            return render(request, 'add_pilot.html', {"form": form})
        else:
            messages.success(request, admin_required)
            return redirect("home")
        
    def update_pilot(request, pilot_num):
        if request.user.is_superuser:
            current_record = Pilot.objects.get(PILOTNUM=pilot_num)
            form = AddPilotForm(request.POST or None, instance=current_record)
            form.fields['PILOTNUM'].widget = forms.HiddenInput()
            if form.is_valid():
                form.save()
                messages.success(request, record_updated)
                return redirect(reverse('view_pilot', kwargs={'pilot_num': pilot_num}))
            return render(request, 'update_pilot.html', {'form':form})
        else:
            messages.success(request, admin_required)
            return redirect('home')

    def delete_pilot_typerating(request, pilot_num, typerating):
        if request.user.is_superuser:
            delete_it = PilotTypeRating.objects.get(PILOTNUM=pilot_num, TYPERATING=typerating)
            employee_num = delete_it.PILOTNUM.EMPNUM.EMPNUM
            delete_it.delete()
            # Add a success message
            messages.success(request, "Pilot type rating Removed...")
            return redirect(reverse('view_staff_member', kwargs={'employee_num': employee_num}))
        else:
            messages.success(request, admin_required)
            return redirect('home')

    def add_pilot_typerating(request, employee_num):
        if request.user.is_superuser:
            pilot = Pilot.objects.get(EMPNUM=employee_num)
            form = AddPilotTypeRatingForm(request.POST or None, initial={'PILOTNUM': pilot.PILOTNUM})
            if request.method == "POST":
                if form.is_valid():
                    typerating = form.save(commit=False)
                    typerating.PILOTNUM = pilot
                    typerating.save()
                    messages.success(request, "Pilot type rating Added...")
                    return redirect(reverse('view_staff_member', kwargs={'employee_num': employee_num}))
            return render(request, 'add_pilot_typerating.html', {"form": form})
        else:
            messages.success(request, admin_required)
            return redirect("home")

#-- Staff --#    
class StaffClass:
    def view_staff(request):
        if request.user.is_authenticated:
            staff = Staff.objects.all()
            return render(request, 'staff.html', {'staff': staff})

    def view_staff_member(request, employee_num):
        if request.user.is_authenticated:
            #look up staff_member
            staff_member = Staff.objects.get(EMPNUM=employee_num)
            addresses = StaffAddress.objects.filter(EMPNUM=employee_num)
            phones = StaffPhone.objects.filter(EMPNUM=employee_num)
            if staff_member.TYPE == 'Crew':
                flights = Flight.objects.filter(flightcrew__EMPNUM=employee_num)
                return render(request, 'staff_details.html', {'staff_member': staff_member, 'addresses': addresses, 'phones': phones, 'flights': flights})
            else:
                pilot = Pilot.objects.get(EMPNUM=employee_num)
                # Use the pilotnum to filter the Flight objects
                flights = Flight.objects.filter(PILOTNUM=pilot.PILOTNUM)
                typeratings = PilotTypeRating.objects.filter(PILOTNUM=pilot)
                return render(request, 'staff_details.html', {'staff_member': staff_member, 'addresses': addresses, 'phones': phones, 'flights': flights, 'typeratings': typeratings, 'pilot': pilot})
        else:
            messages.success(request, 'You must be logged in to view this page.')
            return redirect('home')
        
    def delete_staff_member(request, employee_num):
        if request.user.is_superuser:
            delete_it = Staff.objects.get(EMPNUM=employee_num)
            delete_it.delete()
            messages.success(request, record_deleted)
            return redirect('home')
        else:
            messages.success(request, admin_required)
            return redirect('home')        

    def add_staff_member(request):
        if request.user.is_superuser:
            form = AddStaffForm(request.POST or None)
            AddressFormSet = formset_factory(AddStaffAddressForm)
            PhoneFormSet = formset_factory(AddStaffPhoneForm)
            address_forms = AddressFormSet(request.POST or None, prefix='addresses')
            phone_forms = PhoneFormSet(request.POST or None, prefix='phones')
            
            if request.method == "POST":
                if form.is_valid() and address_forms.is_valid() and phone_forms.is_valid():
                    # Extracting data from POST request
                    employee_num = form.cleaned_data['EMPNUM']
                    name = form.cleaned_data['NAME']
                    surname = form.cleaned_data['SURNAME']
                    type = form.cleaned_data['TYPE']
                    pilot_num = form.cleaned_data['pilotnum']
                    salary = form.cleaned_data['SALARY']
                    
                    # Extracting addresses
                    addresses = request.POST.getlist('addresses-0-ADDRESSDETAILS')
                    
                    # Extracting phones
                    phones = request.POST.getlist('phones-0-PHONE')
                    
                    # Check for duplicate phone numbers
                    existing_phones = StaffPhone.objects.filter(PHONE__in=phones).values_list('PHONE', flat=True)
                    if existing_phones:
                        messages.error(request, {'PHONE': 'Phone number(s) {} already exist.'.format(', '.join(existing_phones))})
                    else:
                        # Creating and saving Staff object
                        staff_member = Staff.objects.create(EMPNUM=employee_num, NAME=name, SURNAME=surname, TYPE=type, SALARY=salary)
                        if type == 'Pilot':
                            Pilot.objects.create(EMPNUM=staff_member, PILOTNUM=pilot_num)

                        # Creating and saving StaffAddress objects
                        for address in addresses:
                            StaffAddress.objects.create(EMPNUM=staff_member, ADDRESSDETAILS=address)

                        # Creating and saving StaffPhone objects
                        for phone in phones:
                            StaffPhone.objects.create(EMPNUM=staff_member, PHONE=phone)

                        messages.success(request, record_added)
                        return redirect("view_staff")
                else:
                    messages.error(request, "Please correct the errors below.")

        else:
            messages.success(request, admin_required)
            return redirect("home")
        return render(request, 'add_staff_member.html', {"form": form, "address_formset": address_forms, "phone_formset": phone_forms})

    def update_staff_member(request, employee_num):
        if request.user.is_superuser:
            current_record = Staff.objects.get(EMPNUM=employee_num)
            if current_record.TYPE == "Pilot":
                pilot_num = Pilot.objects.get(EMPNUM=employee_num).PILOTNUM
                form = AddStaffForm(request.POST or None, instance=current_record, initial={'pilotnum': pilot_num})
                form.fields['EMPNUM'].widget = forms.HiddenInput()
                form.fields['TYPE'].widget = forms.HiddenInput()
                form.fields['pilotnum'].widget = forms.HiddenInput()
            else:
                form = AddStaffForm(request.POST or None, instance=current_record)
                form.fields['pilotnum'].widget = forms.HiddenInput()
                form.fields['EMPNUM'].widget = forms.HiddenInput()
                form.fields['TYPE'].widget = forms.HiddenInput()
            if form.is_valid():
                form.save()
                messages.success(request, record_updated)
                return redirect(reverse('view_staff_member', kwargs={'employee_num': employee_num}))
            return render(request, 'update_staff_member.html', {'form':form, 'employee_num': employee_num})
        else:
            messages.success(request, admin_required)
            return redirect('home')
    
    def delete_staff_address(request, employee_num, address):
        if request.user.is_superuser:
            # Get the FlightCrew object with the given flight number and employee number
            delete_it = StaffAddress.objects.get(EMPNUM=employee_num, ADDRESSDETAILS=address)
            # Delete the FlightCrew object
            delete_it.delete()
            messages.success(request, "Address Removed...")
            return redirect(reverse('view_staff_member', kwargs={'employee_num': employee_num}))
        else:
            # Add a message for unauthenticated users
            messages.success(request, admin_required)
            return redirect('home')

    def add_staff_address(request, employee_num):
        if request.user.is_superuser:
            employee = Staff.objects.get(EMPNUM=employee_num)
            form = AddStaffAddressForm(request.POST or None, initial={'EMPNUM': employee})
            if request.method == "POST":
                if form.is_valid():
                    staff_address = form.save(commit=False)
                    staff_address.EMPNUM = employee
                    # Check for duplicates
                    if StaffAddress.objects.filter(EMPNUM=employee, ADDRESSDETAILS=staff_address.ADDRESSDETAILS).exists():
                        messages.error(request, "The address for this staff member already exists.")
                        return render(request, 'add_staff_address.html', {"form": form})
                    staff_address.save()
                    messages.success(request, f"Address Added...")
                    return redirect(reverse('view_staff_member', kwargs={'employee_num': employee_num}))
            return render(request, 'add_staff_address.html', {"form": form})
        else:
            messages.success(request, admin_required)
            return redirect("home")
    
    def delete_staff_phone(request, phone):
        if request.user.is_superuser:
            delete_it = StaffPhone.objects.get(PHONE=phone)
            employee_num = delete_it.EMPNUM.EMPNUM
            delete_it.delete()
            messages.success(request, "Phone Removed...")
            return redirect(reverse('view_staff_member', kwargs={'employee_num': employee_num}))
        else:
            messages.success(request, admin_required)
            return redirect('home')

    def add_staff_phone(request, employee_num):
        if request.user.is_superuser:
            employee = Staff.objects.get(EMPNUM=employee_num)
            form = AddStaffPhoneForm(request.POST or None, initial={'EMPNUM': employee})
            if request.method == "POST":
                if form.is_valid():
                    staff_phone = form.save(commit=False)
                    staff_phone.EMPNUM = employee
                    valid_chars = set('0123456789-+')
                    for char in staff_phone.PHONE:
                        if char not in valid_chars:
                            messages.error(request, "Invalid Phone Number, must only include 0-9, -, +")
                            form.data = form.data.copy()  # Make the form data mutable
                            form.data['PHONE'] = ""
                            return render(request, 'add_staff_phone.html', {"form": form})
                    if StaffPhone.objects.filter(PHONE=staff_phone.PHONE).exists():
                        messages.error(request, "This phone number is already being used.")
                        form.data = form.data.copy()  # Make the form data mutable
                        form.data['PHONE'] = ""
                        return render(request, 'add_staff_phone.html', {"form": form})
                    staff_phone.save()
                    messages.success(request, f"Phone Added...")
                    return redirect(reverse('view_staff_member', kwargs={'employee_num': employee_num}))
            return render(request, 'add_staff_phone.html', {"form": form})
        else:
            messages.success(request, admin_required)
            return redirect("home")

#-- Stretch --#    
def view_stretches(request):
    if request.user.is_authenticated:
        intermediate_cities = IntermediateCity.objects.all()
        return render(request, 'stretches.html', {'intermediate_cities': intermediate_cities})

def view_stretch(request, stretch_num):
    if request.user.is_authenticated:
        #look up stretch
        intermediate_city = IntermediateCity.objects.get(STRETCHNUM=stretch_num)
        return render(request, 'stretch_details.html', {'intermediate_city':intermediate_city})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
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

#-- Passenger Phones --#    
def view_passenger_phones(request):
    if request.user.is_authenticated:
        passenger_phones = PassengerPhone.objects.all()
        return render(request, 'passenger_phones.html', {'passenger_phones': passenger_phones})

def view_passenger_phone(request, phone):
    if request.user.is_authenticated:
        #look up city
        passenger_phone = PassengerPhone.objects.get(PHONE=phone)
        return render(request, 'passenger_phone_details.html', {'passenger_phone':passenger_phone})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
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
    
#-- Flight Crews --#    
def view_crews(request):
    if request.user.is_authenticated:
        crews = FlightCrew.objects.all()
        return render(request, 'crews.html', {'crews': crews})

def view_crew(request, flight_num, employee_num):
    if request.user.is_authenticated:
        #look up city
        crew = FlightCrew.objects.get(FLIGHTNUM=flight_num, EMPNUM=employee_num)
        return render(request, 'crew_details.html', {'crew':crew})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')
    
#-- Staff Addresses --#
def view_staff_addresses(request):
    if request.user.is_authenticated:
        staff_addresses = StaffAddress.objects.all()
        return render(request, 'staff_addresses.html', {'staff_addresses': staff_addresses})

def view_staff_address(request, emp_num, address):
    if request.user.is_authenticated:
        #look up city
        staff_address = StaffAddress.objects.get(EMPNUM=emp_num, ADDRESSDETAILS=address)
        return render(request, 'staff_address_details.html', {'staff_address':staff_address})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')


#-- Staff Phones --#    
def view_staff_phones(request):
    if request.user.is_authenticated:
        phones = StaffPhone.objects.all()
        return render(request, 'staff_phones.html', {'phones': phones})

def view_staff_phone(request, phone):
    if request.user.is_authenticated:
        #look up staff phone
        staff_phone = StaffPhone.objects.get(PHONE=phone)
        return render(request, 'staff_phone_details.html', {'staff_phone': staff_phone})
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect('home')