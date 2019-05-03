# Generated by Django 2.2.1 on 2019-05-03 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='pokemon',
            name='fk_categoria',
            field=models.ForeignKey(default='Normal', on_delete=django.db.models.deletion.PROTECT, to='pokedex.Tipo'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='fk_habilidades',
            field=models.ManyToManyField(to='pokedex.Habilidade'),
        ),
    ]
