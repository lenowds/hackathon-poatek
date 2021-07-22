from django.contrib import admin

from .models import Estabelecimento, EstabelecimentoProduto, EstabelecimentoEndereco


@admin.register(Estabelecimento)
class EstabelecimentoAdmin(admin.ModelAdmin):
    list_display = [
        "des_estabelecimento", 
        "slug", 
        "created", 
        "modified"
    ]

@admin.register(EstabelecimentoProduto)
class EstabelecimentoProdutoAdmin(admin.ModelAdmin):
    list_display = [
        "produto_id",
        "num_estoque",
        "vlr_unitario",
        "flg_ativo",
        "modified",
    ]
    list_filter = ["flg_ativo", "modified"]
    list_editable = ["vlr_unitario", "flg_ativo"]


@admin.register(EstabelecimentoEndereco)
class EstabelecimentoEnderecoAdmin(admin.ModelAdmin):
    list_display = [
        "estabelecimento_id",
        "tipo_endereco_id",
        "des_cep",
        "des_logradouro",
        "des_latitude",
        "des_longitude",
        "flg_ativo",
        "created",
        "modified",
    ]
    list_filter = ["estabelecimento_id", "flg_ativo", "created", "modified"]
    list_editable = ["des_latitude", "des_longitude", "flg_ativo"]