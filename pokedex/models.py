from django.db import models

# Create your models here.


class Habilidade(models.Model):
    nome = models.CharField(max_length= 40, verbose_name= "Nome")
    descricao_habilidade = models.CharField(max_length=200, verbose_name="Descrição")

    def __str__(self):
        return self.nome


class Tipo(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    descricao_tipo = models.CharField(max_length=200, verbose_name="Descrição")

    def __str__(self):
        return self.nome


class Pokemon(models.Model):
    imagem = models.FileField(upload_to='fotos/')
    nome = models.CharField(max_length=120)
    pontos_de_vida = models.PositiveIntegerField(verbose_name="Vida")
    pontos_de_ataque = models.PositiveIntegerField(verbose_name="Ataque")
    pontos_de_defesa = models.PositiveIntegerField(verbose_name="Defesa")
    pontos_de_velocidade = models.PositiveIntegerField(verbose_name="Velocidade")
    ataque_especial = models.PositiveIntegerField(verbose_name="Ataque Especial")
    defesa_especial = models.PositiveIntegerField(verbose_name="Defesa Especial")
    fk_habilidade = models.ManyToManyField(Habilidade)
    fk_tipo = models.ManyToManyField(Tipo)
    peso = models.FloatField(verbose_name="Peso")

    def __str__(self):
        return self.nome


