from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Assembly
from .serializers import AssemblySerializer


class AssemblyList(APIView):
    def get(self, request):
        assemblies = Assembly.objects.all()
        serializer = AssemblySerializer(assemblies, many=True)

        return Response(serializer.data)


