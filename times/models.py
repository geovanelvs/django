from django.db import models

class Time(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Time")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    ano_fundacao = models.IntegerField(verbose_name="Ano de Fundação")

    def __str__(self):
        return f"{self.nome} ({self.cidade})"