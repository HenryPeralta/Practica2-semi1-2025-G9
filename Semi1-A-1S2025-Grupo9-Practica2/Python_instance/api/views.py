from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import usuarios, Tareas, Archivos, respuestaServidor
from rest_framework import status
from .serializer import usuariosSerializer, TareasSerializer, ArchivosSerializer
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
import jwt

# USUARIOS

@api_view(['POST'])
def crear_usuario(request):
    if request.method == 'POST':
        try:
            usuario = usuarios.objects.get(correo=request.data['correo'])
        except usuarios.DoesNotExist:
            usuario = None
        if usuario:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'El correo ya se encuentra registrado'})
        
        #hashing de la contraseña
        data = request.data.copy()
        data['contraseña'] = make_password(length=8)
        
        serializer = usuariosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            respuestaServidor = respuestaServidor('REGISTER_SUCCESS', 'Registro exitoso', serializer.data, numberCode=201)
            return Response(respuestaServidor, status=status.HTTP_201_CREATED)
        respuestaServidor = respuestaServidor('REGISTER_FAILED', 'Registro exitoso',  numberCode=400, status='error')
        return Response(respuestaServidor, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def listar_usuarios(request):
    if request.method == 'GET':
        usuarios_list = usuarios.objects.all()
        serializer = usuariosSerializer(usuarios_list, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def Obtener_usuario_nombre(request):
    if request.method == 'GET':
        try:
            usuario = usuarios.objects.get(nombre_usuario=request.data['nombre_usuario'])
        except usuarios.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = usuariosSerializer(usuario)
        return Response(serializer.data)
    
@api_view(['GET'])
def obtener_usuario_correo(request):
    if request.method == 'GET':
        try:
            usuario = usuarios.objects.get(correo=request.data['correo'])
        except usuarios.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = usuariosSerializer(usuario)
        return Response(serializer.data)


@api_view(['DELETE'])
def borrar_usuario_nombre(request, nombre_usuario):
    try:
        usuario = usuarios.objects.get(nombre_usuario=nombre_usuario)
    except usuarios.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    usuario.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def borrar_usuario_correo(request, correo):
    try:
        usuario = usuarios.objects.get(correo=correo)
    except usuarios.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    usuario.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def manejo_usuario(request, primary_key):
    if request.method == 'GET':
        try:
            usuario = usuarios.objects.get(primary_key=primary_key)
        except usuarios.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = usuariosSerializer(usuario)
        return Response(serializer.data)
    if request.method == 'PUT':
        try:
            usuario = usuario.objects.get(primary_key=primary_key)
        except usuarios.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = usuariosSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    if request.method == 'DELETE':
        try:
            usuario = usuarios.objects().get(primary_key=primary_key)
        except usuarios.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def iniciar_sesion(request):
    try:
        # Buscar al usuario por correo
        usuario = usuarios.objects.get(correo=request.data['correo'])
        
        # Verificar la contraseña
        if not check_password(request.data['contraseña'], usuario.contraseña):
            return Response({
                'stringCode': 'LOGIN_FAILED',
                'message': 'Contraseña incorrecta'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        # Crear el payload para el token
        payload = {
            'id': usuario.id,
            'nombre_usuario': usuario.nombre_usuario,
            'correo': usuario.correo,
            'imagen_perfil_url': usuario.imagen_perfil_url
        }
        
        # Generar el token JWT
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        
        # Responder con el token
        return Response({
            'stringCode': 'LOGIN_SUCCESS',
            'message': 'Inicio de sesión exitoso',
            'payload': {'token': token}
        }, status=status.HTTP_200_OK)
    
    except usuarios.DoesNotExist:
        return Response({
            'stringCode': 'LOGIN_FAILED',
            'message': 'Usuario no encontrado'
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            'status': 'error',
            'stringCode': 'LOGIN_FAILED',
            'message': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def cerrar_sesion(request):
    if request.method == 'POST':
        return Response(status=status.HTTP_200_OK)
    
# TASKS
###################################################
# TASKS

@api_view(['POST'])
def Crear_Tarea(request):
    if request.method == 'POST':
        serializer = TareasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def Obtener_Tareas_Titulo(request):
    if request.method == 'GET':
        try:
            tareas = Tareas.objects.filter(titulo=request.data['titulo'])
        except Tareas.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TareasSerializer(tareas, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def Obtener_Tareas_User(request):
    if request.method == 'GET':
        try:
            tareas = Tareas.objects.filter(usuario_id=request.data['usuario_id'])
        except Tareas.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TareasSerializer(tareas, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def Obtener_Tareas(request):
    if request.method == 'GET':
        Tareas = Tareas.objects.all()
        serializer = TareasSerializer(Tareas, many=True)
        return Response(serializer.data)
    

@api_view(['GET', 'PUT', 'DELETE'])
def manejo_Tarea_ID(request, primary_key):
    if request.method == 'GET':
        try:
            tarea = tarea.objects.get(primary_key=primary_key)
        except Tareas.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TareasSerializer(tarea)
        return Response(serializer.data)
    if request.method == 'PUT':
        try:
            tarea = tarea.objects.get(primary_key=primary_key)
        except Tareas.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TareasSerializer(tarea, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    if request.method == 'DELETE':
        try:
            tarea = Tareas.objects.get(primary_key=primary_key)
        except Tareas.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        tarea.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# 
###################################################
# Archivos

@api_view(['POST'])
def crear_archivo(request):
    if request.method == 'POST':
        serializer = ArchivosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# Archivos
###################################################################################