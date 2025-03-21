from django.contrib import admin
from compartiment.models import *
# Register your models here.

@admin.register(Compartiment)
class CompartimentAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'nombreLivre', 'domaineLivre', 'etagere')
    search_fields = ('nom',)