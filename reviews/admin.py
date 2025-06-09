from django.contrib import admin
from .models import Review


# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'created_on',
        'rating',
        'product_review',
        'experience_review',
        'user',
        'approved',
    )

    ordering = ('product',)


admin.site.register(Review, ReviewAdmin)
