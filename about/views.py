from django.shortcuts import render
from django.contrib import messages
from .models import Faq
from .forms import ContactForm


def about(request):
    """A view to return the about page"""

    return render(request, 'about/about.html')


def contact_us(request):
    """A view to return the contact page"""
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Contact form recieved! '
                'We appreciate your feedback & will be in contact shortly.')

    contact_form = ContactForm()
    context = {
        'form': contact_form,
    }

    return render(request, 'about/contact.html', context,)


def faq_list(request):
    """A view to return the faq page"""
    faqs = Faq.objects.all()

    context = {
        'faqs': faqs,
    }

    return render(request, 'about/faq.html', context,)


def privacy_policy(request):
    """A view to return the privacy policy page"""

    return render(request, 'about/privacy.html')
