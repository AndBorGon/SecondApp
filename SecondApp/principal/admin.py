__author__ = 'andres'
from django.contrib import admin

from principal.models import *

# Register your models here.
#list_class=[]
#clsmembers = inspect.getmembers(sys.modules['models'], inspect.isclass)
#for name in clsmembers:
#    list_class.append(name[0])
#admin.site.register(list_class)
class UsuarioAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('first_name','last_name', 'username', 'email' ,'password','birth',)
        }),
    )
    list_display = ['__unicode__','first_name','email','date_joined']
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(producto)
admin.site.register(precio)
admin.site.register(tienda)
admin.site.register(clasificationproducto)
admin.site.register(clasificationtienda)