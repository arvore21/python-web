from django.db import models

# Create your models here.
class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name="Titulo")
    imagem = models.ImageField(upload_to='imagens/', verbose_name="Imagem", null=True)
    descricao = models.TextField(verbose_name="descrição", null=True)


    def __str__(self):
        dados = "Titulo: " + self.titulo + "-" + "Descrição: " + self.descricao
        return dados

    def delete(self, using=None, keep_parents=False):
        self.imagem.storage.delete(self.imagem.name)
        super().delete()

                    