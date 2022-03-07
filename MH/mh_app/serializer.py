from rest_framework import serializers
from .models import MH_tb

class MH_tb_Serializer(serializers.ModelSerializer):
    class Meta:
        model = MH_tb
        fields = ('housing_area_code', 'facility_key','shape_wkt','facility_type',
        'ordinal_number','structure_type','shape','fabricated_type_code','pref',
        'create_by','create_at','update_by','update_at')