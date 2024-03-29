# Generated by Django 4.1.6 on 2023-03-11 17:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EntradaMercadoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=2, default=1, max_digits=9)),
                ('data_hora', models.DateTimeField(default=django.utils.timezone.now)),
                ('validade_produto', models.DateField(blank=True, null=True)),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
