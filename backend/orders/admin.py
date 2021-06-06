from django.contrib import admin
from .models import Order, Courier


admin.site.site_title = "Управление ресурсами DocDelivery"
admin.site.site_header = "Админпанель DocDelivery"
admin.site.index_title = "Управление ресурсами"

admin.site.register(Order)
admin.site.register(Courier)
