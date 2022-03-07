from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .models import MH_tb
from .serializer import MH_tb_Serializer
from rest_framework import status
from rest_framework.decorators import api_view


### Create your views here.
class MHViewSet(viewsets.ModelViewSet):
    queryset = MH_tb.objects.all()
    serializer_class = MH_tb_Serializer

class MH_get_shape(viewsets.McoodelViewSet):
    queryset = MH_tb.objects.filter(shape_wkt='') 

#def MH_list(request):
#    if request.method == 'GET':
#        mh_app = MH_tb.objects.all()
#        return JsonResponse(MH_tb_Serializer.data, safe=False)
#   elif request.method == 'POST':
#        mh_data = JSONParser().parse(request)
#        MH_tb_Serializer = 