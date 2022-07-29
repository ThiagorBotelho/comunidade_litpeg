from django.db import models
from django.contrib.auth.models import User


class Laboratorio(models.Model):
  nome_lab = models.CharField(max_length=256)
  usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


  def __str__(self) -> str:
    return self.nome_lab


class Pessoa(models.Model):
  nome_completo = models.CharField(max_length=256, verbose_name='Nome')
  email = models.EmailField(verbose_name='E-mail')
  numero_cracha = models.CharField(max_length=25)
  funcao = models.CharField(max_length=25, default='')
  laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return self.nome_completo