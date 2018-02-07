from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from guidyapp.serializers import UserSerializer


# Create your views here.

class UserList (generics.ListAPIView):
    quertset = Tourist.objects.all()
    serializer_class = UserSerializer

class CurrentUser(generics.RetriveAPIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)