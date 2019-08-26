from django.contrib import admin
from .models import Incidences, counties
from leaflet.admin import LeafletGeoAdmin

class IncidencesAdmin(LeafletGeoAdmin):
	list_display = ('name', 'location')

class countiesAdmin(LeafletGeoAdmin):
	list_display = ('county', 'objectid')

admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(counties, countiesAdmin)