from django.contrib import admin

# Register your models here.
from .models import Month, State, Payment
from django.forms import FileInput
from django.db import models

class MonthAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

class StateAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

class PaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    #Cambie el label de tabla de ultima actualizacón -> fecha de pago
    def payment_date(self, obj):
        return obj.updated
    payment_date.short_description = 'Fecha de pago'

    list_display= ('state','month', 'payment_date', 'name_client_full_name',) 

    #Ocultar checkbox
    actions_selection_counter = False

    #Evitar que eliminen comprobante - pero no se puede visualizar al editar el pago
    #formfield_overrides = {
    #     models.FileField: {'widget': FileInput(attrs={'accept': 'image/*', 'can_delete': False})}
    #}

    #Retorna el nombre completo
    def name_client_full_name(self, obj):
        return obj.name_client.get_full_name()
    name_client_full_name.admin_order_field = 'name_client__last_name'
    name_client_full_name.short_description = 'Nombre completo del cliente'

admin.site.register(Month, MonthAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Payment, PaymentAdmin)