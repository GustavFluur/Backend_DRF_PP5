from rest_framework import serializers
from .models import Assembly

class AssemblySerializer(serializers.ModelSerializer):
    MeetingPoint = serializers.ReadOnlyField(source='MeetingPoint.username')

    class Meta:
        model = Assembly
        fields = '__all__'
