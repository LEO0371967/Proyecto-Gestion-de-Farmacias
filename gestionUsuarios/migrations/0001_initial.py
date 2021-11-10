# Generated by Django 3.2.8 on 2021-10-21 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestionStock', '0008_auto_20211020_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('cedula_de_identidad', models.IntegerField(help_text='Para todo usuario es el numero de CI', primary_key=True, serialize=False, verbose_name='c.i.')),
                ('usuario', models.CharField(max_length=20, unique=True, verbose_name='Nombre de usuario')),
                ('password', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('usuario_activo', models.BooleanField(default=True)),
                ('usuario_administrador', models.BooleanField(default=False)),
                ('sexo', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_de_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('departmento', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionUsuarios.roles')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recetas',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=500, null=True)),
                ('vencimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de vencimiento')),
                ('estado', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionStock.medicamentos')),
                ('medico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='gestionUsuarios.usuarios')),
                ('paciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionUsuarios.usuarios')),
            ],
        ),
    ]