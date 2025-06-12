from .models import Review
from django import forms
from checkout.models import OrderLineItem
from profiles.models import UserProfile
from products.models import Product


class ReviewForm(forms.ModelForm):
    """
    Form for submitting reviews
    """
    product = forms.ModelChoiceField(queryset=None)

    class Meta:
        model = Review
        fields = ['product', 'product_review', 'rating', 'experience_review']

        labels = {
            'product': 'Item',
            'product_view': 'Your Product Review',
            'rating': 'Rate this product out of 5',
            'experience_review': 'Feedback on your experience'
        }
        widgets = {}

    def __init__(self, profile, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        orderded_items = OrderLineItem.objects.filter(user_profile=profile)
        product_ids = orderded_items.values_list('product__id', flat=True).distinct()
        self.fields['product'].queryset = Product.objects.filter(id__in=product_ids)
