from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_posts, name='listar_posts'),
    path('<int:post_id>/', views.detalle_post, name='detalle_post'),
    path('crear/', views.crear_post, name='crear_post'),
    path('registro/', views.registro, name='registro'),
    path('profile/', views.perfil, name='profile'),
    path('editar/<int:post_id>/', views.editar_post, name='editar_post'),
    path('borrar/<int:post_id>/', views.borrar_post, name='borrar_post'),
    path('acerca-de-mi/', views.acerca_de_mi, name='acerca_de_mi'),
    
]
