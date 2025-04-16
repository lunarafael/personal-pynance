from django.db import models
from django.conf import settings

class Category(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Transaction(models.Model):
    TIPO_CHOICES = (
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    )

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=255, blank=True)
    data = models.DateField()

    def __str__(self):
        return f"{self.usuario.username} - {self.tipo} - R${self.valor}"
