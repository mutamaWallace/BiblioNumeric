from django.contrib import admin
from livre.models import *
# Register your models here.
@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'langueLivre', 'annee_publication','auteur', 'id_emplacement', 'compartiment', 'etagere')
    search_fields = ('titre', 'auteur__nom', 'langueLivre')