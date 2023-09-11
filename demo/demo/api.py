from rest_framework import generics
from djgentelella.models import CustomPermission
from serializers import CustomPermissionSerializer

class CustomPermissionList(generics.ListAPIView):
    queryset = CustomPermission.objects.all()
    serializer_class = CustomPermissionSerializer

