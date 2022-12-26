from rest_framework import serializers
from .models import Assembly

class AssemblySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Assembly
        fields = '__all__'
