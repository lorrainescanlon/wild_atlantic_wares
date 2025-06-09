from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from reviews.models import Review
from reviews.forms import ReviewForm
from products.models import Product


def profile(request):
    """ Display the user's profile"""
    profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure your form data is valid')
    else:
        form = UserProfileForm(instance=profile)
    
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'profile_name': profile
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

    template = 'profiles/order_summary.html'
    #template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def profile_reviews(request):
    profile = UserProfile.objects.get(user=request.user)
    form = ReviewForm(profile)

    template = 'profiles/reviews.html'
    context = {
        'form': form,
        'from_profile': True,
    }

    return render(request, template, context)


def submit_review(request):
    if request.method == "POST":
        profile = UserProfile.objects.get(user=request.user)
        review_form = ReviewForm(data=request.POST, profile=profile)
        if review_form.is_valid():

            review = review_form.save(commit=False)
            review.user = profile
            review.save()

            messages.add_message(
                request, messages.SUCCESS,
                'Thank you for your review!'
            )
        else:
            messages.add_message(
                request, messages.Error,
                'Review submission failed. Please ensure form fields are valid.'
            )

    return HttpResponseRedirect(reverse('profile'))


def update_profile(request):
    if request.method == "POST":
        profile = UserProfile.objects.get(user=request.user)
        update_form = UserProfileForm(data=request.POST, instance=profile)

        if update_form.is_valid():
            profile.save()

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
