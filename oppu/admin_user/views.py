from django.shortcuts import render
from .forms import LoginUser
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class RegisterPageView(TemplateView):
    template_name = "admin_user/register.html"

@method_decorator(login_required, name='dispatch')
class HistoryPageView(TemplateView):
    template_name = "admin_user/history.html"
