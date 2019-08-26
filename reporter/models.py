from django.db import models
from django.contrib.gis.db import models
# Create your models here.
class Incidences(models.Model):
	class Meta:
		verbose_name_plural = 'Incidences'
	name = models.CharField(max_length = 20)
	location = models.PointField(srid=4326)


	def __str__(self):
		return self.name

class counties(models.Model):
    objectid = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    county3_field = models.FloatField()
    county3_id = models.FloatField()
    county = models.CharField(max_length=20)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    class Meta:
    	verbose_name_plural = 'counties'

    def __str__(self):
    	return self.county