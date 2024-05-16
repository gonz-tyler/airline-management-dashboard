from django.contrib import admin
from.models import *
# Register your models here.
admin.site.register(Airplane)
admin.site.register(City)
admin.site.register(Flight)
admin.site.register(FlightCrew)
admin.site.register(Passenger)
admin.site.register(PassengerAddress)
admin.site.register(PassengerBooking)
admin.site.register(PassengerPhone)
admin.site.register(Pilot)
admin.site.register(PilotTypeRating)
admin.site.register(Staff)
admin.site.register(StaffAddress)
admin.site.register(StaffPhone)
admin.site.register(IntermediateCity)