from django.db import models
from products.models import Product
from checkout.models import Order, OrderLineItem
from profiles.models import UserProfile
from django.contrib.auth.models import User

RATING = ((5, "5 *"), (4, "4 *"), (3, "3 *"), (2, "2 *"), (1, "1 *"),
          (0, "0 *"))


class Review(models.Model):
    """
    A model to create and manage marproduct reviews
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="reviews")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                             related_name="reviewer")
    product_review = models.TextField(max_length=400)
    experience_review = models.TextField(max_length=400)
    rating = models.IntegerField(choices=RATING, default=5)
    approved = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.product} {self.rating} \
            review by {self.user} * on {self.created_on}"
