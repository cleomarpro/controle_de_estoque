# Generated by Django 4.0.4 on 2022-06-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='saidamercadoria',
            name='estoque_fisico_atual',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9),
        ),
    ]
