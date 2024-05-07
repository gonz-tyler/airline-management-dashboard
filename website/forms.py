from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	
            

class AddAirplaneForm(forms.ModelForm):
    serial_number = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Serial Number", "class":"form-control"}), label="")
    manufacturer = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    model = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")

    class Meta:
        model = Airplane
        exclude = ("user",)

class AddCityForm(forms.ModelForm):
    city_code = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    city_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")

    class Meta:
        model = City
        exclude = ("user",)

class AddStaffForm(forms.ModelForm):
    employee_number = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Serial Number", "class":"form-control"}), label="")
    surname = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    salary = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Serial Number", "class":"form-control"}), label="")
    type = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")

    class Meta:
        model = Staff
        exclude = ("user",)

class AddPilotForm(forms.ModelForm):
    pilot_number = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Serial Number", "class":"form-control"}), label="")
    pilot_choices = Staff.objects.filter(TYPE='Pilot')
    employee_number = forms.ModelChoiceField(queryset=pilot_choices, widget=forms.Select(attrs={"class": "form-control"}), label="")

    class Meta:
        model = Pilot
        exclude = ("user",)

class AddFlightForm(forms.ModelForm):
    flight_number = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Flight Number", "class":"form-control"}), label="")
    origin_city_code = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")
    destination_city_code = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")
    departure_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control", "placeholder": "YYYY-MM-DD HH:MM:SS"}), label="")
    arrival_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control", "placeholder": "YYYY-MM-DD HH:MM:SS"}), label="")
    pilot_number = forms.ModelChoiceField(queryset=Pilot.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")
    plane_number = forms.ModelChoiceField(queryset=Airplane.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")

    class Meta:
        model = Flight
        exclude = ("user",)

class AddFlightCrewForm(forms.ModelForm):
    flight_number = forms.ModelChoiceField(queryset=Flight.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")
    crew_choices = Staff.objects.filter(TYPE='Crew')
    employee_number = forms.ModelChoiceField(queryset=crew_choices, widget=forms.Select(attrs={"class": "form-control"}), label="")

    class Meta:
        model = FlightCrew
        exclude = ("user",)

class AddPassengerForm(forms.ModelForm):
    passenger_number = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Serial Number", "class":"form-control"}), label="")
    surname = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")

    class Meta:
        model = Passenger
        exclude = ("user",)

class AddPassengerAddressForm(forms.ModelForm):
    address_details = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    passenger_number = forms.ModelChoiceField(queryset=Passenger.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")

    class Meta:
        model = PassengerAddress
        exclude = ("user",)

class AddPassengerBookingForm(forms.ModelForm):
    passenger_number = forms.ModelChoiceField(queryset=Passenger.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")
    flight_number = forms.ModelChoiceField(queryset=Flight.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")

    class Meta:
        model = PassengerBooking
        exclude = ("user",)

class AddPassengerPhoneForm(forms.ModelForm):
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    passenger_number = forms.ModelChoiceField(queryset=Passenger.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")

    class Meta:
        model = PassengerPhone
        exclude = ("user",)

class AddPilotTypeRatingForm(forms.ModelForm):
    type_rating = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    pilot_number = forms.ModelChoiceField(queryset=Pilot.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")
    date_earned = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control", "placeholder": "YYYY-MM-DD HH:MM:SS"}), label="")

    class Meta:
        model = PilotTypeRating
        exclude = ("user",)

class AddStaffAddressForm(forms.ModelForm):
    address_details = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    employee_number = forms.ModelChoiceField(queryset=Staff.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")

    class Meta:
        model = StaffAddress
        exclude = ("user",)

class AddStaffPhoneForm(forms.ModelForm):
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    employee_number = forms.ModelChoiceField(queryset=Staff.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")

    class Meta:
        model = StaffPhone
        exclude = ("user",)

class AddStretchForm(forms.ModelForm):
    stretch_number = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Serial Number", "class":"form-control"}), label="")
    origin_city_code = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")
    destination_city_code = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")
    flight_number = forms.ModelChoiceField(queryset=Flight.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")
    arrival_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control", "placeholder": "YYYY-MM-DD HH:MM:SS"}), label="")
    departure_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control", "placeholder": "YYYY-MM-DD HH:MM:SS"}), label="")

    class Meta:
        model = Stretch
        exclude = ("user",)
