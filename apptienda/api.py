from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

class ApptiendaViewSetlibro(viewsets.ModelViewSet):
    queryset = libro.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ApptiendaSerializerlibro

class ApptiendaViewSetpersona(viewsets.ModelViewSet):
    queryset = persona.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ApptiendaSerializerpersona

class ApptiendaViewSetfacturacion(viewsets.ModelViewSet):
    queryset = facturacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ApptiendaSerializerfacturacion

class ApptiendaViewSetusuario(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ApptiendaSerializerusuario