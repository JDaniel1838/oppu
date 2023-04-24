from django.urls import path
from .views import HomePageView
from . import views

urlpatterns = [
    path('',HomePageView.as_view(),name="home"),
    path('planes/',views.planes,name="planes"),
    path('contact/',views.contact,name="contact"),
]

#path('about/',views.about,name="about"),
#path('store/',views.store,name="store"),
