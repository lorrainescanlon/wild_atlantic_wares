from .models import Review
from django import forms
from checkout.models import OrderLineItem
from profiles.models import UserProfile


class ReviewForm(forms.ModelForm):
    """
    Form for submitting reviews
    """
    product = forms.ModelChoiceField(queryset=None)

    def __init__(self, profile, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        self.fields['product'].queryset = OrderLineItem.objects.filter(
                                        user_profile=profile)

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
