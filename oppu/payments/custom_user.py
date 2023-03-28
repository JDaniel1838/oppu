#En este archivo añadir un método para mostrar el email del usuario en el panel de administrador

from django.contrib.auth.models import User

def user_str(self):
    return self.email

User.add_to_class("__str__", user_str)
