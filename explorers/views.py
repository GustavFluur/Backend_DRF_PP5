from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Assembly
from .serializers import ProfileSerializer


class AssemblyList(APIView):
    def get(self, request):
        assemblies = Assembly.objects.all()
        serializer = AssemblySerializer(explorers, many=True)

        return Response(serializer.data)


