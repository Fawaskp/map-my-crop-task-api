from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.db import models
from .models import POI
from .serializers import (
    POISerializer,
    AdminCreateSerializer,
    UserCreateSerializer,
    UserRegistrationSerializer,
    UserListSerializer,
)
from django.contrib.gis.geos import Point
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from django.contrib.auth import get_user_model


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_check_authentication(request):
    access_token = request.headers.get('Authorization', '').split(' ')[1]
    role = AccessToken(access_token).get('role')
    status = 403 if role == 'admin' else 200
    return Response(status=status)

@api_view(['GET'])
@permission_classes([IsAuthenticated,IsAdminUser])
def admin_check_authentication(request):
    return Response(status=200)


def create_jwt_pair_tokens(user):
    refresh = RefreshToken.for_user(user)
    refresh["username"] = user.username
    refresh["username"] = user.username
    refresh['role'] = 'admin' if user.is_superuser and user.is_staff else 'user'
    tokens = {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }
    return tokens

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        tokens = create_jwt_pair_tokens(user)
        return Response(tokens, status=status.HTTP_200_OK)


"""Admin Related APIs"""

class AdminCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AdminCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

class UserListAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserListSerializer

    def get_queryset(self):
        queryset = get_user_model().objects.annotate(num_pois=models.Count('poi'))
        return queryset.order_by('id')


class POIListView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = POISerializer
    queryset = POI.objects.all()


"""User related APIs"""

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

class POIListByUserView(generics.ListAPIView):
    serializer_class = POISerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user = get_user_model().objects.get(id=user_id)
        return POI.objects.filter(user=user)
    

"""POI APIs"""

class POICreateView(generics.CreateAPIView):
    queryset = POI.objects.all()
    serializer_class = POISerializer

    def perform_create(self, serializer):
        latitude = self.request.data.get("latitude")
        longitude = self.request.data.get("longitude")

        point = Point(float(longitude), float(latitude))

        existing_poi = POI.objects.filter(point=point).first()
        if existing_poi:
            return Response(
                    {'detail': 'POI with these coordinates already exists.'}, 
                    status=status.HTTP_400_BAD_REQUEST
                   )

        serializer.validated_data["point"] = point

        serializer.save()


class POIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = POI.objects.all()
    serializer_class = POISerializer

    def perform_update(self, serializer):
        latitude = self.request.data.get("latitude")
        longitude = self.request.data.get("longitude")

        point = Point(float(longitude), float(latitude))

        serializer.validated_data["point"] = point

        serializer.save()
