from django.urls import path
from . import views, auth
urlpatterns = [
    path('', views.index), 
    path('administrador/', views.administrador), 
    path('registro/', auth.registro),
    path('login/', auth.login),
    path('logout/', auth.logout) ,
    path('procesar_mensaje/', views.procesar_mensaje),
    path('procesar_comentario/', views.procesar_comentario) ,
    path('eliminar_comentario/<int:id>', views.eliminar_comentario) ,
    path('eliminar_mensaje/<int:id>', views.eliminar_mensaje) ,
]
