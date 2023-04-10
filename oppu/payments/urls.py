from django.urls import path
from .views import ExportPDFView

urlpatterns = [
    path('', ExportPDFView.as_view(), name="report" )
]
