from django.db import models

# Create your models here.
class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name="Titulo")
    imagem = models.ImageField(upload_to='imagens/', verbose_name="Imagem", null=True)
    descricao = models.TextField(verbose_name="descrição", null=True)
