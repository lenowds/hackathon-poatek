# Generated by Django 3.2.5 on 2021-07-20 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estabelecimentoproduto',
            name='id_estabelecimento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='marketplace.estabelecimento'),
            preserve_default=False,
        ),
    ]
