from django.shortcuts import render


def about(request):
    """A view to return the about page"""

    return render(request, 'about/about.html')


def contact(request):
    """A view to return the contact page"""

    return render(request, 'about/contact.html')


def faq(request):
    """A view to return the faq page"""

    return render(request, 'about/faq.html')


def privacy(request):
    """A view to return the privacy policy page"""

    return render(request, 'about/privacy.html')
