# Generated by Django 5.0.4 on 2024-04-08 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_SIGApoio', '0012_alter_emprestimo_horasaida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='horaEntrada',
            field=models.DateTimeField(default=''),
        ),
    ]
