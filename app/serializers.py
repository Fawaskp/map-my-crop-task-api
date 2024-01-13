from rest_framework import serializers
from .models import POI
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password


"""Admin Related Serializers"""

class AdminCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password"]

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            is_staff=True,
            is_superuser=True,
        )
        return user


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password"]

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user

class UserListSerializer(serializers.ModelSerializer):
    num_pois = serializers.IntegerField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'is_superuser','num_pois']


"""User Related Serializer"""

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password"]

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


"""POI Serializer"""

class POISerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(source="point.y")
    longitude = serializers.FloatField(source="point.x")
    username = serializers.SerializerMethodField()

    class Meta:
        model = POI
        fields = ["id", "name", "latitude", "longitude", "user", "username"]

    def get_username(self, obj):
        return obj.user.username if obj and obj.user else None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")

        if request and request.method == "GET":
            data["username"] = self.get_username(instance)

        return data
