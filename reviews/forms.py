from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    """
    Form for submitting reviews
    """

    class Meta:
        model = Review
        fields = ['product_review', 'rating', 'experience_review']
        labels = {
            'product_view': 'Your Product Review',
            'rating': 'Rate this product out of 5',
            'experience_review': 'Feedback on your experience'
        }
        widgets = {}

