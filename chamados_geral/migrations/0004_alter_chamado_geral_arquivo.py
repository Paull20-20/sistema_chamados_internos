# Generated by Django 4.0.1 on 2022-02-10 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamados_geral', '0003_chamado_geral_arquivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado_geral',
            name='Arquivo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
