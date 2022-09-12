# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Colores(models.Model):
    id_color = models.AutoField(primary_key=True)
    nom_color = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'colores'


class Departamentos(models.Model):
    id_departamento = models.IntegerField(primary_key=True)
    nombre_departamento = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'departamentos'


class Generos(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nom_genero = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'generos'


class Mascotas(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    foto = models.CharField(max_length=500)
    descripcion = models.CharField(max_length=200)
    id_tipo_mascota_fk = models.ForeignKey('TiposMascota', models.DO_NOTHING, db_column='id_tipo_mascota_fk')
    id_sexo_fk = models.ForeignKey('Sexos', models.DO_NOTHING, db_column='id_sexo_fk')
    id_tamanio_fk = models.ForeignKey('Tamanios', models.DO_NOTHING, db_column='id_tamanio_fk')
    id_color_fk = models.ForeignKey(Colores, models.DO_NOTHING, db_column='id_color_fk')
    id_raza_fk = models.ForeignKey('Razas', models.DO_NOTHING, db_column='id_raza_fk')

    class Meta:
        managed = False
        db_table = 'mascotas'


class Municipios(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    nombre_municipio = models.CharField(max_length=120)
    id_departamento_fk = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='id_departamento_fk')

    class Meta:
        managed = False
        db_table = 'municipios'


class Personas(models.Model):
    id_persona = models.AutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20, blank=True, null=True)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=11)
    direccion = models.CharField(max_length=50)
    correo = models.CharField(max_length=40)
    id_genero_fk = models.ForeignKey(Generos, models.DO_NOTHING, db_column='id_genero_fk')

    class Meta:
        managed = False
        db_table = 'personas'


class Razas(models.Model):
    id_raza = models.AutoField(primary_key=True)
    nom_raza = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'razas'


class RegistroPerdidas(models.Model):
    id_registro_perdida = models.AutoField(primary_key=True)
    id_persona_fk = models.ForeignKey(Personas, models.DO_NOTHING, db_column='id_persona_fk')
    id_mascota_fk = models.ForeignKey(Mascotas, models.DO_NOTHING, db_column='id_mascota_fk')
    id_municipio_fk = models.ForeignKey(Municipios, models.DO_NOTHING, db_column='id_municipio_fk')
    fecha_perdida = models.DateField(blank=True, null=True)
    descripcion = models.CharField(max_length=200)
    estado_registro = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'registro_perdidas'


class Sexos(models.Model):
    id_sexo = models.AutoField(primary_key=True)
    nom_sexo = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'sexos'


class Tamanios(models.Model):
    id_tamanio = models.AutoField(primary_key=True)
    nom_tamanio = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tamanios'


class TiposMascota(models.Model):
    id_tipo_mascota = models.AutoField(primary_key=True)
    nom_tipo_mascota = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tipos_mascota'


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=100)
    clave = models.CharField(max_length=200)
    id_persona_fk = models.ForeignKey(Personas, models.DO_NOTHING, db_column='id_persona_fk')

    class Meta:
        managed = False
        db_table = 'usuarios'
