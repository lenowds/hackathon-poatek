from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from product.models import Produto
from shop.models import TipoEndereco

class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(flg_ativo=True)


class Estabelecimento(TimeStampedModel):
    des_estabelecimento = models.CharField(max_length=150, unique=True, blank=False)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="des_estabelecimento")
    imagem = models.ImageField(upload_to="marketplace/%Y", blank=True)
    flg_ativo = models.BooleanField(default=True)

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ("des_estabelecimento",)

    def __str__(self):
        return self.des_estabelecimento

class EstabelecimentoProduto(TimeStampedModel):
    estabelecimento = models.ForeignKey(
        Estabelecimento, related_name="estabelecimentoproduto", on_delete=models.CASCADE
    )
    produto = models.ForeignKey(
        Produto, related_name="product", on_delete=models.CASCADE
    )
    num_estoque = models.IntegerField(blank=False)
    vlr_unitario = models.DecimalField(max_digits=15, decimal_places=2)
    flg_ativo = models.BooleanField(default=True)

    objects = models.Manager()

    class Meta:
        ordering = ("produto_id",)

    def __str__(self):
        return self.produto.des_produto

class EstabelecimentoEndereco(TimeStampedModel):
    estabelecimento = models.ForeignKey(
        Estabelecimento, related_name="marketplace", on_delete=models.CASCADE
    )
    tipo_endereco = models.ForeignKey(
        TipoEndereco, related_name="shop", on_delete=models.CASCADE
    )
    des_cep = models.CharField(max_length=8, blank=False)
    des_logradouro = models.CharField(max_length=150, blank=False)
    des_numero = models.CharField(max_length=10)
    des_bairro = models.CharField(max_length=150, blank=False)
    des_cidade = models.CharField(max_length=150, blank=False)
    des_estado = models.CharField(max_length=2, blank=False)
    des_complemento = models.CharField(max_length=150, blank=True)
    des_latitude = models.CharField(max_length=100)
    des_longitude = models.CharField(max_length=100)
    flg_ativo = models.BooleanField(default=True)

    objects = models.Manager()

    class Meta:
        ordering = ("des_logradouro",)

    def __str__(self):
        return self.des_logradouro