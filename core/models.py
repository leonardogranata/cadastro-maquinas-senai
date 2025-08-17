from django.db import models

class Colaboradoes(models.Model):
    nomeCompleto = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    setor = models.CharField(max_length=8)

    def __str__(self):
        return f'{self.nomeCompleto} - {self.setor}'

class Maquinas(models.Model):
    nomeMaquina = models.CharField(max_length=25)
    numPatrimonio = models.CharField(max_length=8)
    modelo = models.CharField(max_length=10)
    setor = models.CharField(max_length=8)
    colaborador = models.ForeignKey(Colaboradoes, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomeMaquina