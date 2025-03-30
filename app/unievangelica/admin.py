from django.contrib import admin
from .models import Bloco

# Register your models here.

@admin.register(Bloco)
class BlocoAdmin(admin.ModelAdmin):
    ...
