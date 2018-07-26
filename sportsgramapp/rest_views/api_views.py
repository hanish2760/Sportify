from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from sportsgramapp.models import Sport, Ground
from sportsgramapp.serializers.app_serializers import SportsSerializer,GroundSerializer


@csrf_exempt
def sports_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        sports = Sport.objects.all()
        serializer = SportsSerializer(sports, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':

        # data = JSONParser().parse(request)

        data = JSONParser().parse(request)
        serializer = SportsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def sport_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        sport = Sport.objects.get(pk=pk)
    except Sport.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SportsSerializer(sport)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SportsSerializer(sport, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        sport.delete()
        return HttpResponse(status=204)

@csrf_exempt
def grounds_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        # ground = Ground.objects.values('id','ground_name')
        ground = Ground.objects.all()
        serializer = GroundSerializer(ground, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':

        # data = JSONParser().parse(request)

        data = JSONParser().parse(request)
        serializer = GroundSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def ground_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        ground = Ground.objects.get(pk=pk)
    except Ground.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GroundSerializer(ground)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GroundSerializer(ground, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        ground.delete()
        return HttpResponse(status=204)

