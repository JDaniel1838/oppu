from django.contrib import admin

# Register your models here.
from .models import Month, State, Payment

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

    #Retorna el nombre completo
    def name_client_full_name(self, obj):
        return obj.name_client.get_full_name()
    name_client_full_name.admin_order_field = 'name_client__last_name'
    name_client_full_name.short_description = 'Nombre completo del cliente'

    list_filter = ('state','month') # Agregado para filtrar por estado
    search_fields = ['name_client__last_name','name_client__first_name'] # Agregado para buscar por usuario
    list_per_page = 10 #10 register for view
    list_max_show_all = 200 # mostrar solo si hay mas de 200

    class Media:
        js = ('core/js/main.js',)
        css = {'all': ('core/css/admin.css',)}

admin.site.register(Month, MonthAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Payment, PaymentAdmin)