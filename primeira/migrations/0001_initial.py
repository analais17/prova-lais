# Generated by Django 2.2.4 on 2019-09-13 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho_De_Compras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacidade', models.CharField(max_length=50)),
                ('valor_carrinho', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=11)),
                ('cpf', models.CharField(max_length=10)),
                ('carrinho_de_compras', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='primeira.Carrinho_De_Compras')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('preco', models.CharField(max_length=11)),
                ('quantidade', models.CharField(max_length=10)),
                ('carrinho_de_compras', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primeira.Carrinho_De_Compras')),
            ],
        ),
    ]