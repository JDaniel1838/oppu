from django.shortcuts import render

# View home
def home(request):
    return render(request,"core/home.html")