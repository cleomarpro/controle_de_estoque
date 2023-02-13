# Generated by Django 4.0.4 on 2022-06-21 11:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=50)),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
                ('usuarios', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=30)),
                ('codigo', models.CharField(max_length=13)),
                ('percentagem_de_lucro', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('valor_venal', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('valor_compra', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('entrada', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('saida', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('estoque', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('data_hora', models.DateTimeField(default=django.utils.timezone.now)),
                ('imagem', models.ImageField(blank=True, upload_to='')),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
                ('categoria', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='produto.categoria', verbose_name='Categoria')),
                ('usuarios', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='SaidaMercadoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=2, default=1, max_digits=9)),
                ('data_hora', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
                ('usuarios', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='EntradaMercadoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=2, default=1, max_digits=9)),
                ('data_hora', models.DateTimeField(default=django.utils.timezone.now)),
                ('validade_produto', models.DateField(blank=True, null=True)),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
                ('usuarios', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuarios')),
            ],
        ),
    ]
