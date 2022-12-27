from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Assembly
from .serializers import AssemblySerializer
from django.http import Http404
from rest_framework import status
from DRF_API.permissions import IsOwnerOrReadOnly


class AssemblyList(APIView):
    def get(self, request):
        assemblies = Assembly.objects.all()
        serializer = AssemblySerializer(assemblies, many=True, context={'request': request})
        return Response(serializer.data)


class AssemblyDetail(APIView):
    serializer_class = AssemblySerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            assembly = Assembly.objects.get(pk=pk)
            self.check_object_permissions(self.request, assembly) 
            return assembly
        except Profile.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        assembly = self.get_object(pk)
        serializer = AssemblySerializer(assembly, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



