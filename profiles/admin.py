from django.contrib import admin
from .models import UserProfile


# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'default_country',
                    'default_county',
                    'default_town_or_city',
                    )

    ordering = ('user',)


admin.site.register(UserProfile, UserProfileAdmin)
