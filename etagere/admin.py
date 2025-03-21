from django.contrib import admin
from etagere.models import *

# Register your models here.

@admin.register(Etagere)
class EtagereAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'etat_etagere', 'mobilite', 'charge_maximal')
    search_fields = ('nom',)