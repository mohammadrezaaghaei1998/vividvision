from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'), 
    path('contactus', views.contactus, name='contactus'), 
    path('service', views.service, name='service'), 
    path('gallery', views.gallery, name='gallery'), 
    path('contact/',views.contact,name='contact'),
    path('success/',views.success,name='success')

]