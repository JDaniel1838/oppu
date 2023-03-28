from django.shortcuts import render
from .forms import LoginUser
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from payments.models import Payment
import json
from django.forms.models import model_to_dict



@method_decorator(login_required, name='dispatch')
class RegisterPageView(TemplateView):
    template_name = "admin_user/register.html"



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

    
