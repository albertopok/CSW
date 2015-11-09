from django.db import models
from jsonfield import JSONField
import collections

# Create your models here.
class Catalogo(models.Model):
    name = models.CharField(max_length=120, blank = False, null = False)
    json_layers= JSONField(load_kwargs={'object_pairs_hook': collections.OrderedDict})
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __unicode__(self):
        return self.name
#Ejemplo GetRecords
#http://ide.adesur.centrogeo.org.mx/catalogue/csw?service=CSW&version=2.0.2&request=GetRecords&outputFormat=application/json&outputSchema=http://www.isotc211.org/2005/gmd&resultType=results&ElementSetName=summary&typeNames=csw:Record
