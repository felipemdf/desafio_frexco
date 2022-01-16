from django.contrib import admin
from api.models import Region, Fruit

class Regions(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_per_page = (5)

class Fruits(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_per_page = (5)

admin.site.register(Region, Regions)
admin.site.register(Fruit, Fruits)
