from django.shortcuts import render

# Create your views here.


def basket(request):
    """A view to return the index page"""

    return render(request, 'basket/basket.html')
