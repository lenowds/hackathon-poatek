from django.contrib import admin

from .models import Categoria, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["des_categoria", "slug", "created", "modified"]


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        "des_produto",
        "slug",
        "id_categoria",
        "des_marca",
        "flg_ativo",
        "created",
        "modified",
    ]
    list_filter = ["flg_ativo", "created", "modified"]
    list_editable = ["des_marca", "flg_ativo"]