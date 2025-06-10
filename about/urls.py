from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('contact', views.contact_us, name='contact'),
    path('faq', views.faq_list, name='faq'),
    path('privacy', views.privacy_policy, name='privacy'),
]
