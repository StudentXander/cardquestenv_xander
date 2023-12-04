from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PokemonCard

# admin.site.register(PokemonCard)
@admin.register(PokemonCard)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity")
    search_fields = ("name", "rarity")
