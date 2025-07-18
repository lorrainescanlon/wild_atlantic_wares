from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInine(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderLineItemAdmin(admin.ModelAdmin):
    readonly_fields = ('order', 'product', 'quantity')

    list_display = ('order', 'product', 'quantity')


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInine,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    fields = ('order_number', 'user_profile', 'full_name', 'date',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'address1',
              'address2', 'county', 'delivery_cost',
              'order_total', 'grand_total',)

    list_display = ('order_number', 'full_name', 'date',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLineItem, OrderLineItemAdmin)
