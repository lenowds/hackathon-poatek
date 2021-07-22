from django.db import models
from model_utils.models import TimeStampedModel

class TipoEndereco(TimeStampedModel):
    des_tipo_endereco = models.CharField(max_length=50, unique=True, blank=False)
    flg_ativo = models.BooleanField(default=True)

    objects = models.Manager()

    class Meta:
        ordering = ("des_tipo_endereco",)

    def __str__(self):
        return self.des_tipo_endereco
