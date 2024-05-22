from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),

    #-- users --#
    path('users/', UserManagement.list_users, name='list_users'),
    path('users/add/', UserManagement.add_user, name='add_user'),
    path('users/edit/<int:user_id>/', UserManagement.edit_user, name='edit_user'),
    path('users/delete/<int:user_id>/', UserManagement.delete_user, name='delete_user'),

    #-- planes --#
    path('planes/', PlaneClass.view_planes, name='view_planes'),
    path('planes/<int:serial_num>', PlaneClass.view_plane, name='view_plane'),
    path('delete_plane/<int:serial_num>', PlaneClass.delete_plane, name='delete_plane'),
    path('add_plane', PlaneClass.add_plane, name='add_plane'),
    path('update_plane/<int:serial_num>', PlaneClass.update_plane, name='update_plane'),

    #-- cities --#
    path('cities/', CityClass.view_cities, name='view_cities'),
    path('cities/<str:city_code>', CityClass.view_city, name='view_city'),
    path('delete_city/<str:city_code>', CityClass.delete_city, name='delete_city'),
    path('add_city', CityClass.add_city, name='add_city'),
    path('update_city/<str:city_code>', CityClass.update_city, name='update_city'),

    #-- flight crews --#
    #path('crews/', view_crews, name='view_crews'),
    #path('crews/<int:flight_num>/<int:employee_num>', view_crew, name='view_crew'),
    path('delete_crew/<int:flight_num>/<int:employee_num>', FlightClass.delete_crew, name='delete_crew'),
    path('add_crew/<int:flight_num>', FlightClass.add_crew, name='add_crew'),

    #-- flights --#
    path('flights/', FlightClass.view_flights, name='view_flights'),
    path('flights/<int:flight_num>', FlightClass.view_flight, name='view_flight'),
    path('delete_flight/<int:flight_num>', FlightClass.delete_flight, name='delete_flight'),
    path('add_flight', FlightClass.add_flight, name='add_flight'),
    path('update_flight/<int:flight_num>', FlightClass.update_flight, name='update_flight'),

    #-- passenger address --#
    #path('passenger_addresses/', view_passenger_addresses, name='view_passenger_addresses'),
    #path('passenger_addresses/<int:passenger_num>/<str:passenger_address>', view_passenger_address, name='view_passenger_address'),
    path('delete_passenger_address/<int:passenger_num>/<str:address>', PassengerClass.delete_passenger_address, name='delete_passenger_address'),
    path('add_passenger_address/<int:passenger_num>', PassengerClass.add_passenger_address, name='add_passenger_address'),

    #-- passenger booking --#
    #path('bookings/', view_passenger_bookings, name='view_passenger_bookings'),
    #path('bookings/<int:passenger_num>/<int:flight_num>', view_passenger_booking, name='view_passenger_booking'),
    path('delete_booking/<int:flight_num>/<int:passenger_num>', FlightClass.delete_passenger_booking, name='delete_passenger_booking'),
    path('add_booking/<int:flight_num>', FlightClass.add_passenger_booking, name='add_passenger_booking'),

    #-- passenger phone --#
    #path('passenger_phones/', view_passenger_phones, name='view_passenger_phones'),
    #path('passenger_phones/<str:phone>', view_passenger_phone, name='view_passenger_phone'),
    path('delete_passenger_phone/<str:phone>', PassengerClass.delete_passenger_phone, name='delete_passenger_phone'),
    path('add_passenger_phone/<int:passenger_num>', PassengerClass.add_passenger_phone, name='add_passenger_phone'),

    #-- passenger --#
    path('passengers/', PassengerClass.view_passengers, name='view_passengers'),
    path('passengers/<int:passenger_num>', PassengerClass.view_passenger, name='view_passenger'),
    path('delete_passenger/<int:passenger_num>', PassengerClass.delete_passenger, name='delete_passenger'),
    path('add_passenger', PassengerClass.add_passenger, name='add_passenger'),
    path('update_passenger/<int:passenger_num>', PassengerClass.update_passenger, name='update_passenger'),

    #-- pilot typeratings --#
    #path('pilot_typeratings/', view_pilot_typeratings, name='view_pilot_typeratings'),
    #path('pilot_typeratings/<int:pilot_num>/<str:typerating>', view_pilot_typerating, name='view_pilot_typerating'),
    path('delete_pilot_typerating/<int:pilotnum>/<str:typerating>', PilotClass.delete_pilot_typerating, name='delete_pilot_typerating'),
    path('add_pilot_typerating/<int:employee_num>', PilotClass.add_pilot_typerating, name='add_pilot_typerating'),

    #-- pilots --#
    path('pilots/', PilotClass.view_pilots, name='view_pilots'),
    path('pilots/<int:pilot_num>', PilotClass.view_pilot, name='view_pilot'),
    path('delete_pilot/<int:pilot_num>', PilotClass.delete_pilot, name='delete_pilot'),
    path('add_pilot', PilotClass.add_pilot, name='add_pilot'),
    path('update_pilot/<int:pilot_num>', PilotClass.update_pilot, name='update_pilot'),

    #-- staff addresses --#
    #path('staff_addresses/', view_staff_addresses, name='view_staff_addresses'),
    #path('staff_addresses/<int:employee_num>/<str:address>', view_staff_address, name='view_staff_address'),
    path('delete_staff_address/<int:employee_num>/<str:address>', StaffClass.delete_staff_address, name='delete_staff_address'),
    path('add_staff_address/<int:employee_num>', StaffClass.add_staff_address, name='add_staff_address'),

    #-- staff phones --#
    #path('staff_phones/', view_staff_phones, name='view_staff_phones'),
    #path('staff_phones/<str:phone>', view_staff_phone, name='view_staff_phone'),
    path('delete_staff_phone/<str:phone>', StaffClass.delete_staff_phone, name='delete_staff_phone'),
    path('add_staff_phone/<str:employee_num>', StaffClass.add_staff_phone, name='add_staff_phone'),
    
    #-- staff --#
    path('staff/', StaffClass.view_staff, name='view_staff'),
    path('staff/<int:employee_num>', StaffClass.view_staff_member, name='view_staff_member'),
    path('delete_staff/<int:employee_num>', StaffClass.delete_staff_member, name='delete_staff_member'),
    path('add_staff_member', StaffClass.add_staff_member, name='add_staff_member'),
    path('update_Staff_member/<int:employee_num>', StaffClass.update_staff_member, name='update_staff_member'),
    
    #-- stretch --#
    #path('stretches/', view_stretches, name='view_stretches'),
    #path('stretches/<int:stretch_num>', view_stretch, name='view_stretch'),
    path('delete_intermediate_city/<int:stretch_num>', FlightClass.delete_intermediate_city, name='delete_intermediate_city'),
    path('add_intermediate_city/<int:flight_num>', FlightClass.add_intermediate_city, name='add_intermediate_city'),

]