# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Opinion(models.Model):
    id_usuario = models.OneToOneField('Usuarios', models.DO_NOTHING, db_column='Id_Usuario', primary_key=True)  # Field name made lowercase.
    id_pagina = models.ForeignKey('Pagina', models.DO_NOTHING, db_column='Id_Pagina', blank=True, null=True)  # Field name made lowercase.
    comentario = models.CharField(db_column='Comentario', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Opinion'


class Pagina(models.Model):
    id_pagina = models.AutoField(db_column='Id_Pagina', primary_key=True)  # Field name made lowercase.
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Id_Usuario', blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    name_servers = models.CharField(max_length=100, blank=True, null=True)
    registrar = models.CharField(max_length=100, blank=True, null=True)
    registrant_name = models.CharField(max_length=100, blank=True, null=True)
    registrant_city = models.CharField(max_length=80, blank=True, null=True)
    registrant_state = models.CharField(max_length=80, blank=True, null=True)
    registrant_country = models.CharField(max_length=80, blank=True, null=True)
    admin = models.CharField(max_length=100, blank=True, null=True)
    admin_city = models.CharField(max_length=80, blank=True, null=True)
    admin_country = models.CharField(max_length=80, blank=True, null=True)
    admin_state = models.CharField(max_length=80, blank=True, null=True)
    tech_name = models.CharField(max_length=80, blank=True, null=True)
    tech_city = models.CharField(max_length=80, blank=True, null=True)
    tech_state = models.CharField(max_length=80, blank=True, null=True)
    tech_country = models.CharField(max_length=80, blank=True, null=True)
    biling_name = models.CharField(max_length=80, blank=True, null=True)
    biling_city = models.CharField(max_length=80, blank=True, null=True)
    biling_state = models.CharField(max_length=80, blank=True, null=True)
    domain_name = models.CharField(max_length=100, blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    estatus = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Pagina'


class Rfc(models.Model):
    id_usuario = models.OneToOneField('Usuarios', models.DO_NOTHING, db_column='Id_Usuario', primary_key=True)  # Field name made lowercase.
    rfc = models.CharField(db_column='RFC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estatus = models.CharField(db_column='Estatus', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RFC'


class Usuarios(models.Model):
    REQUIRED_FIELDS = ['nombre']
    USERNAME_FIELD = 'correo'
    is_anonymous = True
    is_authenticated = False
    id_usuario = models.AutoField(db_column='Id_Usuario', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=50, blank=True, null=True, unique=True)  # Field name made lowercase.
    contraseña = models.CharField(db_column='Contraseña', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuarios'


class Validacion(models.Model):
    id_pagina = models.OneToOneField(Pagina, models.DO_NOTHING, db_column='Id_Pagina', primary_key=True)  # Field name made lowercase.
    estatus = models.CharField(db_column='Estatus', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Validacion'
