from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre', views.sobre, name='sobre'),
    path('livros', views.livros, name='livros'),
    path('livros/criar', views.criar, name='criar'),
    path('livros/alterar', views.alterar, name='alterar')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

