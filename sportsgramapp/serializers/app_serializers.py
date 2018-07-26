from rest_framework import serializers
from sportsgramapp.models import*
from rest_framework.serializers import ModelSerializer



class SportsSerializer(ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'


class GroundSerializer(ModelSerializer):
    class Meta:
        model = Ground
        fields = '__all__'


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups', 'user_permissions', 'is_staff', 'is_active', 'is_superuser')

class UserProfileSerializer(ModelSerializer):

    sports=SportsSerializer(many=True,read_only=True)
    grounds=GroundSerializer(many=True,read_only=True)
    location=LocationSerializer(many=True,read_only=True)

    class Meta:
        model=UserProfile
        fields='__all__'



class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('username', 'groups', 'user_permissions', 'is_staff', 'is_active', 'is_superuser')