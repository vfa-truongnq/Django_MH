from django.shortcuts import render
from django.http.response import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.gis.geos import GEOSGeometry,Point

from .models import MH_tb
from .serializer import MH_tb_Serializer

from rest_framework import status
from rest_framework.decorators import api_view


### Create your views here.

@api_view(['GET',])
def api_detail_mh(request, id):
    try:
        mh_data = MH_tb.objects.get(facility_key=id)
    except MH_tb.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MH_tb_Serializer(mh_data)
        return JsonResponse()
    
@api_view(['PUT',])
def api_update_mh(request, id):
    try:
        mh_data = MH_tb.objects.get(facility_key=id)
    except MH_tb.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        try:
            serializer = MH_tb_Serializer(mh_data, data=request.data)
            data={}
            if serializer.is_valid():
                serializer.save()
                data['Success'] = 'Update success'
                return JsonResponse(data=data)
        except:
            return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['DELETE',])
def api_delete_mh(request, id):
    try:
        mh_data = MH_tb.objects.get(facility_key=id)
    except MH_tb.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        try:
            operation = mh_data.delete()
            data={}
            if operation:
                data['Success'] = 'Delete success'
        except:
            data['Fail'] = 'Delete failed'
        return JsonResponse(data=data)

@api_view(['POST',])
def api_create_mh(request):
    try:
        serializer = MH_tb_Serializer(data=request.data)
    except MH_tb.Exist:
        return JsonResponse(status=status.HTTP_201_CREATED) 
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({
                'message': 'Create a new Car successful!'
            }, status=status.HTTP_201_CREATED)
    return JsonResponse({
            'message': 'Create a new Car unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_get_list(request):
    try:
        mh_data = MH_tb.objects.all()
    except MH_tb.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MH_tb_Serializer(mh_data, many=True)
        return JsonResponse(serializer.data, safe = False)

@api_view(['GET'])
def api_get_list_radius(request):
    try:
        latitude = float(request.GET['latitude'])
        longtitude = float(request.GET['longtitude'])
        radius  = float(request.GET['radius'])
        page = request.query_params.get('page')

        location = Point(latitude,longtitude,srid=4326)
        get_data = MH_tb.objects.filter(shape_wkt__distance_lte = (location, radius))
        paginator = Paginator(get_data,5)
        try:
            get_data = paginator.page(page) 
        except PageNotAnInteger:                                
            get_data = paginator.page(1)                    
        except EmptyPage:                                       
            get_data = paginator.page(paginator.num_pages)
        serializer = MH_tb_Serializer(get_data, many=True)
    except:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)
    return JsonResponse(serializer.data, safe=False)




        
