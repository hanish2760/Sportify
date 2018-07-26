from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework_jwt.serializers import User

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from sportsgramapp.serializers.app_serializers import UserUpdateSerializer, UserProfile, SportsSerializer, Sport, \
    UserProfileSerializer


class UserSportsAPI(APIView):
    # permission_classes = (IsAuthenticated)
    """
        Get  info related to the logged in user
        when we send along with jwt authentication token there is user object request.user !!!!
    """
    def get(self, request, format=None):
        import ipdb
        ipdb.set_trace()
        user = get_object_or_404(User, pk=request.user.id)
        userprofile=UserProfile.objects.get(user=user)
        serializer = UserProfileSerializer(userprofile)
        # need to return the spors played by the user!!
        return Response(serializer.data)


    def put(self, request, format=None):
        user = get_object_or_404(User, pk=request.user.id)
        userprofile = UserProfile.objects.get(user=user)

        for s in request.data['sports']:
            # sport=SportsSerializer(s)
            sid=s['id']
            sport=Sport.objects.get(id=sid)
            userprofile.sports.add(sport)

        user.save()
        return Response({'id': user.id}, status=status.HTTP_201_CREATED)

# similarly for the grounds !
