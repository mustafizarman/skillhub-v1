
from rest_framework import serializers
from skillhub.models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'birthday', 'designation', 'phone_number', 'profile_picture']
        read_only_fields = ['id', 'username', 'email']