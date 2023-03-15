from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('',HomePageView.as_view(),name="home"),
]

#path('about/',views.about,name="about"),
#path('store/',views.store,name="store"),
