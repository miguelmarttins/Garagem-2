from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nascionalidade = models.CharField(max_length=50, null=True);

    def __str__(self):
        return f"{self.nome.upper()} ({self.id}) ({self.nascionalidade})"
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"