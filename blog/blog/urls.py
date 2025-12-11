from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from blog.views import IndexView
from apps.posts.views import ckeditor5_subir_imagen

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='index'),

    # Usuarios
    path('usuarios/', include(('apps.usuarios.urls', 'usuarios'), namespace='usuarios')),
    
    # Nosotros
    path('nosotros/', TemplateView.as_view(template_name='nosotros.html'), name='nosotros'),
    
    # Contacto
    path('contacto/', TemplateView.as_view(template_name='contacto.html'), name='contacto'),

    # POSTS -> NECESARIO PARA QUE FUNCIONE "posts:ListaColaboraciones"
    path('posts/', include(('apps.posts.urls', 'posts'), namespace='posts')),

    path("comentarios/", include("apps.comentarios.urls", namespace="comentarios")),
    
    # CKEditor 5 upload - URL global requerida por CKEditor 5
    path('ckeditor/upload/', ckeditor5_subir_imagen, name='ck_editor_5_upload_file'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
