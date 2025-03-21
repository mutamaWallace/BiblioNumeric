from django.contrib import admin
from .models import Auteurs

# Register your models here.

admin.site.register(Auteurs)
class Auteursadmin(admin.ModelAdmin):
    list_display=['id','nom','prenom','postnom','CNI','Email']
    