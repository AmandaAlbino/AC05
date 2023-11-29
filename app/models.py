from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()

    arquivado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome