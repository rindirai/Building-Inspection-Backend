from django.contrib.auth.models import User
from rest_framework import serializers
from client.serializers import ClientProfileSerializer


class UserSerializer(serializers.ModelSerializer):
    inspector = ClientProfileSerializer(
        many=True, read_only=True)

    class Meta:
        model = User
        # fields = ('id', 'username', 'email', 'first_name', 'last_name')
        fields = '__all__'


class UserInspectorCountSerializer(serializers.ModelSerializer):
    # inspector = ClientProfileSerializer(
    #     many=True, read_only=True)
    inspector_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'inspector_count')

    def get_inspector_count(self, obj):
        return obj.inspector.count()
