from django import forms
from payments.models import Payment

class LoginUser(forms.Form):
    email = forms.EmailField(min_length=3,max_length=100, required=True,
        widget=forms.TextInput(attrs={'placeholder':'Correo electrónico...','class':'form-control mb-2', 'aria-describedby':'emailHelp', 'id':'email-user'}))
    password = forms.CharField(min_length=3,max_length=100, required=True, 
        widget=forms.PasswordInput(attrs={'placeholder':'Contraseña...','class':'form-control mb-2', 'id':'password-user', 'aria-describedby':'passwordHelpBlock'}))

#class PaymentForm(forms.ModelForm):
#    class Meta:
#        model = Payment
#        fields = '__all__'

class PaymentForm(forms.Form):
    #MONTH_CHOICES = (('', 'Seleccione mes de pago'),)
    #month = forms.ChoiceField(choices=MONTH_CHOICES, widget=forms.Select(attrs={'class': 'form-select', 'required': True, 'id':'user-month-payment'}))
    
    receipt = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control custom-file-input', 'id': 'user-form-file', 'required': True}))