from django.contrib import admin

from .models import Hall, Film, Session, Tickets

admin.site.register(Hall)
admin.site.register(Film)
admin.site.register(Session)
admin.site.register(Tickets)