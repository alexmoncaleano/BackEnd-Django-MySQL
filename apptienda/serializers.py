from rest_framework import serializers

from apptienda.models import *


class ApptiendaSerializerlibro(serializers.ModelSerializer):
    class Meta:
        model = libro
        fields = ('id', 'title', 'description', 'autor', 'editorial', 'añoedicion',
                  'preciocompra', 'precioalquiler', 'disponible', 'portada', 'created_at')
        read_only_dields = ('created_at', )


class ApptiendaSerializerpersona(serializers.ModelSerializer):
    class Meta:
        model = persona
        fields = ('id', 'nombre', 'apellido', 'cedula',
                  'direcion', 'celular', 'email')


class ApptiendaSerializerfacturacion(serializers.ModelSerializer):
    class Meta:
        model = facturacion
        fields = ('id', 'fecha', 'usuario', 'libro', 'valor')


class ApptiendaSerializerusuario(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ('id', 'contraseña', 'usuario', 'persona')
