from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404
from sportsgramapp.serializers.app_serializers import*
from sportsgramapp.serializers import *
from rest_framework.response import Response
from sportsgramapp.models import *
from rest_framework import status


class SignUpAPi(APIView):
    def post(self, request, format=None):

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(**serializer.data)
            userprofile=UserProfile()
            userprofile.user=user
            userprofile.save()
            return Response({'id': user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserDetailesApi(APIView):
    # permission_classes = (IsAuthenticated)
    """
        Get  info related to the logged in user


        when we send along iwth jwt authentication token there is user object request.user !!!!
    """
    def get(self, request, format=None):
        import ipdb
        ipdb.set_trace()
        user = get_object_or_404(User, pk=request.user.id)
        serializer = UserUpdateSerializer(user)
        return Response(serializer.data)

    """
        Update User info such as password, email, first name, last name
    """
    def put(self, request, format=None):

        import ipdb
        ipdb.set_trace()
        user = get_object_or_404(User, pk=request.user.id)
        serializer = UserUpdateSerializer(user, request.data)

        if serializer.is_valid():
            user = serializer.save()
            """
            
                When saving the user via serializer hashing wont be done, so by calling the method "set_password"
                the hashed values of the password will be stored in the DB
            
            """
            user.set_password(user.password)
            user.save()
            return Response({'id': user.id}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def user_credentials(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)

@csrf_exempt
def users_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':

        # data = JSONParser().parse(request)

        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


