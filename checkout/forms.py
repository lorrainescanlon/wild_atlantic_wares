from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'address1', 'address2', 'town_or_city',
                  'county', 'postcode', 'country',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders remove lables and autofocus on full_name field
        """
        super().__init__(*args, **kwargs)

        self.fields['full_name'].widget.attrs['autofocus'] = True
        self.fields['full_name'].widget.attrs['placeholder'] = 'Full Name*'
        self.fields['email'].widget.attrs['placeholder'] = 'Email*'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Telephone*'
        self.fields['address1'].widget.attrs['placeholder'] = 'Street Address*'
        self.fields['address2'].widget.attrs['placeholder'] = 'Sreet Address 2'
        self.fields['town_or_city'].widget.attrs['placeholder'] = 'Town/City*'
        self.fields['county'].widget.attrs['placeholder'] = 'County'
        self.fields['postcode'].widget.attrs['placeholder'] = 'Postcode'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
