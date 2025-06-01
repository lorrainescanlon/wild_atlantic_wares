from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from basket.contexts import basket_contents
import stripe


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is currently empty")
        return redirect(reverse('products'))

    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form
    }

    return render(request, template, context)
