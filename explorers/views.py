from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Assembly
from .serializers import AssemblySerializer
from django.http importHttp404


class AssemblyList(APIView):
    def get(self, request):
        assemblies = Assembly.objects.all()
        serializer = AssemblySerializer(assemblies, many=True)

        return Response(serializer.data)


class AssemblyDetail(APIView):
    def get_object(self, pk):
        try:
            assembly = Assembly.objects.get(pk=pk)
            return assembly
        except Profile.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        assembly = self.get_object(pk)
        serializer=AssemblySerializer(assembly)
        return Response(serializer.data)


