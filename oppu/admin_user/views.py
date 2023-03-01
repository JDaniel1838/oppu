from django.shortcuts import render
from .forms import LoginUser
from django.contrib.auth import authenticate

# Create your views here.
# View home
def login(request):
    login_user = LoginUser()

    if request.method == "POST":
        login_user = LoginUser(data=request.POST)

        if login_user.is_valid():
            email = login_user.cleaned_data['email'] 
            password = login_user.cleaned_data['password'] 
            print("Email: ", email)
            print("Password: ", password)

            # Buscar si un usuario existe con el email y password dados
            user = authenticate(email=email, password=password)
            if user is not None:
                print("exito")
                # Hacer algo más aquí, como redirigir al usuario a una página de inicio
            else:
                print(user)
                print("No se encontró ningún usuario con las credenciales dadas")

    return render(request,"admin_user/login.html", {'login':login_user})

def register(request):
    return render(request,"admin_user/register.html")

def history(request):
    return render(request,"admin_user/history.html")
