from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('privacy', views.privacy, name='privacy'),
]
