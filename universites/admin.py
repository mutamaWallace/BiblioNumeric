from django.contrib import admin
from .models import Universite, Faculte, Departement, Class

@admin.register(Universite)
class UniversiteAdmin(admin.ModelAdmin):
    list_display = ('universite', 'pays', 'ville', 'email', 'site_web', 'campus')
    search_fields = ('universite', 'pays', 'ville')
    
@admin.register(Faculte)
class FaculteAdmin(admin.ModelAdmin):
    list_display = ('faculte', 'universite')
    search_fields = ('faculte',)

@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ('departement', 'faculte')
    search_fields = ('departement',)

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('niveau', 'departement', 'faculte')
    search_fields = ('niveau',)