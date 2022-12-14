# Generated by Django 4.1.1 on 2022-09-12 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colores',
            fields=[
                ('id_color', models.AutoField(primary_key=True, serialize=False)),
                ('nom_color', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'colores',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id_departamento', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_departamento', models.CharField(max_length=120)),
            ],
            options={
                'db_table': 'departamentos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('id_genero', models.AutoField(primary_key=True, serialize=False)),
                ('nom_genero', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'generos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id_mascota', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('foto', models.CharField(max_length=500)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'mascotas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Municipios',
            fields=[
                ('id_municipio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_municipio', models.CharField(max_length=120)),
            ],
            options={
                'db_table': 'municipios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id_persona', models.AutoField(primary_key=True, serialize=False)),
                ('primer_nombre', models.CharField(max_length=20)),
                ('segundo_nombre', models.CharField(blank=True, max_length=20, null=True)),
                ('primer_apellido', models.CharField(max_length=20)),
                ('segundo_apellido', models.CharField(blank=True, max_length=20, null=True)),
                ('telefono', models.CharField(max_length=11)),
                ('direccion', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'personas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Razas',
            fields=[
                ('id_raza', models.AutoField(primary_key=True, serialize=False)),
                ('nom_raza', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'razas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegistroPerdidas',
            fields=[
                ('id_registro_perdida', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_perdida', models.DateField(blank=True, null=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('estado_registro', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'registro_perdidas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sexos',
            fields=[
                ('id_sexo', models.AutoField(primary_key=True, serialize=False)),
                ('nom_sexo', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'sexos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tamanios',
            fields=[
                ('id_tamanio', models.AutoField(primary_key=True, serialize=False)),
                ('nom_tamanio', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'tamanios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TiposMascota',
            fields=[
                ('id_tipo_mascota', models.AutoField(primary_key=True, serialize=False)),
                ('nom_tipo_mascota', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'tipos_mascota',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=100)),
                ('clave', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'usuarios',
                'managed': False,
            },
        ),
    ]
