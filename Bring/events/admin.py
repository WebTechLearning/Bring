from django.contrib import admin
from .models import Item, Transportation, Event

# Register your models here.
admin.site.register(Item)

class EventAdmin(admin.ModelAdmin):
    fields = ('place', 'start_date', 'end_date', 'duration', 'gender', 'trans', 'items')
    readonly_fields = ('duration',)
    
    def duration(self, obj):
        return (obj.end_date - obj.start_date).days + 1

admin.site.register(Event, EventAdmin)

admin.site.register(Transportation)