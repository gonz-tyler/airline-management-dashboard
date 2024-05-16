from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Airplane(models.Model):
    SERIALNUM = models.IntegerField(primary_key=True)
    MANUFACTURER = models.CharField(max_length=10)
    MODEL = models.CharField(max_length=10)

class City(models.Model):
    CITYCODE = models.CharField(max_length=4, primary_key=True)
    CITYNAME = models.CharField(max_length=20)

class Staff(models.Model):
    EMPNUM = models.IntegerField(primary_key=True)
    SURNAME = models.CharField(max_length=30)
    NAME = models.CharField(max_length=20)
    SALARY = models.DecimalField(max_digits=10, decimal_places=2)
    TYPE = models.CharField(max_length=10)
    
    def clean(self):
        if self.TYPE not in ['Crew', 'Pilot']:
            raise ValidationError(_('Staff type must be "Crew" or "Pilot".'))

    def save(self, *args, **kwargs):
        self.full_clean()  # Ensure clean is called before saving
        super().save(*args, **kwargs)

class Pilot(models.Model):
    PILOTNUM = models.IntegerField(primary_key=True)
    EMPNUM = models.ForeignKey(Staff, on_delete=models.CASCADE)

class Flight(models.Model):
    FLIGHTNUM = models.IntegerField(primary_key=True)
    ORIGINCITYCODE = models.ForeignKey(City, on_delete=models.CASCADE, related_name='origin_flights')
    DESTCITYCODE = models.ForeignKey(City, on_delete=models.CASCADE, related_name='destination_flights')
    DEPTIME = models.DateTimeField()
    ARRTIME = models.DateTimeField()
    PILOTNUM = models.ForeignKey(Pilot, on_delete=models.CASCADE, related_name='pilot_flights')
    PLANENUM = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name='airplane_flights')

class FlightCrew(models.Model):
    FLIGHTNUM = models.ForeignKey(Flight, on_delete=models.CASCADE)
    EMPNUM = models.ForeignKey(Staff, on_delete=models.CASCADE, limit_choices_to={'TYPE': 'Crew'})
    class Meta:
        unique_together = (('FLIGHTNUM', 'EMPNUM'),)

class Passenger(models.Model):
    PASSENGERNUM = models.IntegerField(primary_key=True)
    SURNAME = models.CharField(max_length=30)
    NAME = models.CharField(max_length=20)

class PassengerAddress(models.Model):
    ADDRESSDETAILS = models.CharField(max_length=50)
    PASSENGERNUM = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('PASSENGERNUM', 'ADDRESSDETAILS'),)

class PassengerBooking(models.Model):
    PASSENGERNUM = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    FLIGHTNUM = models.ForeignKey(Flight, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('PASSENGERNUM', 'FLIGHTNUM'),)

class PassengerPhone(models.Model):
    PHONE = models.CharField(max_length=15, primary_key=True)
    PASSENGERNUM = models.ForeignKey(Passenger, on_delete=models.CASCADE)



class PilotTypeRating(models.Model):
    TYPERATING = models.CharField(max_length=20)
    PILOTNUM = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    DATEEARNED = models.DateTimeField()
    class Meta:
        unique_together = (('TYPERATING', 'PILOTNUM'),)



class StaffAddress(models.Model):
    ADDRESSDETAILS = models.CharField(max_length=50)
    EMPNUM = models.ForeignKey(Staff, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('EMPNUM', 'ADDRESSDETAILS'),)

class StaffPhone(models.Model):
    PHONE = models.CharField(max_length=15, primary_key=True)
    EMPNUM = models.ForeignKey(Staff, on_delete=models.CASCADE)

class IntermediateCity(models.Model):
    STRETCHNUM = models.AutoField(primary_key=True)
    INTERMEDIATECITYCODE = models.ForeignKey(City, on_delete=models.CASCADE, related_name='intermediate_stretch_city')
    #DESTCITYCODE = models.ForeignKey(City, on_delete=models.CASCADE, related_name='destination_stretches')
    FLIGHTNUM = models.ForeignKey(Flight, on_delete=models.CASCADE)
    ARRTIME = models.DateTimeField()
    DEPTIME = models.DateTimeField()
