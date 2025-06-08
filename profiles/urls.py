from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('profile_orders', views.profile_orders, name='profile_orders'),
]
