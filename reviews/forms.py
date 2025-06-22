from .models import Review
from django import forms
from checkout.models import OrderLineItem
from products.models import Product
from profiles.models import UserProfile


class ReviewForm(forms.ModelForm):
    """
    Form for submitting reviews
    """
    product = forms.ModelChoiceField(
        queryset=None,
        required=True,
        empty_label="-- Select your purchased item --",
        label='Item',
    )

    class Meta:
        model = Review
        fields = ['product', 'product_review', 'rating', 'experience_review']

        labels = {
            'product': 'Item',
            'product_review': 'Your Item Review',
            'rating': 'Rate this item out of 5',
            'experience_review': 'Feedback on your experience'
        }
        widgets = {}

    def __init__(self, profile, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        """
        orderded_items = OrderLineItem.objects.filter(user_profile=profile)
        product_ids = orderded_items.values_list('product__id',
                                                 flat=True).distinct()
        """
        orderded_items = OrderLineItem.objects.filter(
            order__user_profile=profile)
        product_ids = orderded_items.values_list(
            'product__id', flat=True).distinct()

        self.fields['product'].queryset = Product.objects.filter(
            id__in=product_ids)
