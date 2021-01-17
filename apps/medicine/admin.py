from django.contrib import admin
from .models import Medicine, Order

# Register your models here.
admin.site.register(Medicine)


class OrderDataAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'hospital', 'quantity',
                       'address', 'mobile', 'time', 'prescription')


admin.site.register(Order, OrderDataAdmin)
