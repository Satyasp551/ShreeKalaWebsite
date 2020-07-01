from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('singleblog/', views.singleblog, name="singleblog"),
    path('blog/', views.blog, name="blog"),
    path('gallery/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),
]
