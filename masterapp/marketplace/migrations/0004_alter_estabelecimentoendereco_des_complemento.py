# Generated by Django 3.2.5 on 2021-07-21 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_auto_20210720_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estabelecimentoendereco',
            name='des_complemento',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
