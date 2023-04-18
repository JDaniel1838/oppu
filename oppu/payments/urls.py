from django.urls import path
from .views import ExportPDFView,ErrorWithPDF

urlpatterns = [
    path('', ExportPDFView.as_view(), name="report" ),
    path('error/', ErrorWithPDF.as_view(), name="error" )
]
