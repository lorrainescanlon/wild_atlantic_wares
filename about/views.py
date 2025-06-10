from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect


def about(request):
    """A view to return the about page"""

    return render(request, 'about/about.html')


def contact_us(request):
    """A view to return the contact page"""

    return render(request, 'about/contact.html')


def faq_list(request):
    """A view to return the faq page"""

    return render(request, 'about/faq.html')


def privacy_policy(request):
    """A view to return the privacy policy page"""

    return render(request, 'about/privacy.html')
