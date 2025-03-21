from django.contrib import admin
from emplacement.models import *

# Register your models here.
@admin.register(Emplacement)
class EmplacementAdmin(admin.ModelAdmin):
    list_display = ('id', 'position_precise', 'disponibilite', 'id_compartiment', 'id_etagere')
    search_fields = ('position_precise',)
