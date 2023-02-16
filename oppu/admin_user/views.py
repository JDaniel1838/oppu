from django.shortcuts import render
from .forms import LoginUser

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



    return render(request,"admin_user/login.html", {'login':login_user})
