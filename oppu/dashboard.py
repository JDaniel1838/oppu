from django.utils.translation import gettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard

class CustomIndexDashboard(Dashboard):
    columns = 3

    def init_with_context(self, context):
        self.available_children.append(modules.LinkList)

        self.children.append(modules.LinkList(
            _('Administration'),
            children=[
                {
                    'title': _('Todos los Usuarios'),
                    'url': '/admin/auth/user/',
                    'external': False,
                },
                {
                    'title': _('Agregar Usuarios'),
                    'url': '/admin/auth/user/add',
                    'external': False,
                },
            ],
            column=0,
            order=1
        ))

        # Agrega el enlace para la aplicación "Payments"
        self.children.append(modules.LinkList(
            _('PAGOS '),
            children=[
                {
                    'title': _('Todos los pagos'),  # Título del enlace
                    'url': '/admin/payments/payment/',  # URL de la vista de administración de la aplicación "Payments"
                    'external': False,
                },
                {
                    'title': _('Registrar nuevo pago'),  # Título del enlace
                    'url': '/admin/payments/payment/add',  # URL de la vista de administración de la aplicación "Payments"
                    'external': False,
                },
            ],
            column=1,
            order=2  # Ajusta el orden del enlace en el panel de administrador según tus necesidades
        ))

        # Enlaces rapidos
        self.children.append(modules.LinkList(
            _('Enlaces Rapidos'),
            children=[
                {
                    'title': _('Volver al sitio'),
                    'url': '/',
                    'external': False,
                },
                {
                    'title': _('Cambiar contraseña'),  # Título del enlace
                    'url': '/admin/password_change/',  # URL de la vista de cambio de contraseña de Django
                    'external': False,
                },
                {
                    'title': _('Cerrar sesión'),  # Título del enlace
                    'url': '/admin/logout/',  # URL de la vista de cierre de sesión de Django
                    'external': False,
                },
            ],
            column=2,
            order=3
        ))
    """
    self.children.append(modules.LinkList(
            _('Support'),
            children=[
                {
                    'title': _('Django documentation'),
                    'url': 'http://docs.djangoproject.com/',
                    'external': True,
                },
                {
                    'title': _('Django "django-users" mailing list'),
                    'url': 'http://groups.google.com/group/django-users',
                    'external': True,
                },
                {
                    'title': _('Django irc channel'),
                    'url': 'irc://irc.freenode.net/django',
                    'external': True,
                },
            ],
            column=0,
            order=0
        ))


    
    """
