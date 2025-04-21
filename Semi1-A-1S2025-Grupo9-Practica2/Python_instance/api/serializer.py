from rest_framework import serializers
from .models import Usuarios, Tareas, Archivos

class usuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'
        
class TareasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = '__all__'
        
class ArchivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivos
        fields = '__all__'
    