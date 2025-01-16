from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('gallery', views.gallery, name='gallery'), 
    path('contact/',views.contact,name='contact'),
    path('success/',views.success,name='success')

]