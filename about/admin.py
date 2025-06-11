from django.contrib import admin
from .models import Contact, Faq
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Contact)
class Contact(admin.ModelAdmin):

    list_display = ('created_on', 'message', 'read', 'name', )
    search_fields = ['name']
    list_filter = ('read',)


@admin.register(Faq)
class Faq(SummernoteModelAdmin):

    list_display = ('title', 'body')
    search_fields = ['title']
    list_filter = ('title',)
    summernote_fields = ('body',)
