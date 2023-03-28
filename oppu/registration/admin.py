from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

def get_user_color(user):
    if user.is_staff:
        return 'green'
    else:
        return 'red'

class CustomUserAdmin(UserAdmin):
    def get_row_css_class(self, obj):
        return get_user_color(obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
