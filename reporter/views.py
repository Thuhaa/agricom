from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import counties, Incidences
# Create your views here.
class HomePageView(TemplateView):
	template_name = 'index.html'



def CountyData(request):
	Counties = serialize('geojson', counties.objects.all())
	return HttpResponse(Counties, content_type='json')

def Incidence(request):
	points = serialize('geojson', Incidences.objects.all())
	return HttpResponse(points, content_type='json')