from django.contrib import admin
from RecipeApp.models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list = ['title', 'description', 'ingredients', 'instructions']

admin.site.register(Recipe, RecipeAdmin)