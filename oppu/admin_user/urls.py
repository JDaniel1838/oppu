from django.urls import path
from .views import RegisterPageView, HistoryPageView

#path('',views.login, name='login'),
urlpatterns = [
    path('register/', RegisterPageView.as_view(), name='register'),
    path('history/', HistoryPageView.as_view(), name='history'),
]

