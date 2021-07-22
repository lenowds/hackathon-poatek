from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(flg_ativo=True)

class Categoria(TimeStampedModel):
    des_categoria = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="des_categoria")
    imagem = models.ImageField(upload_to="categorias/%Y", blank=True)

    class Meta:
        ordering = ("des_categoria",)
        #verbose_name = "category"
        #verbose_name_plural = "categories"
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.des_categoria

    def get_absolute_url(self):
        return reverse("product:list_by_category", kwargs={"slug": self.slug})


class Produto(TimeStampedModel):
    id_categoria = models.ForeignKey(
        Categoria, related_name="product", on_delete=models.CASCADE
    )
    des_produto = models.CharField(max_length=150, unique=True, blank=False)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="des_produto")
    imagem = models.ImageField(upload_to="products/%Y/%m/%d", blank=False)
    des_detalhes = models.TextField(blank=True)
    des_medida = models.CharField(max_length=50, blank=True)
    des_ingredientes = models.TextField(blank=True)
    des_fabricante = models.CharField(max_length=150)
    des_marca = models.CharField(max_length=100, blank=True)
    flg_ativo = models.BooleanField(default=True)

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ("des_produto",)

    def __str__(self):
        return self.des_produto

    def get_absolute_url(self):
        return reverse("product:detail", kwargs={"slug": self.slug})