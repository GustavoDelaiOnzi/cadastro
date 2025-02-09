from django.db import models


class Contato(models.Model):
    nome = models.CharField(db_column='NOME', max_length=125)
    telefone = models.CharField(db_column='TELEFONE', max_length=11)
    email = models.CharField(db_column='ENAIL', max_length=255, null=True)

    class Meta:
        db_table = 'CONTATO'
