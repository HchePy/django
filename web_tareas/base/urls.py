from django.urls import path
from .views import (ListaPendientes, DetalleTarea, CrearTarea, EditarTarea,register,
                    EliminarTarea, Logueo, deslogueo)

urlpatterns = [path('', ListaPendientes.as_view(), name='tareas'),
               path('login/', Logueo.as_view(), name='login'),
               path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
               path('crear-tarea/', CrearTarea.as_view(), name='crear_tarea'),
               path('editar-tarea/<int:pk>', EditarTarea.as_view(), name='editar_tarea'),
               path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar_tarea'),
               path('logout/',deslogueo,name='logout'),
               path('registro/',register,name='registro')]
