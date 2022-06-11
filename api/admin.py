from django.contrib import admin

from api.models import Infanunciante, Infempresa, anuncios


@admin.register(Infanunciante)
class InfanuncianteAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(anuncios)
class anunciosAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(Infempresa)
class InfempresaAdmin(admin.ModelAdmin):
    exclude = ()

