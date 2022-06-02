from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from .models import Cloud, NonSmokingArea, SmokingArea
from rest_framework.views import APIView
from .serializers import CloudSerializer, NonSmokingSerializer, SmokingSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from haversine import haversine, Unit


@csrf_exempt
def address_list(request):
    if request.method == 'GET':
        query_set = Cloud.objects.all()
        serializer = CloudSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CloudSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def address(request, pk):
    obj = Cloud.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = CloudSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CloudSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


@csrf_exempt
def nonsmoking_list(request):
    if request.method == 'GET':
        query_set = NonSmokingArea.objects.all()
        serializer = NonSmokingSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def nonsmoking_filtered_list(request, lat, lon):
    if request.method == 'GET':
        longitude = float(lon)
        latitude = float(lat)
        point = (latitude, longitude)
        nonsmoking_all = NonSmokingArea.objects.all()
        nonsmoking_filter = [nonsmoking for nonsmoking in nonsmoking_all
                             if haversine(point, (nonsmoking.latitude, nonsmoking.longitude)) <= 0.3]

        serializer = NonSmokingSerializer(nonsmoking_filter, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def smoking_list(request):
    if request.method == 'GET':
        query_set = SmokingArea.objects.all()
        serializer = SmokingSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
