from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def basket(request):
    """A view to return the basket contents page"""

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified item to the shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket

    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Update quantity of the specified item in the shopping basket """

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket

    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ Delete item from the shopping basket """
    try:
        basket = request.session.get('basket', {})

        basket.pop(item_id)

        request.session['basket'] = basket

        return HttpResponse(status=200)
    
    except Exception as e:
        return HttpResponse(status=500)
