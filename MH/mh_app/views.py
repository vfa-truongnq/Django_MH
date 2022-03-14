from django.shortcuts import render
from django.http.response import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
        return JsonResponse(serializer.data)
    
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
def api_get_list_for_radius(request):
    try:
        mh_data = MH_tb.objects.get(shape_wkt = request.GET)
    except MH_tb.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MH_tb_Serializer(mh_data, many=True)
        return JsonResponse(serializer.data, safe = False)

        