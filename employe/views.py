from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import Pulpit, Employe
from .serializer import PulpitSerializer, EmployeSerializer


class EmployeViewSet(ModelViewSet):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    filterset_fields = ['puplit']
    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partial_update', 'create']:
            self.permission_classes = [IsAdminUser]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()        


class PulpitViewSet(ModelViewSet):
    queryset = Pulpit.objects.all()
    serializer_class = PulpitSerializer