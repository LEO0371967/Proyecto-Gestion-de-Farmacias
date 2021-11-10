# Generated by Django 3.2.8 on 2021-10-23 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionUsuarios', '0004_alter_recetas_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recetas',
            name='estado',
            field=models.CharField(blank=True, choices=[('RES', 'Reservado'), ('RET', 'Retirado')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='roles',
            name='descripcion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='apellido',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='cedula_de_identidad',
            field=models.IntegerField(help_text='Para todo usuario es el numero de c.i.', primary_key=True, serialize=False, verbose_name='c.i.'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
