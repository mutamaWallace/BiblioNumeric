from django.contrib import admin

# Register your models here.

from .models import Utilisateur

admin.site.register(Utilisateur)


class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cin', 'email','password')
