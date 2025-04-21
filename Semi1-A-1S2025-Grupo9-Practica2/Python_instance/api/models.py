from django.db import models

class Usuarios(models.Model):
    nombre_usuario = models.CharField(max_length=255)
    correo = models.EmailField(max_length=255)
    contrasena = models.CharField(max_length=255)
    imagen_perfil_url = models.CharField(max_length=300)
    class Meta:
        db_table = 'Usuarios'

class Tareas(models.Model):
    usuario_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    completada = models.BooleanField(default=False)
    class Meta:
        db_table = 'Tareas'
        
class Archivos(models.Model):
    usuario_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    nombre_archivo = models.CharField(max_length=255)
    tipo_archivo = models.CharField(max_length=10)
    url_archivo = models.CharField(max_length=255)
    class Meta:
        db_table = 'Archivos'
        
class respuestaServidor():
    def __init__(self, stringCode, message, payload=None, status='success',numberCode=200):
        self.status = status
        self.numberCode = numberCode
        self.stringCode = stringCode
        self.message = message
        self.payload = payload
        
    def to_dict(self):
        return {
            'status': self.status,
            'numberCode': self.numberCode,
            'stringCode': self.stringCode,
            'message': self.message,
            'payload': self.payload,
        }