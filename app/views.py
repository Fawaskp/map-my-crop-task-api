from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import POI
from .serializers import (
    POISerializer,
    UserRegistrationSerializer,
    AdminRegistrationSerializer,
)
from rest_framework import permissions


'''User related APIs'''
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

class POIListCreateView(generics.ListCreateAPIView):
    queryset = POI.objects.all()
    serializer_class = POISerializer


'''Admin Related APIs'''
class AdminRegistrationView(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


'''Common APIs'''
class POIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = POI.objects.all()
    serializer_class = POISerializer
