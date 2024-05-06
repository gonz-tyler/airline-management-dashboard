from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('planes/', views.view_planes, name='view_planes'),
    path('planes/<int:pk>', views.view_plane, name='view_plane'),
    path('delete_plane/<int:pk>', views.delete_plane, name='delete_plane'),
    path('flights/', views.view_flights, name='view_flights'),
    path('flights/<int:pk>', views.view_flight, name='view_flight'),
    path('delete_flight/<int:pk>', views.delete_flight, name='delete_flight'),

    path('cities/', views.view_cities, name='view_cities'),
    path('cities/<str:pk>', views.view_city, name='view_city'),
    path('pilots/', views.view_pilots, name='view_pilots'),
    path('pilots/<int:pk>', views.view_pilot, name='view_pilot'),

]