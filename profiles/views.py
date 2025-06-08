from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


def profile(request):
    """ Display the user's profile"""
    profile = get_object_or_404(UserProfile, user=request.user)
    profile_name = request.user
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'profile_name': profile_name
    }

    return render(request, template, context)

def profile_orders(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    profile_name = request.user
    orders = profile.orders.all()

    template = 'profiles/orders.html'
    context = {
        'orders': orders,
        'on_profile_page': True,
        'profile_name': profile_name
    }

    return render(request, template, context)

    
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))
    
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def update_profile(request):
    if request.method == "POST":
        profile = UserProfile.objects.get(user=request.user)
        update_form = UserProfileForm(data=request.POST, instance=profile)
       
        if update_form.is_valid():
            profile.save()

        #template = 'profiles/profile.html'
            messages.add_message(
                request, messages.SUCCESS,
                'Profile Updated'
            )
        else:
            messages.add_message(
                request, messages.Error,
                'Profile update failed. Please ensure form fields are valid.'
            )
            
    return HttpResponseRedirect(reverse('profile'))
    #return render(request, template)
