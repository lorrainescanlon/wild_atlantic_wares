from django.contrib import admin
from .models import Contact, Faq


@admin.register(Contact)
class Contact(admin.ModelAdmin):

    list_display = ('created_on', 'message', 'read', 'name', )
    search_fields = ['name']
    list_filter = ('read',)


@admin.register(Faq)
class Faq(admin.ModelAdmin):

    list_display = ('title', 'body')
    search_fields = ['title']
    list_filter = ('title',)
