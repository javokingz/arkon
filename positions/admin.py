from django.contrib import admin
from positions.models import Position

@admin.register(Position)
class PostAdmin(admin.ModelAdmin):
    list_display =['alcaldia', 'vehicle_id']
