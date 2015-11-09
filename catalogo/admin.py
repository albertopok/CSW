from django.contrib import admin
from .models import Catalogo
# Register your models here.

class CatalogoAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp","updated"]
    class Meta:
        model=Catalogo

admin.site.register(Catalogo, CatalogoAdmin)
