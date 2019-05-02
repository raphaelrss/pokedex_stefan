from django.db import models

# Create your models here.

class Pokemon(models.Model):
    imagem = models.FileField(upload_to='fotos/')
    nome = models.CharField(max_length=120)
    pontos_de_vida = models.PositiveIntegerField(verbose_name= "Vida")
    pontos_de_ataque = models.PositiveIntegerField(verbose_name= "Ataque")
    pontos_de_defesa = models.PositiveIntegerField(verbose_name= "Defesa")
    pontos_de_velocidade = models.PositiveIntegerField(verbose_name= "Velocidade")
    ataque_especial = models.PositiveIntegerField(verbose_name= "Ataque Especial")
    defesa_especial = models.PositiveIntegerField(verbose_name= "Defesa Especial")
    peso = models.FloatField(verbose_name= "Peso")

    def __str__(self):
        return self.nome
