from rest_framework import serializers
from .models import Assembly


class AssemblySerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='name.username')
    is_name = serializers.SerializerMethodField()

    def is_name(self, obj):
        request = self.context['request']
        return request.user == obj.name


    class Meta:
        model = Assembly
        fields = '__all__'
