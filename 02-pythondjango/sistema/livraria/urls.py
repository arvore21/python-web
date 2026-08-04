from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre', views.sobre, name='sobre'),
    path('livros', views.livros, name='livros'),
    path('livros/criar', views.criar, name='criar'),
    path('livros/alterar/<int:id>', views.alterar, name='alterar'),
    path('excluir/<int:id>', views.excluir, name='excluir')    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

