from django.shortcuts import render
from django.views.generic.base import TemplateView

# View home
class HomePageView(TemplateView):
    template_name = "core/home.html"

def planes(request):
    return render(request, "core/planes.html")

def contact(request):
    return render(request, "core/contact.html")
