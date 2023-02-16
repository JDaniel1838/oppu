from django import forms

class LoginUser(forms.Form):
    email = forms.EmailField(min_length=3,max_length=100, required=True,
        widget=forms.TextInput(attrs={'placeholder':'Correo electrónico...','class':'form-control mb-2', 'aria-describedby':'emailHelp', 'id':'email-user'}))
    password = forms.CharField(min_length=3,max_length=100, required=True, 
        widget=forms.PasswordInput(attrs={'placeholder':'Contraseña...','class':'form-control mb-2', 'id':'password-user', 'aria-describedby':'passwordHelpBlock'}))