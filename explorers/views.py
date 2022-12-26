from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Assembly


class AssemblyList(APIView):
    def get(self, request):
        assemblies = Assembly.objects.all()
        return Response(assemblies)

