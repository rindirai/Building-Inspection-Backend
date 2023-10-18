from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, UserInspectorCountSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class user_list_view(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class user_inspection_count(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserInspectorCountSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/toke/refresh'
    ]

    return Response(routes)
