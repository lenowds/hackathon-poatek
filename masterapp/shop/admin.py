from django.contrib import admin

from django.contrib import auth
from django.contrib.auth import admin as auth_admin
from .models import TipoEndereco


@admin.register(TipoEndereco)
class TipoEnderecoAdmin(admin.ModelAdmin):
    list_display = ["des_tipo_endereco", "created", "modified"]