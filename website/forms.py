from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import inlineformset_factory
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
    SERIALNUM = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Serial Number", "class":"form-control"}), label="")
    MANUFACTURER = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Manufacturer", "class":"form-control"}), label="")
    MODEL = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Model", "class":"form-control"}), label="")

    class Meta:
        model = Airplane
        exclude = ("user",)

class AddCityForm(forms.ModelForm):
    CITYCODE = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Airport Code", "class":"form-control"}), label="")
    CITYNAME = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City Name", "class":"form-control"}), label="")

    class Meta:
        model = City
        exclude = ("user",)

class AddStaffForm(forms.ModelForm):
    EMPNUM = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Employee Number", "class":"form-control"}), label="")
    SURNAME = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    NAME = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    SALARY = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Salary", "class":"form-control"}), label="")
    type_choices = (('Pilot', 'Pilot'),('Crew', 'Crew'),)
    TYPE = forms.ChoiceField(required=True,choices=type_choices,widget=forms.Select(attrs={"class": "form-control"}),label="")
    pilotnum = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={"placeholder": "Pilot Number", "class": "form-control"}), label="")

    class Meta:
        model = Staff
        exclude = ("user",)

    def clean(self):
        cleaned_data = super().clean()
        staff_type = cleaned_data.get('TYPE')
        pilotnum = cleaned_data.get('pilotnum')

        if staff_type == 'Pilot' and not pilotnum:
            self.add_error('pilotnum', 'Pilot number is required for Pilots.')
        return cleaned_data

class AddPilotForm(forms.ModelForm):
    PILOTNUM = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Pilot Number", "class":"form-control"}), label="")
    pilot_choices = Staff.objects.filter(TYPE='Pilot')
    EMPNUM = forms.ModelChoiceField(queryset=pilot_choices, widget=forms.Select(attrs={"class": "form-control"}), label="")

    class Meta:
        model = Pilot
        exclude = ("user",)

class AddFlightForm(forms.ModelForm):
    FLIGHTNUM = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Flight Number", "class":"form-control"}), label="")
    ORIGINCITYCODE = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")
    DESTCITYCODE = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")
    DEPTIME = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control", "placeholder": "YYYY-MM-DD HH:MM:SS"}), label="")
    ARRTIME = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control", "placeholder": "YYYY-MM-DD HH:MM:SS"}), label="")
    PILOTNUM = forms.ModelChoiceField(queryset=Pilot.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")
    PLANENUM = forms.ModelChoiceField(queryset=Airplane.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")

    class Meta:
        model = Flight
        exclude = ("user",)

class AddFlightCrewForm(forms.ModelForm):
    FLIGHTNUM = forms.ModelChoiceField(queryset=Flight.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")
    crew_choices = Staff.objects.filter(TYPE='Crew')
    EMPNUM = forms.ModelChoiceField(queryset=crew_choices, widget=forms.Select(attrs={"class": "form-control"}), label="")

    class Meta:
        model = FlightCrew
        exclude = ("user",)

class AddPassengerForm(forms.ModelForm):
    PASSENGERNUM = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Passenger Number", "class":"form-control"}), label="")
    SURNAME = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    NAME = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")

    class Meta:
        model = Passenger
        exclude = ("user",)

class AddPassengerAddressForm(forms.ModelForm):
    ADDRESSDETAILS = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
    #PASSENGERNUM = forms.ModelChoiceField(queryset=Passenger.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")

    class Meta:
        model = PassengerAddress
        exclude = ("user","PASSENGERNUM")


class AddPassengerPhoneForm(forms.ModelForm):
    PHONE = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone Number", "class":"form-control"}), label="")
    #PASSENGERNUM = forms.ModelChoiceField(queryset=Passenger.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")

    class Meta:
        model = PassengerPhone
        exclude = ("user","PASSENGERNUM")

# Create formsets using the inlineformset_factory
PassengerAddressFormSet = inlineformset_factory(Passenger, PassengerAddress, form=AddPassengerAddressForm, extra=1)
PassengerPhoneFormSet = inlineformset_factory(Passenger, PassengerPhone, form=AddPassengerPhoneForm, extra=1)

class AddPassengerBookingForm(forms.ModelForm):
    PASSENGERNUM = forms.ModelChoiceField(queryset=Passenger.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")
    FLIGHTNUM = forms.ModelChoiceField(queryset=Flight.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")

    class Meta:
        model = PassengerBooking
        exclude = ("user",)

class AddPilotTypeRatingForm(forms.ModelForm):
    TYPERATING = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Type Rating", "class":"form-control"}), label="")
    PILOTNUM = forms.ModelChoiceField(queryset=Pilot.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")
    DATEEARNED = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control", "placeholder": "YYYY-MM-DD HH:MM:SS"}), label="")

    class Meta:
        model = PilotTypeRating
        exclude = ("user",)

class AddStaffAddressForm(forms.ModelForm):
    ADDRESSDETAILS = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
    #EMPNUM = forms.ModelChoiceField(queryset=Staff.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")

    class Meta:
        model = StaffAddress
        exclude = ("user","EMPNUM")

class AddStaffPhoneForm(forms.ModelForm):
    PHONE = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone Number", "class":"form-control"}), label="")
    #EMPNUM = forms.ModelChoiceField(queryset=Staff.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")

    class Meta:
        model = StaffPhone
        exclude = ("user","EMPNUM")

# Create formsets using the inlineformset_factory
StaffAddressFormSet = inlineformset_factory(Staff, StaffAddress, form=AddStaffAddressForm, extra=1)
StaffPhoneFormSet = inlineformset_factory(Staff, StaffPhone, form=AddStaffPhoneForm, extra=1)

class AddStretchForm(forms.ModelForm):
    STRETCHNUM = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Serial Number", "class":"form-control"}), label="")
    ORIGINCITYCODE = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")
    DESTCITYCODE = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")
    FLIGHTNUM = forms.ModelChoiceField(queryset=Flight.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="")
    ARRTIME = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control", "placeholder": "YYYY-MM-DD HH:MM:SS"}), label="")
    DEPTIME = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control", "placeholder": "YYYY-MM-DD HH:MM:SS"}), label="")

    class Meta:
        model = Stretch
        exclude = ("user",)
