from django.contrib import admin
from .models import Property, Owner


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'ordered_date')


admin.site.register(Property)
admin.site.register(Owner)
