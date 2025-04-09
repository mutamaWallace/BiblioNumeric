from django.contrib import admin
from campus.models import *
# Register your models here.

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('id', 'codecampus', 'campus')
