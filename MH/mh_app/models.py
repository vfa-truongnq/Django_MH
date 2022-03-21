from django.db import models
from django.contrib.gis.db import models
import csv


# Create your models here.
class MH_tb(models.Model):
#    path = 'E:\Django_MH\MH\mh.csv'
    housing_area_code = models.BigIntegerField()
    facility_key = models.CharField(max_length=150, primary_key=True)
    shape_wkt = models.PointField()
    facility_type = models.CharField(max_length=100)
    ordinal_number = models.IntegerField()
    structure_type = models.CharField(max_length=150)
    shape = models.CharField(max_length=500)
    fabricated_type_code = models.CharField(max_length=500)
    pref = models.CharField(max_length=100)
    create_by = models.CharField(max_length=150, default='some string')
    create_at = models.DateTimeField()
    update_by = models.CharField(max_length=150)
    update_at = models.DateTimeField()

    def __str__(self):
        return self.facility_key 

    # def load_csv_file(path):
    #     with open(path) as file_obj:
    #         reader = csv.reader(file_obj)
    #         for row in reader:
    #             MH_tb.objects.create(
    #                 housing_area_code=row[0],
    #                 facility_key=row[1],
    #                 shape_wkt=Point(row[2]),
    #                 facility_type=row[3],
    #                 ordinal_number = row[4],
    #                 structure_type = row[5],
    #                 shape = row[6],
    #                 fabricated_type_code = row[7],
    #                 pref = row[8],
    #                 create_by = row[9],
    #                 create_at = DateTime(row[10]),
    #                 update_by = row[11],
    #                 update_at = DateTime(row[12])
    #             )
    
