# Generated by Django 2.1.1 on 2019-05-31 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, verbose_name='Nome')),
                ('descricao_habilidade', models.CharField(max_length=200, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.FileField(upload_to='fotos/')),
                ('nome', models.CharField(max_length=120)),
                ('pontos_de_vida', models.PositiveIntegerField(verbose_name='Vida')),
                ('pontos_de_ataque', models.PositiveIntegerField(verbose_name='Ataque')),
                ('pontos_de_defesa', models.PositiveIntegerField(verbose_name='Defesa')),
                ('pontos_de_velocidade', models.PositiveIntegerField(verbose_name='Velocidade')),
                ('ataque_especial', models.PositiveIntegerField(verbose_name='Ataque Especial')),
                ('defesa_especial', models.PositiveIntegerField(verbose_name='Defesa Especial')),
                ('peso', models.FloatField(verbose_name='Peso')),
                ('fk_habilidade', models.ManyToManyField(to='pokedex.Habilidade')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('descricao_tipo', models.CharField(max_length=200, verbose_name='Descrição')),
            ],
        ),
        migrations.AddField(
            model_name='pokemon',
            name='fk_tipo',
            field=models.ManyToManyField(to='pokedex.Tipo'),
        ),
    ]
