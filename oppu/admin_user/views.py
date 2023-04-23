from django.shortcuts import render
from .forms import LoginUser
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from payments.models import Payment, State, Month
from .forms import PaymentForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

MONTHS = {
    "1": "ENERO",
    "2": "FEBRERO",
    "3": "MARZO",
    "4": "ABRIL",
    "5": "MAYO",
    "6": "JUNIO",
    "7": "JULIO",
    "8": "AGOSTO",
    "9": "SEPTIEMBRE",
    "10": "OCTUBRE",
    "11": "NOVIEMBRE",
    "12": "DICIEMBRE"
}

ERROR_MONTH_REPEAT = False
ERROR_OTHER = False



@method_decorator(login_required, name='dispatch')
class RegisterPageView(FormView):
    template_name = "admin_user/register.html"
    form_class = PaymentForm
    success_url = reverse_lazy("history")

    def get_form(self, form_class=None):
        global ERROR_MONTH_REPEAT
        ERROR_MONTH_REPEAT = False
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(**self.get_form_kwargs())
    
    # Añadir parametro a url para mostrar mensaje a usuario
    def get_success_url(self):
        return reverse_lazy('history') + '?new_payment'

    def form_valid(self, form):
        month_name = MONTHS[self.request.POST.get('month')]
        month = Month.objects.get(name=month_name)
        receipt_file = self.request.FILES.get('receipt')
        name_client = self.request.user
        state = State.objects.get(name="PENDIENTE")
        email = self.request.user.email

        payment = Payment.objects.filter(name_client=name_client, month=month).first()
        if payment:
            global ERROR_MONTH_REPEAT
            ERROR_MONTH_REPEAT = True#Condicional para mandar error a vista
            form.add_error(None, f"Ya existe un pago registrado para el mes de {month_name}.")
            return self.form_invalid(form)

        payment = Payment(
            month=month, 
            receipt=receipt_file,
            name_client=name_client,
            email_client=email,
            state=state,
        )
        payment.save()
        print("Todo correcto ...")
        return super().form_valid(form)

    

    def form_invalid(self, form):
        print("---NUEVO PAGO EN PROGRESO ERROR---")

        print(self.request.user)
        print(State.objects.get(name="PENDIENTE"))
        print(self.request.user.email)
        print(Month.objects.get(name=MONTHS[self.request.POST.get('month')]))
        print(form.errors)
        print(ERROR_MONTH_REPEAT)


        context = {
            'form': form,
        }

        #Mes repetido
        if ERROR_MONTH_REPEAT:
            context = {
                'form': form,
                'error': f"Ya existe un pago registrado para el mes de <b>{MONTHS[self.request.POST.get('month')]}</b>.",
            }   

        #Cualquier otro error
        if ERROR_MONTH_REPEAT == False:
            context = {
                'form': form,
                'other_error': f"Ha ocurrido un error inesperado, vuelve a intentarlo más tarde o reportelo a <b>correo@contacto.com</b>.",
            }  


        return render(self.request, self.template_name, context)
    





@method_decorator(login_required, name='dispatch')
class HistoryPageView(TemplateView):
    template_name = "admin_user/history.html"

    def get_queryset(self):
        queryset = Payment.objects.filter(name_client=self.request.user)
        queryset = queryset.order_by('-month') # ordena por fecha de creación descendente: -month = de forma ascendente 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['payments'] = self.get_queryset()
        return context







    """ CODIGO PARA VER ID EN CMD
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        payments = Payment.objects.filter(name_client=self.request.user)
        payments_dict = [self.payment_to_dict(payment) for payment in payments]
        context['payments'] = json.dumps(payments_dict)


        payments = Payment.objects.filter(name_client=self.request.user)
        payment_list = []
        for payment in payments:
            payment_dict = model_to_dict(payment)
            payment_dict['receipt'] = str(payment_dict['receipt'])
            payment_list.append(payment_dict)
            print(payment_dict['created'])
        return context

    def payment_to_dict(self, payment):
        payment_dict = model_to_dict(payment)
        payment_dict['receipt'] = str(payment_dict['receipt'])  # Convert FieldFile to string
        return payment_dict"""
    

#Redireccionar al usuario dependiendo de sus permisos
"""
class AdminLoginRedirectView(View):
    def get(self, request):
        if request.user.is_superuser:
            # Redirigir a la URL deseada para los usuarios administradores
            return redirect('admin/payments/payment/')
        else:
            # Redirigir a la URL predeterminada para los otros usuarios
            return redirect('register')
"""
