# Generated by Django 3.2.8 on 2021-10-14 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionStock', '0005_lotes_ingreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='lotes',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='lotes',
            name='medicamento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestionStock.medicamentos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lotes',
            name='ubicacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestionStock.farmacias'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lotes',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de edición'),
        ),
        migrations.AlterField(
            model_name='lotes',
            name='ingreso',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de ingreso'),
        ),
        migrations.AlterField(
            model_name='lotes',
            name='vencimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de vencimiento'),
        ),
    ]
