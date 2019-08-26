from django.urls import path
from .views import *

urlpatterns = [
path('', HomePageView.as_view(), name = 'home'),
path('county/', CountyData, name='county'),
path('incidences/', Incidence, name='incidences'),


]