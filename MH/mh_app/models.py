from django.db import models

# Create your models here.
class MH_tb(models.Model):
    housing_area_code = models.BigIntegerField()
    facility_key = models.CharField(max_length=150, primary_key=True)
    shape_wkt = models.CharField(max_length=5000)
    facility_type = models.CharField(max_length=100)
    ordinal_number = models.IntegerField()
    structure_type = models.CharField(max_length=150)
    shape = models.CharField(max_length=500)
    fabricated_type_code = models.CharField(max_length=500)
    pref = models.CharField(max_length=100)
    create_by = models.CharField(max_length=150, default='some string')
    create_at = models.DateTimeField()
    update_by = models.CharField(max_length=150)
    update_at = models.DateField()

    def __str__(self):
        return self.facility_key 
