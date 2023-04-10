from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views import View
from weasyprint import HTML
from django.conf import settings
import datetime
from .models import Payment, Month, State
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

@method_decorator(staff_member_required, name='dispatch')
class ExportPDFView(View):

    def get(self, request):
        month_id_exact = request.GET.get('month__id__exact')
        state__id__exact = request.GET.get('state__id__exact')
        
        if month_id_exact and state__id__exact:
            state = State.objects.get(id=state__id__exact)
            month = Month.objects.get(id=month_id_exact)
            print("Mes y estado")
            title = f"PAGOS DE {month.name} CON ESTADO '{state.name}'"
            payments = Payment.objects.filter(state=state, month=month).select_related('name_client')
        elif state__id__exact:
            print("Solo estado")
            state = State.objects.get(id=state__id__exact)
            title = f"PAGOS CON ESTADO '{state.name}'"
            payments = Payment.objects.filter(state=state).select_related('name_client')
        elif month_id_exact:
            print("Solo mes")
            month = Month.objects.get(id=month_id_exact)
            title = f"PAGOS DE {month.name}"
            payments = Payment.objects.filter(month=month).select_related('name_client')

        image_url = request.scheme + '://' + request.META['HTTP_HOST'] + settings.MEDIA_URL + 'images/logo_sion.png'
        fecha_actual = datetime.date.today()
        context = {
            'image_path': image_url,
            'date': fecha_actual.strftime("%d/%m/%Y"),
            'title':title,
            'payments': [{
                'name_client': f"{p.name_client.get_full_name()}",
                'state':p.state,
                'month': p.month,
                'updated': p.updated,
            } for p in payments],
            
        }
        
        html = render_to_string("payments/report-pdf.html", context)

        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = "inline; report.pdf"

        HTML(string=html).write_pdf(response,)

        return response
