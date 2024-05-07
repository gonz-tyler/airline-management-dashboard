from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    #-- planes --#
    path('planes/', views.view_planes, name='view_planes'),
    path('planes/<int:pk>', views.view_plane, name='view_plane'),
    path('delete_plane/<int:pk>', views.delete_plane, name='delete_plane'),
    path('add_plane', views.add_plane, name='add_plane'),

    #-- cities --#
    path('cities/', views.view_cities, name='view_cities'),
    path('cities/<str:pk>', views.view_city, name='view_city'),
    path('delete_city/<str:pk>', views.delete_city, name='delete_city'),
    path('add_city', views.add_city, name='add_city'),

    #-- flight crews --#
    path('crews/', views.view_crews, name='view_crews'),
    path('crews/<int:pk>', views.view_crew, name='view_crew'),
    path('delete_crew/<int:pk>', views.delete_crew, name='delete_crew'),
    path('add_crew', views.add_crew, name='add_crew'),

    #-- flights --#
    path('flights/', views.view_flights, name='view_flights'),
    path('flights/<int:pk>', views.view_flight, name='view_flight'),
    path('delete_flight/<int:pk>', views.delete_flight, name='delete_flight'),
    path('add_flight', views.add_flight, name='add_flight'),

    #-- passenger address --#
    path('passenger_addresses/', views.view_passenger_addresses, name='view_passenger_addresses'),
    path('passenger_addresses/<int:pk>', views.view_passenger_address, name='view_passenger_address'),
    path('delete_passenger_address/<int:pk>', views.delete_passenger_address, name='delete_passenger_address'),
    path('add_passenger_address', views.add_passenger_address, name='add_passenger_address'),

    #-- passenger booking --#
    path('pilots/', views.view_pilots, name='view_pilots'),
    path('pilots/<int:pk>', views.view_pilot, name='view_pilot'),
    path('delete_pilot/<int:pk>', views.delete_pilot, name='delete_pilot'),
    path('add_pilot', views.add_pilot, name='add_pilot'),

    #-- passenger phone --#
    path('passenger_phones/', views.view_passenger_phones, name='view_passenger_phones'),
    path('passenger_phones/<int:pk>', views.view_passenger_phone, name='view_passenger_phone'),
    path('delete_passenger_phone/<int:pk>', views.delete_passenger_phone, name='delete_passenger_phone'),
    path('add_passenger_phone', views.add_passenger_phone, name='add_passenger_phone'),

    #-- passenger --#
    path('passengers/', views.view_passengers, name='view_passengers'),
    path('passengers/<int:pk>', views.view_passenger, name='view_passenger'),
    path('delete_passenger/<int:pk>', views.delete_passenger, name='delete_passenger'),
    path('add_passenger', views.add_passenger, name='add_passenger'),

    #-- pilot typeratings --#
    path('pilot_typeratings/', views.view_pilot_typeratings, name='view_pilot_typeratings'),
    path('pilot_typeratings/<int:pk>', views.view_pilot_typerating, name='view_pilot_typerating'),
    path('delete_pilot_typerating/<int:pk>', views.delete_pilot_typerating, name='delete_pilot_typerating'),
    path('add_pilot_typerating', views.add_pilot_typerating, name='add_pilot_typerating'),

    #-- pilots --#
    path('pilots/', views.view_pilots, name='view_pilots'),
    path('pilots/<int:pk>', views.view_pilot, name='view_pilot'),
    path('delete_pilot/<int:pk>', views.delete_pilot, name='delete_pilot'),
    path('add_pilot', views.add_pilot, name='add_pilot'),

    #-- staff addresses --#
    path('staff_addresses/', views.view_staff_addresses, name='view_staff_addresses'),
    path('staff_addresses/<int:pk>', views.view_staff_address, name='view_staff_address'),
    path('delete_staff_address/<int:pk>', views.delete_staff_address, name='delete_staff_address'),
    path('add_staff_address', views.add_staff_address, name='add_staff_address'),

    #-- staff phones --#
    path('staff_phones/', views.view_staff_phones, name='view_staff_phones'),
    path('staff_phones/<int:pk>', views.view_staff_phone, name='view_staff_phone'),
    path('delete_staff_phone/<int:pk>', views.delete_staff_phone, name='delete_staff_phone'),
    path('add_staff_phone', views.add_staff_phone, name='add_staff_phone'),
    
    #-- staff --#
    path('staff/', views.view_staff, name='view_staff'),
    path('staff/<int:pk>', views.view_staff_member, name='view_staff_members'),
    path('delete_staff/<int:pk>', views.delete_staff_member, name='delete_staff'),
    path('add_staff', views.add_staff_member, name='add_staff'),
    
    #-- stretch --#
    path('stretches/', views.view_stretches, name='view_stretches'),
    path('stretches/<int:pk>', views.view_stretch, name='view_stretch'),
    path('delete_stretch/<int:pk>', views.delete_stretch, name='delete_stretch'),
    path('add_stretch', views.add_stretch, name='add_stretch'),

]