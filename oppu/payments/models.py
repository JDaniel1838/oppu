from django.db import models
from django.contrib.auth.models import User
from django import forms


# MES DE PAGO.
class Month(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, 
        verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "mes"
        verbose_name_plural="meses"

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, 
        verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "estado"
        verbose_name_plural="estados"

    def __str__(self):
        return self.name
    
class Payment(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de pago")
    updated = models.DateTimeField(auto_now=True, verbose_name="Ultima modificación")
    receipt = models.FileField(upload_to="comprobantes", null=True, blank=True, verbose_name="Comprobante")
    name_client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Nombre del cliente")
    email_client = models.EmailField(max_length=254,verbose_name="Correo electrónico del cliente", null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name="Estado")
    month = models.ForeignKey(Month, on_delete=models.CASCADE, verbose_name="Mes de pago")

    class Meta:
        verbose_name = "pago"
        verbose_name_plural="pagos"

    def __str__(self):
        return f"{self.name_client.get_full_name().split()[0]} - {self.id}"

    @staticmethod
    def get_user_emails():
        return [(email, email) for email in User.objects.values_list('email', flat=True)]

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['email_client', 'email_client',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email_client'].choices = self.instance.get_user_emails()


    #def __str__(self):
    #    return f"{self.name_client.get_full_name()} - {self.id}"


