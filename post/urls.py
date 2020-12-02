from django.urls import path
from .views import home, about, contact, details

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('details/<int:pk>', details, name='details')
]
