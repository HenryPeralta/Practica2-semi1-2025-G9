from django.urls import path
from .views import Obtener_Tareas_Titulo, Obtener_Tareas_User, Obtener_Tareas, manejo_Tarea_ID, Crear_Tarea
from .views import Obtener_usuario_nombre, borrar_usuario_correo, borrar_usuario_nombre, obtener_usuario_correo
from .views import manejo_usuario
from .views import iniciar_sesion, cerrar_sesion, crear_usuario, crear_archivo, listar_usuarios


urlpatterns = [
    path('auth/login', iniciar_sesion , name='Iniciar_sesion'),
    path('auth/register', crear_usuario, name='crear_usuario'),
    
    path('tasks/all', Obtener_Tareas , name='cerrar_sesion'),
    path('tasks/<id>', manejo_Tarea_ID , name='manejo_Tarea_ID'),
    path('tasks/user/<usuario_id>', Obtener_Tareas_User , name='Obtener_Tareas_User'),
    path('tasks/title/<titulo>', Obtener_Tareas_Titulo , name='Obtener_Tareas_Titulo'),
    path('tasks/', Crear_Tarea , name='Crear_Tarea'),
    
    
    
    
    path('users/', listar_usuarios , name='listar_usuarios'),
    path('users/<id>', manejo_usuario , name='manejo_usuario'),
    path('users/email/<email>', obtener_usuario_correo , name='obtener_usuario_correo'),
    path('users/email/<email>', borrar_usuario_correo , name='borrar_usuario_correo'),
    path('users/username/<username>', Obtener_usuario_nombre , name='Obtener_usuario_nombre'),
    path('users/username/<username>', borrar_usuario_nombre , name='borrar_usuario_nombre'),
    
    
    
]