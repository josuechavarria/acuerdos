# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Directivacentral(models.Model):
    codigo = models.CharField(max_length=1, blank=True)
    codigo_centro = models.CharField(max_length=255, blank=True)
    cuenta = models.CharField(max_length=255, blank=True)
    horas_plaza = models.CharField(max_length=2, blank=True)
    identidad_empleado = models.CharField(max_length=255, blank=True)
    nombres_empleado = models.CharField(max_length=255, blank=True)
    apellidos_empleado = models.CharField(max_length=255, blank=True)
    codigo_cargo = models.CharField(max_length=15, blank=True)
    descripcion_cargo = models.CharField(max_length=255, blank=True)
    codigo_transaccion = models.CharField(max_length=2, blank=True)
    monto_2005 = models.TextField(blank=True) # This field type is a guess.
    monto_anual_2006 = models.TextField(blank=True) # This field type is a guess.
    monto_2006 = models.TextField(blank=True) # This field type is a guess.
    monto_corregido_2006 = models.TextField(db_column='Monto_Corregido_2006', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'DIRECTIVACENTRAL'

class Directivadepartamenta(models.Model):
    codigo = models.CharField(max_length=1, blank=True)
    codigo_centro = models.CharField(max_length=255, blank=True)
    cuenta = models.CharField(max_length=255, blank=True)
    horas_plaza = models.CharField(max_length=2, blank=True)
    identidad_empleado = models.CharField(max_length=255, blank=True)
    nombres_empleado = models.CharField(max_length=255, blank=True)
    apellidos_empleado = models.CharField(max_length=255, blank=True)
    codigo_cargo = models.CharField(max_length=15, blank=True)
    descripcion_cargo = models.CharField(max_length=255, blank=True)
    codigo_transaccion = models.CharField(max_length=2, blank=True)
    monto_2005 = models.TextField(blank=True) # This field type is a guess.
    monto_anual_2006 = models.TextField(blank=True) # This field type is a guess.
    monto_2006 = models.TextField(blank=True) # This field type is a guess.
    monto_corregido_2006 = models.TextField(db_column='Monto_Corregido_2006', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'DIRECTIVADEPARTAMENTA'

class DirectDeptalDesglosado(models.Model):
    codigo = models.CharField(max_length=5, blank=True)
    descripcion_centro = models.CharField(max_length=100, blank=True)
    cuenta = models.CharField(max_length=50, blank=True)
    horas = models.IntegerField(blank=True, null=True)
    identidad = models.CharField(max_length=15, blank=True)
    codigo_cargo = models.CharField(max_length=15, blank=True)
    descripcion_cargo = models.CharField(max_length=100, blank=True)
    nombres_empleado = models.CharField(max_length=100, blank=True)
    apellidos_empleado = models.CharField(max_length=100, blank=True)
    cod_tran = models.IntegerField(blank=True, null=True)
    transaccion = models.CharField(db_column='Transaccion', max_length=100, blank=True) # Field name made lowercase.
    a_o2005 = models.TextField(db_column='A\xf1o2005', blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    a_o2006 = models.TextField(db_column='A\xf1o2006', blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    correccion = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        managed = False
        db_table = 'DIRECT_DEPTAL_Desglosado'

class DirecCentralDesglose(models.Model):
    codigo = models.CharField(max_length=5, blank=True)
    descripcion_centro = models.CharField(max_length=100, blank=True)
    cuenta = models.CharField(max_length=50, blank=True)
    horas = models.IntegerField(blank=True, null=True)
    identidad_empleado = models.CharField(max_length=15, blank=True)
    codigo_cargo = models.CharField(max_length=15, blank=True)
    descripcion_cargo = models.CharField(max_length=100, blank=True)
    nombres_empleado = models.CharField(max_length=100, blank=True)
    apellidos_empleado = models.CharField(max_length=100, blank=True)
    cod_tran = models.IntegerField(blank=True, null=True)
    transaccion = models.CharField(db_column='Transaccion', max_length=2, blank=True) # Field name made lowercase.
    anio2005 = models.TextField(db_column='Anio2005', blank=True) # Field name made lowercase. This field type is a guess.
    anio2006 = models.TextField(db_column='Anio2006', blank=True) # Field name made lowercase. This field type is a guess.
    correcion = models.TextField(db_column='CORRECION', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'Direc_central_desglose'

class MatrizNuevaRecuperar(models.Model):
    sip_old = models.CharField(max_length=50, blank=True)
    siafi_old = models.CharField(max_length=50, blank=True)
    anio = models.CharField(max_length=4, blank=True)
    siafi_new = models.CharField(max_length=50, blank=True)
    pad_new = models.CharField(max_length=5, blank=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    sip_titulo = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    sip_programa = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    sip_subprograma = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    sip_actividad = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    sip_fondo = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    sip_renglon = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    sip_objeto = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    siafi_institucion = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    siafi_ga = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    siafi_ue = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    siafi_programa = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    siafi_subprograma = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    siafi_proyecto = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    siafi_actividad = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    siafi_fuente = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    siafi_org_fin = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    siafi_partida = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    siafi_beneficiario = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    sip_new = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'Matriz_Nueva_Recuperar'

class MatrizCarga2(models.Model):
    anio = models.CharField(max_length=4, blank=True)
    sip = models.CharField(max_length=50, blank=True)
    pad = models.CharField(max_length=5, blank=True)
    siafi = models.CharField(max_length=50, blank=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    sip_titulo = models.CharField(max_length=3, blank=True)
    sip_programa = models.CharField(max_length=3, blank=True)
    sip_subprograma = models.CharField(max_length=2, blank=True)
    sip_actividad = models.CharField(max_length=2, blank=True)
    sip_fondo = models.CharField(max_length=2, blank=True)
    sip_renglon = models.CharField(max_length=3, blank=True)
    sip_objeto = models.CharField(max_length=3, blank=True)
    siafi_institucion = models.CharField(max_length=4, blank=True)
    siafi_ga = models.CharField(max_length=3, blank=True)
    siafi_ue = models.CharField(max_length=3, blank=True)
    siafi_programa = models.CharField(max_length=2, blank=True)
    siafi_subprograma = models.CharField(max_length=2, blank=True)
    siafi_proyecto = models.CharField(max_length=3, blank=True)
    siafi_actividad = models.CharField(max_length=3, blank=True)
    siafi_fuente = models.CharField(max_length=2, blank=True)
    siafi_org_fin = models.CharField(max_length=3, blank=True)
    siafi_partida = models.CharField(max_length=5, blank=True)
    siafi_beneficiario = models.CharField(max_length=4, blank=True)
    class Meta:
        managed = False
        db_table = 'Matriz_carga2'

class Mora1(models.Model):
    sector = models.TextField(db_column='Sector', blank=True) # Field name made lowercase. This field type is a guess.
    departamento = models.TextField(db_column='Departamento', blank=True) # Field name made lowercase. This field type is a guess.
    municipio = models.TextField(db_column='Municipio', blank=True) # Field name made lowercase. This field type is a guess.
    prestamo = models.TextField(db_column='Prestamo', blank=True) # Field name made lowercase. This field type is a guess.
    identidad = models.CharField(db_column='Identidad', max_length=20, blank=True) # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=255, blank=True) # Field name made lowercase.
    plazo = models.TextField(db_column='Plazo', blank=True) # Field name made lowercase. This field type is a guess.
    cuota = models.TextField(db_column='Cuota', blank=True) # Field name made lowercase. This field type is a guess.
    en_mora = models.TextField(db_column='en_Mora', blank=True) # Field name made lowercase. This field type is a guess.
    mora = models.TextField(db_column='Mora', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'Mora1'

class VPlazasVacantes(models.Model):
    cuenta = models.CharField(max_length=50)
    horas_plaza = models.IntegerField(blank=True, null=True)
    estado_plaza = models.SmallIntegerField()
    descripcion_estado = models.CharField(max_length=50)
    institucion = models.IntegerField()
    programa = models.IntegerField()
    subprograma = models.IntegerField()
    fuente = models.IntegerField()
    departamento = models.CharField(db_column='Departamento', max_length=2, blank=True) # Field name made lowercase.
    municipio = models.CharField(db_column='Municipio', max_length=2, blank=True) # Field name made lowercase.
    centro_educativo = models.CharField(db_column='Centro_Educativo', max_length=5, blank=True) # Field name made lowercase.
    nro_plaza = models.CharField(db_column='Nro_Plaza', max_length=6, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'V_Plazas_Vacantes'

class DepAldeas(models.Model):
    codigo_departamento = models.CharField(max_length=2)
    codigo_municipio = models.CharField(max_length=2)
    codigo_ine = models.CharField(max_length=3)
    codigo_gobernacion = models.CharField(max_length=3)
    descripcion_gobernacion = models.CharField(max_length=50)
    usuario_enlazo_ine = models.CharField(max_length=25, blank=True)
    fecha_enlazo_ine = models.DateTimeField(blank=True, null=True)
    usuario_enlazo_gob = models.CharField(max_length=25, blank=True)
    fecha_enlazo_gob = models.DateTimeField(blank=True, null=True)
    descripcion_ine = models.CharField(max_length=50)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    enlazado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'dep_aldeas'

class DepAldeasCargadas(models.Model):
    codigo_institucion = models.IntegerField()
    codigo_departamento = models.CharField(max_length=2)
    codigo_municipio = models.CharField(max_length=2)
    codigo_aldea = models.CharField(max_length=2)
    descripcion_aldea = models.CharField(max_length=100)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    agregado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'dep_aldeas_cargadas'

class DepBitacoraCambio(models.Model):
    identidad = models.CharField(max_length=13)
    codigo_problema = models.IntegerField()
    usuario_creacion = models.CharField(max_length=35)
    fecha_creacion = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'dep_bitacora_cambio'

class DepCaserios(models.Model):
    codigo_departamento = models.CharField(max_length=2)
    codigo_municipio = models.CharField(max_length=2)
    codigo_aldea = models.CharField(max_length=3)
    codigo_ine = models.CharField(max_length=3)
    codigo_gobernacion = models.CharField(max_length=3)
    descripcion_gobernacion = models.CharField(max_length=50)
    usuario_enlazo_ine = models.CharField(max_length=25, blank=True)
    fecha_enlazo_ine = models.DateTimeField(blank=True, null=True)
    usuario_enlazo_gob = models.CharField(max_length=25, blank=True)
    fecha_enlazo_gob = models.DateTimeField(blank=True, null=True)
    descripcion_ine = models.CharField(max_length=50)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    enlazado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'dep_caserios'

class DepCaseriosCargados(models.Model):
    codigo_institucion = models.IntegerField()
    codigo_departamento = models.CharField(max_length=2)
    codigo_municipio = models.CharField(max_length=2)
    codigo_aldea = models.CharField(max_length=2)
    codigo_caserio = models.CharField(max_length=3)
    descripcion_caserio = models.CharField(max_length=100)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    agregado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'dep_caserios_cargados'

class DepCentrosEducativosEnlace(models.Model):
    codigo_departamento_siarhd = models.CharField(max_length=2)
    codigo_municipio_siarhd = models.CharField(max_length=2)
    codigo_centro_siarhd = models.CharField(max_length=5)
    codigo_departamento_ee = models.IntegerField()
    codigo_municipio_ee = models.IntegerField()
    codigo_centro_ee = models.DecimalField(max_digits=19, decimal_places=0)
    codigo_aldea_ee = models.IntegerField()
    codigo_caserio_ee = models.IntegerField()
    codigo_plantel = models.IntegerField(blank=True, null=True)
    enlace_definitivo = models.CharField(max_length=1)
    usuario_enlazo = models.CharField(max_length=25, blank=True)
    fecha_enlazo = models.DateTimeField(blank=True, null=True)
    cambio_centros_ee = models.CharField(max_length=1, blank=True)
    depto_ee_anterior = models.IntegerField(blank=True, null=True)
    muni_ee_anterior = models.IntegerField(blank=True, null=True)
    centro_ee_anterior = models.IntegerField(blank=True, null=True)
    codigo_muni_siarhd_anterior = models.CharField(max_length=2, blank=True)
    codigo_centro_siarhd_anterior = models.CharField(max_length=2, blank=True)
    municipio_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'dep_centros_educativos_enlace'

class DepCentrosEe(models.Model):
    codigo_depto_ee = models.IntegerField()
    desc_departamento_ee = models.CharField(max_length=60, blank=True)
    codigo_municipio_ee = models.IntegerField()
    desc_municipio_ee = models.CharField(max_length=50, blank=True)
    codigo_aldea_ee = models.IntegerField()
    desc_aldea_ee = models.CharField(max_length=60, blank=True)
    codigo_caserio_ee = models.IntegerField()
    desc_caserio_ee = models.CharField(max_length=50, blank=True)
    codigo_centro_ee = models.DecimalField(max_digits=10, decimal_places=0)
    nombre_centro_ee = models.CharField(max_length=80, blank=True)
    tipo_admin_ee = models.SmallIntegerField(blank=True, null=True)
    direccion_ee = models.CharField(max_length=100, blank=True)
    codigo_plantel_ee = models.IntegerField(blank=True, null=True)
    codigo_depto_een = models.IntegerField(blank=True, null=True)
    codigo_municipio_een = models.IntegerField(blank=True, null=True)
    codigo_centro_een = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    cambio_centro_ee = models.CharField(max_length=1, blank=True)
    centro_ee_anterior = models.IntegerField(blank=True, null=True)
    depto_ee_anterior = models.IntegerField(blank=True, null=True)
    muni_anterior_ee = models.IntegerField(blank=True, null=True)
    codigo_administracion = models.IntegerField(blank=True, null=True)
    desc_administracion = models.CharField(max_length=12, blank=True)
    codigo_area = models.IntegerField(blank=True, null=True)
    desc_area = models.CharField(max_length=20, blank=True)
    codigo_tipo_organizacion = models.IntegerField(blank=True, null=True)
    desc_tipo_organizacion = models.CharField(max_length=100, blank=True)
    codigo_tipo_centro = models.IntegerField(blank=True, null=True)
    desc_tipo_centro = models.CharField(max_length=50, blank=True)
    numero_fax = models.CharField(max_length=9, blank=True)
    numero_telefono = models.CharField(max_length=9, blank=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'dep_centros_ee'

class DepCentroseeSecuenciados(models.Model):
    codigo_departamento = models.IntegerField(db_column='Codigo_Departamento', blank=True, null=True) # Field name made lowercase.
    codigo_municipio = models.IntegerField(db_column='Codigo_Municipio', blank=True, null=True) # Field name made lowercase.
    codigo_centro = models.DecimalField(db_column='Codigo_Centro', max_digits=18, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    codigo_departamento_nuevo = models.IntegerField(db_column='Codigo_Departamento_Nuevo', blank=True, null=True) # Field name made lowercase.
    codigo_municipio_nuevo = models.IntegerField(db_column='Codigo_Municipio_Nuevo', blank=True, null=True) # Field name made lowercase.
    codigo_centro_nuevo = models.DecimalField(db_column='Codigo_Centro_Nuevo', max_digits=18, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'dep_centrosee_secuenciados'

class DepColonias(models.Model):
    codigo_departamento = models.CharField(max_length=2)
    codigo_municipio = models.CharField(max_length=2)
    codigo_aldea = models.CharField(max_length=3)
    codigo_ine = models.CharField(max_length=3)
    codigo_gobernacion = models.CharField(max_length=3)
    descripcion_gobernacion = models.CharField(max_length=50)
    usuario_enlazo_ine = models.CharField(max_length=25, blank=True)
    fecha_enlazo_ine = models.DateTimeField(blank=True, null=True)
    usuario_enlazo_gob = models.CharField(max_length=25, blank=True)
    fecha_enlazo_gob = models.DateTimeField(blank=True, null=True)
    descripcion_ine = models.CharField(max_length=50)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    enlazado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'dep_colonias'

class DepColoniasCargadas(models.Model):
    codigo_institucion = models.IntegerField()
    codigo_departamento = models.CharField(max_length=2)
    codigo_municipio = models.CharField(max_length=2)
    codigo_aldea = models.CharField(max_length=2)
    codigo_colonia = models.CharField(max_length=3)
    descripcion_colonia = models.CharField(max_length=100)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    agregado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'dep_colonias_cargadas'

class DepContenedorImagenes(models.Model):
    identidad = models.CharField(max_length=13, blank=True)
    nombre = models.CharField(max_length=80, blank=True)
    numero_acuerdos = models.IntegerField(blank=True, null=True)
    numero_estudio_exp = models.IntegerField(blank=True, null=True)
    numero_doc_personales = models.IntegerField(blank=True, null=True)
    numero_titulos = models.IntegerField(blank=True, null=True)
    numero_foto = models.IntegerField(blank=True, null=True)
    numero_formulario = models.IntegerField(blank=True, null=True)
    numero_quinquenios = models.IntegerField(blank=True, null=True)
    numero_reparos = models.IntegerField(blank=True, null=True)
    numero_resol_categoria = models.IntegerField(blank=True, null=True)
    numero_otros = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'dep_contenedor_imagenes'

class DepDepartamentos(models.Model):
    codigo_siarhd = models.CharField(max_length=2)
    codigo_ine = models.CharField(max_length=2)
    codigo_gobernacion = models.CharField(max_length=2)
    descripcion_gobernacion = models.CharField(max_length=25)
    usuario_enlazo_siarhd = models.CharField(max_length=25, blank=True)
    fecha_enlazo_siarhd = models.DateTimeField(blank=True, null=True)
    usuario_enlazo_ine = models.CharField(max_length=25, blank=True)
    fecha_enlazo_ine = models.DateTimeField(blank=True, null=True)
    usuario_enlazo_gob = models.CharField(max_length=25, blank=True)
    fecha_enlazo_gob = models.DateTimeField(blank=True, null=True)
    descripcion_ine = models.CharField(max_length=25)
    descripcion_siarhd = models.CharField(max_length=25)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    enlazado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'dep_departamentos'

class DepDepartamentosCargados(models.Model):
    codigo_institucion = models.IntegerField()
    codigo_departamento = models.CharField(max_length=2)
    descripcion_departamento = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'dep_departamentos_cargados'

class DepDocentesCambio(models.Model):
    identidad_actual = models.CharField(primary_key=True, max_length=13)
    identidad_dep = models.CharField(max_length=13, blank=True)
    nombres_dep = models.CharField(max_length=35, blank=True)
    apellidos_dep = models.CharField(max_length=35, blank=True)
    clave_escalafon_dep = models.CharField(max_length=15, blank=True)
    usuario_creacion = models.CharField(max_length=35)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=35, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    ultima_categoria_dep = models.IntegerField(blank=True, null=True)
    codigo_nivel_educativo_dep = models.IntegerField(blank=True, null=True)
    fecha_nacimiento_dep = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'dep_docentes_cambio'

class DepDocentesEe(models.Model):
    a_o_estadisticas = models.IntegerField(db_column='a\xf1o_estadisticas') # Field renamed to remove unsuitable characters.
    tipo_estadisticas = models.CharField(max_length=2)
    codigo_departamento = models.IntegerField()
    codigo_municipio = models.IntegerField()
    codigo_centro_viejo_s = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    codigo_centro = models.DecimalField(max_digits=18, decimal_places=0)
    numero_identidad = models.CharField(max_length=13)
    nombre_docente = models.CharField(max_length=70)
    sexo = models.CharField(max_length=1)
    nacionalidad = models.CharField(max_length=1)
    clave_escalafon_alfanumerica1 = models.CharField(max_length=2, blank=True)
    clave_escalafon_alfanumerica2 = models.CharField(max_length=2, blank=True)
    clave_escalafon_numerica = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    codigo_cargo = models.CharField(max_length=7, blank=True)
    codigo_area = models.IntegerField(blank=True, null=True)
    codigo_modalidad = models.IntegerField(blank=True, null=True)
    horas_clase = models.IntegerField(blank=True, null=True)
    grado1 = models.IntegerField(blank=True, null=True)
    grado2 = models.IntegerField(blank=True, null=True)
    grado3 = models.IntegerField(blank=True, null=True)
    grado4 = models.IntegerField(blank=True, null=True)
    grado5 = models.IntegerField(blank=True, null=True)
    grado6 = models.IntegerField(blank=True, null=True)
    grado7 = models.IntegerField(blank=True, null=True)
    grado8 = models.IntegerField(blank=True, null=True)
    grado9 = models.IntegerField(blank=True, null=True)
    jor_vespertina = models.IntegerField(db_column='jor_Vespertina', blank=True, null=True) # Field name made lowercase.
    jor_matutina = models.IntegerField(db_column='jor_Matutina', blank=True, null=True) # Field name made lowercase.
    jor_nocturna = models.IntegerField(db_column='jor_Nocturna', blank=True, null=True) # Field name made lowercase.
    jor_doble = models.IntegerField(db_column='jor_Doble', blank=True, null=True) # Field name made lowercase.
    tit_mep = models.IntegerField(db_column='tit_Mep', blank=True, null=True) # Field name made lowercase.
    tit_me = models.IntegerField(db_column='tit_Me', blank=True, null=True) # Field name made lowercase.
    tit_st = models.IntegerField(db_column='tit_St', blank=True, null=True) # Field name made lowercase.
    tit_pem = models.IntegerField(blank=True, null=True)
    tit_tu = models.IntegerField(db_column='tit_Tu', blank=True, null=True) # Field name made lowercase.
    tit_lic = models.IntegerField(db_column='tit_Lic', blank=True, null=True) # Field name made lowercase.
    tit_mae = models.IntegerField(db_column='tit_Mae', blank=True, null=True) # Field name made lowercase.
    tit_doc = models.IntegerField(db_column='tit_Doc', blank=True, null=True) # Field name made lowercase.
    encontrado_siarhd = models.IntegerField(blank=True, null=True)
    encontrado_rnp = models.IntegerField(blank=True, null=True)
    nombre_diferente_siarhd_rnp = models.IntegerField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=10, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_actualizacion = models.CharField(max_length=10, blank=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'dep_docentes_ee'

class DepDocentesInprema(models.Model):
    identidad_empleado = models.CharField(max_length=13)
    nombres_empleado = models.CharField(max_length=120)
    fecha = models.DateTimeField()
    tipo_beneficio = models.CharField(max_length=20)
    codigo_tipo_beneficio = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'dep_docentes_inprema'

class DepDocentesInprema2(models.Model):
    identidad = models.CharField(max_length=13, blank=True)
    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    codigo_tipo_beneficio = models.IntegerField(blank=True, null=True)
    descripcion_tipo_beneficio = models.CharField(max_length=30, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    fecha_fallecimiento = models.DateTimeField(blank=True, null=True)
    fecha_resolucion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'dep_docentes_inprema_2'

class DepDocentesSiarhd(models.Model):
    anio = models.IntegerField()
    identidad_empleado = models.CharField(max_length=13)
    cuenta = models.CharField(max_length=50)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    municipio_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'dep_docentes_siarhd'

class DepGobernacion(models.Model):
    codigo = models.CharField(max_length=6)
    descripcion = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'dep_gobernacion'

class DepIne(models.Model):
    depto = models.CharField(max_length=2, blank=True)
    desdepto = models.CharField(max_length=100, blank=True)
    muni = models.CharField(max_length=2, blank=True)
    desmuni = models.CharField(max_length=100, blank=True)
    aldea = models.CharField(max_length=2, blank=True)
    desaldea = models.CharField(max_length=100, blank=True)
    caserio = models.CharField(max_length=3, blank=True)
    descaserio = models.CharField(max_length=100, blank=True)
    colonia = models.CharField(max_length=3, blank=True)
    descolonia = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'dep_ine'

class DepInstitucionesListados(models.Model):
    codigo_institucion = models.IntegerField(primary_key=True)
    descripcion_institucion = models.CharField(max_length=50)
    observaciones = models.CharField(db_column='Observaciones', max_length=255, blank=True) # Field name made lowercase.
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'dep_instituciones_listados'

class DepMunicipios(models.Model):
    codigo_departamento = models.CharField(max_length=2)
    codigo_siarhd = models.CharField(max_length=2)
    codigo_ine = models.CharField(max_length=2)
    codigo_gobernacion = models.CharField(max_length=2)
    descripcion_gobernacion = models.CharField(max_length=25)
    usuario_enlazo_siarhd = models.CharField(max_length=25, blank=True)
    fecha_enlazo_siarhd = models.DateTimeField(blank=True, null=True)
    usuario_enlazo_ine = models.CharField(max_length=25, blank=True)
    fecha_enlazo_ine = models.DateTimeField(blank=True, null=True)
    usuario_enlazo_gob = models.CharField(max_length=25, blank=True)
    fecha_enlazo_gob = models.DateTimeField(blank=True, null=True)
    descripcion_ine = models.CharField(max_length=25)
    descripcion_siarhd = models.CharField(max_length=25)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    enlazado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'dep_municipios'

class DepMunicipiosCargados(models.Model):
    codigo_institucion = models.IntegerField()
    codigo_departamento = models.CharField(max_length=2)
    codigo_municipio = models.CharField(max_length=2)
    descripcion_municipio = models.CharField(max_length=100, blank=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    agregado = models.CharField(max_length=1, blank=True)
    observaciones = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'dep_municipios_cargados'

class DepNivelesEducativos(models.Model):
    codigo_nivel = models.IntegerField(primary_key=True)
    descripci_n_nivel = models.CharField(db_column='descripci\xc6n_nivel', max_length=60) # Field name made lowercase. Field renamed to remove unsuitable characters.
    cambio_centro_ee = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'dep_niveles_educativos'

class DepNivelesXCentro(models.Model):
    codigo_departamento = models.IntegerField()
    codigo_municipio = models.IntegerField()
    codigo_centro = models.IntegerField()
    codigo_aldea = models.IntegerField(blank=True, null=True)
    codigo_caserio = models.IntegerField(blank=True, null=True)
    codigo_plantel = models.IntegerField(blank=True, null=True)
    codigo_nivel_educativo = models.IntegerField()
    codigo_subnivel = models.IntegerField()
    cambio_centro_ee = models.CharField(max_length=1, blank=True)
    centro_ee_anterior = models.IntegerField(blank=True, null=True)
    muni_ee_anterior = models.IntegerField(blank=True, null=True)
    depto_ee_anterior = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'dep_niveles_x_centro'

class DepProblemasCambio(models.Model):
    codigo_problema = models.IntegerField(primary_key=True)
    descripcion_problema = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'dep_problemas_cambio'

class DepProblemasDepCambio(models.Model):
    identidad_empleado = models.CharField(max_length=13)
    codigo_problema = models.IntegerField()
    observacion = models.CharField(max_length=255, blank=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'dep_problemas_dep_cambio'

class DepSeguimientoTitulos(models.Model):
    codigo_histo_titulo = models.CharField(max_length=37)
    secuencial_estado = models.IntegerField()
    ultimo_estado_documento = models.SmallIntegerField()
    estado_anterior_documento = models.SmallIntegerField(blank=True, null=True)
    usuario_estado_anterior = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_estado_anterior = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'dep_seguimiento_titulos'

class DepSubnivelesEducativos(models.Model):
    codigo_nivel_educativo = models.IntegerField()
    codigo_subnivel_educativo = models.IntegerField()
    descripcion_subnivel = models.CharField(max_length=60)
    class Meta:
        managed = False
        db_table = 'dep_subniveles_educativos'

class DepTitulosCambio(models.Model):
    identidad_empleado = models.CharField(max_length=13)
    codigo_titulo = models.IntegerField()
    codigo_centro_estudio = models.IntegerField()
    tomo = models.CharField(max_length=15)
    folio = models.CharField(max_length=15)
    fecha_emision = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=35)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=35, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    codigo_pais = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'dep_titulos_cambio'

class Dtproperties(models.Model):
    id = models.AutoField(primary_key=True)
    objectid = models.IntegerField(blank=True, null=True)
    property = models.CharField(max_length=64)
    value = models.CharField(max_length=255, blank=True)
    uvalue = models.CharField(max_length=255, blank=True)
    lvalue = models.BinaryField(blank=True, null=True)
    version = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'dtproperties'

class Dual(models.Model):
    col1 = models.CharField(max_length=20, blank=True)
    nextval = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'dual'

class EeRnpCompleto(models.Model):
    identidad = models.CharField(db_column='Identidad', max_length=13) # Field name made lowercase.
    primer_nombre = models.CharField(db_column='Primer_Nombre', max_length=50, blank=True) # Field name made lowercase.
    segundo_nombre = models.CharField(db_column='Segundo_Nombre', max_length=50, blank=True) # Field name made lowercase.
    primer_apellido = models.CharField(db_column='Primer_Apellido', max_length=50, blank=True) # Field name made lowercase.
    segundo_apellido = models.CharField(db_column='Segundo_Apellido', max_length=50, blank=True) # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=1, blank=True) # Field name made lowercase.
    fecha_nacimiento_txt = models.CharField(db_column='Fecha_Nacimiento_txt', max_length=10, blank=True) # Field name made lowercase.
    departamento_domicilio = models.IntegerField(db_column='Departamento_Domicilio', blank=True, null=True) # Field name made lowercase.
    descripcion_departamento = models.CharField(db_column='Descripcion_Departamento', max_length=50, blank=True) # Field name made lowercase.
    municipio_domicilio = models.IntegerField(db_column='Municipio_Domicilio', blank=True, null=True) # Field name made lowercase.
    descripcion_municipio = models.CharField(db_column='Descripcion_Municipio', max_length=50, blank=True) # Field name made lowercase.
    colonia_domicilio = models.IntegerField(db_column='Colonia_Domicilio', blank=True, null=True) # Field name made lowercase.
    descripcion_colonia = models.CharField(db_column='Descripcion_Colonia', max_length=50, blank=True) # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=5, blank=True) # Field name made lowercase.
    fecha_nacimiento = models.DateTimeField(db_column='Fecha_Nacimiento', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ee_rnp_completo'

class HhCheques(models.Model):
    codigo_institucion = models.CharField(max_length=13, blank=True)
    codigo_periodo = models.CharField(max_length=6, blank=True)
    codigo_planilla = models.CharField(max_length=10, blank=True)
    identidad_empleado = models.CharField(max_length=13, blank=True)
    anio_cheque = models.CharField(max_length=4)
    tipo_pago_cheque = models.CharField(max_length=2)
    numero_cheque = models.CharField(max_length=6)
    beneficiario = models.CharField(max_length=100, blank=True)
    fecha_generacion_cheque = models.DateTimeField()
    fecha_emision_cheque = models.DateTimeField(blank=True, null=True)
    monto_cheque = models.DecimalField(max_digits=18, decimal_places=2)
    estado_cheque = models.SmallIntegerField()
    registro_cheque = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_anulacion_cheque = models.DateTimeField(blank=True, null=True)
    fecha_pago_cheque = models.DateTimeField(blank=True, null=True)
    codigo_identificador = models.CharField(max_length=13, blank=True)
    class Meta:
        managed = False
        db_table = 'hh_cheques'

class HhDepositos(models.Model):
    anio_deposito = models.CharField(max_length=4)
    tipo_deposito = models.CharField(max_length=2)
    numero_deposito = models.CharField(max_length=6)
    codigo_planilla = models.CharField(max_length=10, blank=True)
    codigo_periodo = models.CharField(max_length=6, blank=True)
    codigo_banco = models.IntegerField(blank=True, null=True)
    cuenta_bancaria = models.CharField(max_length=25, blank=True)
    codigo_institucion = models.CharField(max_length=13, blank=True)
    identidad_empleado = models.CharField(max_length=13, blank=True)
    beneficiario = models.CharField(max_length=100, blank=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    monto_deposito = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fecha_deposito = models.DateTimeField(blank=True, null=True)
    codigo_depto_deposito = models.CharField(max_length=2, blank=True)
    class Meta:
        managed = False
        db_table = 'hh_depositos'

class HhHistoMovimientos(models.Model):
    codigo_periodo = models.CharField(max_length=6)
    codigo_histo_movimiento = models.DateTimeField()
    identidad_empleado = models.CharField(max_length=13)
    codigo_movimiento = models.IntegerField()
    codigo_motivo = models.IntegerField()
    codigo_departamento = models.CharField(max_length=2, blank=True)
    codigo_municipio = models.CharField(max_length=2, blank=True)
    codigo_centro = models.CharField(max_length=5, blank=True)
    codigo_tipo_profesional = models.CharField(max_length=3, blank=True)
    fecha_inicial = models.DateTimeField(blank=True, null=True)
    fecha_final = models.DateTimeField(blank=True, null=True)
    plaza_primaria = models.CharField(max_length=50, blank=True)
    e_plaza_primaria_anterior = models.SmallIntegerField(blank=True, null=True)
    e_plaza_secundaria_anterior = models.SmallIntegerField(blank=True, null=True)
    plaza_secundaria = models.CharField(max_length=50, blank=True)
    plaza_actual = models.SmallIntegerField(blank=True, null=True)
    estado_plaza_registro = models.SmallIntegerField(blank=True, null=True)
    fecha_activacion = models.DateTimeField(blank=True, null=True)
    fecha_desactivacion = models.DateTimeField(blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    numero_documento = models.CharField(max_length=20, blank=True)
    tipo_generacion = models.SmallIntegerField(blank=True, null=True)
    anios_servicio = models.SmallIntegerField(blank=True, null=True)
    pagar_plaza_primaria = models.SmallIntegerField(blank=True, null=True)
    licencia_goce = models.SmallIntegerField(blank=True, null=True)
    horas_clase = models.IntegerField(blank=True, null=True)
    e_plaza_primaria_generar = models.SmallIntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    observaciones = models.CharField(max_length=255, blank=True)
    codigo_municipio_anterior = models.CharField(max_length=2, blank=True)
    codigo_centro_anterior = models.CharField(max_length=5, blank=True)
    municipio_depurado = models.CharField(max_length=1, blank=True)
    plaza_primaria_anterior = models.CharField(max_length=50, blank=True)
    plaza_secundaria_anterior = models.CharField(max_length=50, blank=True)
    plaza_primaria_muni_depurado = models.CharField(max_length=1, blank=True)
    plaza_secundaria_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'hh_histo_movimientos'

class HhHistoTransPeriodos(models.Model):
    codigo_periodo = models.CharField(max_length=6)
    identidad_empleado = models.CharField(max_length=13)
    cuenta = models.CharField(max_length=50)
    codigo_transaccion = models.IntegerField()
    secuencial_histo_trans = models.IntegerField()
    codigo_planilla = models.CharField(max_length=10, blank=True)
    monto_transaccion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    periodo_transaccion = models.CharField(max_length=6, blank=True)
    item_matricial = models.IntegerField(blank=True, null=True)
    estado_transaccion = models.SmallIntegerField(blank=True, null=True)
    fecha_activacion = models.DateTimeField(blank=True, null=True)
    fecha_desactivacion = models.DateTimeField(blank=True, null=True)
    presupuesto_congelado = models.SmallIntegerField(blank=True, null=True)
    monto_sobregiro = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    numero_documento = models.CharField(max_length=20, blank=True)
    estructura_periodo = models.CharField(max_length=50, blank=True)
    tipo_generacion = models.SmallIntegerField(blank=True, null=True)
    aparecio_planilla = models.SmallIntegerField(blank=True, null=True)
    periodo_original = models.CharField(max_length=6, blank=True)
    valor_recuperar = models.SmallIntegerField(blank=True, null=True)
    observacion_tran_periodo = models.CharField(max_length=250, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'hh_histo_trans_periodos'

class HhTransPlanillas(models.Model):
    codigo_planilla = models.CharField(max_length=10)
    identidad_empleado = models.CharField(max_length=13)
    cuenta = models.CharField(max_length=50)
    codigo_transaccion = models.IntegerField()
    nombres_empleado = models.CharField(max_length=35, blank=True)
    apellidos_empleado = models.CharField(max_length=35, blank=True)
    codigo_nivel_educativo = models.IntegerField()
    codigo_banco_deposito = models.IntegerField(blank=True, null=True)
    cuenta_bancaria = models.CharField(max_length=25, blank=True)
    codigo_departamento = models.CharField(max_length=2, blank=True)
    codigo_municipio = models.CharField(max_length=2, blank=True)
    codigo_centro = models.CharField(max_length=5, blank=True)
    codigo_aldea = models.CharField(max_length=5, blank=True)
    codigo_clase = models.IntegerField(blank=True, null=True)
    codigo_planta = models.CharField(max_length=2, blank=True)
    codigo_cargo = models.CharField(max_length=15, blank=True)
    codigo_tipo_cargo = models.CharField(max_length=2, blank=True)
    codigo_cargo_generico = models.CharField(max_length=2, blank=True)
    codigo_distrito = models.IntegerField(blank=True, null=True)
    monto_transaccion = models.DecimalField(max_digits=18, decimal_places=2)
    monto_sobregiro = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    estructura_ejecucion = models.CharField(max_length=50, blank=True)
    estado_presupuesto = models.SmallIntegerField(blank=True, null=True)
    clase_transaccion = models.SmallIntegerField(blank=True, null=True)
    descripcion_corta_trans = models.CharField(max_length=25, blank=True)
    descripcion_transaccion = models.CharField(max_length=100, blank=True)
    clase_centro = models.IntegerField(blank=True, null=True)
    codigo_tipo_centro = models.IntegerField(blank=True, null=True)
    codigo_unidad = models.CharField(max_length=1, blank=True)
    anio_cheque = models.CharField(max_length=4, blank=True)
    tipo_pago_cheque = models.CharField(max_length=2, blank=True)
    numero_cheque = models.CharField(max_length=6, blank=True)
    item_matricial = models.IntegerField(blank=True, null=True)
    corrent = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    programa = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    subprog = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    proyecto = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    actobra = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    partida = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    codfte = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    org_financ = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    benef = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    numero_plaza = models.CharField(max_length=6, blank=True)
    horas_clase = models.IntegerField(blank=True, null=True)
    nombre_tipo_cargo = models.CharField(max_length=50, blank=True)
    nombre_cargo_generico = models.CharField(max_length=50, blank=True)
    descripcion_clase = models.CharField(max_length=50, blank=True)
    nombre_unidad = models.CharField(max_length=50, blank=True)
    descripcion_planta = models.CharField(max_length=50, blank=True)
    descripcion_cargo = models.CharField(max_length=50, blank=True)
    descripcion_departamento = models.CharField(max_length=25, blank=True)
    descripcion_municipio = models.CharField(max_length=25, blank=True)
    descripcion_centro = models.CharField(max_length=120, blank=True)
    descripcion_aldea = models.CharField(max_length=25, blank=True)
    descripcion_distrito = models.CharField(max_length=25, blank=True)
    descripcion_tipo_centro = models.CharField(max_length=100, blank=True)
    abreviatura_trans = models.CharField(max_length=10, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    anio_deposito = models.CharField(max_length=4, blank=True)
    tipo_deposito = models.CharField(max_length=2, blank=True)
    numero_deposito = models.CharField(max_length=6, blank=True)
    gerencia_admon = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    unidad_ejecutora = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'hh_trans_planillas'

class Jubilados(models.Model):
    identidad = models.CharField(db_column='IDENTIDAD', max_length=20, blank=True) # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=255, blank=True) # Field name made lowercase.
    identidad_empleado = models.CharField(max_length=13)
    no_remision = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'jubilados'

class LosElegidos(models.Model):
    identidad_empleado = models.CharField(max_length=20)
    monto = models.DecimalField(max_digits=18, decimal_places=2)
    class Meta:
        managed = False
        db_table = 'los_elegidos'

class LosElegidosC(models.Model):
    corrida = models.IntegerField()
    identidad_empleado = models.CharField(max_length=13, blank=True)
    class Meta:
        managed = False
        db_table = 'los_elegidos_c'

class LosElegidosD(models.Model):
    corrida = models.IntegerField()
    codigo_banco = models.IntegerField()
    cuenta_bancaria = models.CharField(max_length=25, blank=True)
    identidad_empleado = models.CharField(max_length=13, blank=True)
    beneficiario = models.CharField(max_length=100, blank=True)
    monto_deposito = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'los_elegidos_d'

class Pbcatcol(models.Model):
    pbc_tnam = models.CharField(max_length=30)
    pbc_tid = models.IntegerField()
    pbc_ownr = models.CharField(max_length=30)
    pbc_cnam = models.CharField(max_length=30)
    pbc_cid = models.SmallIntegerField()
    pbc_labl = models.CharField(max_length=254, blank=True)
    pbc_lpos = models.SmallIntegerField(blank=True, null=True)
    pbc_hdr = models.CharField(max_length=254, blank=True)
    pbc_hpos = models.SmallIntegerField(blank=True, null=True)
    pbc_jtfy = models.SmallIntegerField(blank=True, null=True)
    pbc_mask = models.CharField(max_length=31, blank=True)
    pbc_case = models.SmallIntegerField(blank=True, null=True)
    pbc_hght = models.SmallIntegerField(blank=True, null=True)
    pbc_wdth = models.SmallIntegerField(blank=True, null=True)
    pbc_ptrn = models.CharField(max_length=31, blank=True)
    pbc_bmap = models.CharField(max_length=1, blank=True)
    pbc_init = models.CharField(max_length=254, blank=True)
    pbc_cmnt = models.CharField(max_length=254, blank=True)
    pbc_edit = models.CharField(max_length=31, blank=True)
    pbc_tag = models.CharField(max_length=254, blank=True)
    class Meta:
        managed = False
        db_table = 'pbcatcol'

class Pbcatedt(models.Model):
    pbe_name = models.CharField(max_length=30)
    pbe_edit = models.CharField(max_length=254)
    pbe_type = models.SmallIntegerField()
    pbe_cntr = models.IntegerField(blank=True, null=True)
    pbe_seqn = models.SmallIntegerField()
    pbe_flag = models.IntegerField(blank=True, null=True)
    pbe_work = models.CharField(max_length=32, blank=True)
    class Meta:
        managed = False
        db_table = 'pbcatedt'

class Pbcatfmt(models.Model):
    pbf_name = models.CharField(max_length=30)
    pbf_frmt = models.CharField(max_length=254)
    pbf_type = models.SmallIntegerField()
    pbf_cntr = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pbcatfmt'

class Pbcattbl(models.Model):
    pbt_tnam = models.CharField(max_length=30)
    pbt_tid = models.IntegerField(primary_key=True)
    pbt_ownr = models.CharField(max_length=30)
    pbd_fhgt = models.SmallIntegerField(blank=True, null=True)
    pbd_fwgt = models.SmallIntegerField(blank=True, null=True)
    pbd_fitl = models.CharField(max_length=1, blank=True)
    pbd_funl = models.CharField(max_length=1, blank=True)
    pbd_fchr = models.SmallIntegerField(blank=True, null=True)
    pbd_fptc = models.SmallIntegerField(blank=True, null=True)
    pbd_ffce = models.CharField(max_length=32, blank=True)
    pbh_fhgt = models.SmallIntegerField(blank=True, null=True)
    pbh_fwgt = models.SmallIntegerField(blank=True, null=True)
    pbh_fitl = models.CharField(max_length=1, blank=True)
    pbh_funl = models.CharField(max_length=1, blank=True)
    pbh_fchr = models.SmallIntegerField(blank=True, null=True)
    pbh_fptc = models.SmallIntegerField(blank=True, null=True)
    pbh_ffce = models.CharField(max_length=32, blank=True)
    pbl_fhgt = models.SmallIntegerField(blank=True, null=True)
    pbl_fwgt = models.SmallIntegerField(blank=True, null=True)
    pbl_fitl = models.CharField(max_length=1, blank=True)
    pbl_funl = models.CharField(max_length=1, blank=True)
    pbl_fchr = models.SmallIntegerField(blank=True, null=True)
    pbl_fptc = models.SmallIntegerField(blank=True, null=True)
    pbl_ffce = models.CharField(max_length=32, blank=True)
    pbt_cmnt = models.CharField(max_length=254, blank=True)
    class Meta:
        managed = False
        db_table = 'pbcattbl'

class Pbcatvld(models.Model):
    pbv_name = models.CharField(max_length=30)
    pbv_vald = models.CharField(max_length=254)
    pbv_type = models.SmallIntegerField()
    pbv_cntr = models.IntegerField(blank=True, null=True)
    pbv_msg = models.CharField(max_length=254, blank=True)
    class Meta:
        managed = False
        db_table = 'pbcatvld'

class PpAcuerdos(models.Model):
    codigo_unidad = models.ForeignKey('PpUnidadesEjecutoras', db_column='codigo_unidad')
    numero_acuerdo = models.CharField(unique=True, max_length=20)
    nombre_unidad = models.CharField(max_length=50, blank=True)
    codigo_movimiento = models.ForeignKey('PpMotivosMovimientos', db_column='codigo_movimiento')
    descripcion_movimiento = models.CharField(max_length=50, blank=True)
    codigo_motivo = models.ForeignKey('PpMotivosMovimientos', db_column='codigo_motivo')
    descripcion_motivo = models.CharField(max_length=100, blank=True)
    codigo_departamento = models.ForeignKey('PpCentrosEducativos', db_column='codigo_departamento')
    descripcion_departamento = models.CharField(max_length=25, blank=True)
    codigo_municipio = models.ForeignKey('PpCentrosEducativos', db_column='codigo_municipio')
    codigo_centro = models.ForeignKey('PpCentrosEducativos', db_column='codigo_centro')
    nombre_centro_educativo = models.CharField(max_length=120, blank=True)
    identidad_empleado = models.ForeignKey('PpEmpleados', db_column='identidad_empleado')
    nombres_empleado = models.CharField(max_length=80, blank=True)
    direccion_empleado = models.CharField(max_length=100, blank=True)
    apellidos_empleado = models.CharField(max_length=100, blank=True)
    estado_documento = models.ForeignKey('PpEstadosDocumentos', db_column='estado_documento')
    edad_empleado = models.IntegerField(blank=True, null=True)
    tiempo_servicio_empleado = models.CharField(max_length=30, blank=True)
    total_horas_actuales = models.IntegerField(blank=True, null=True)
    tipo_profesional_empleado = models.CharField(max_length=35, blank=True)
    titulo_empleado = models.CharField(max_length=100, blank=True)
    jornada_empleado = models.CharField(max_length=25, blank=True)
    numero_accion = models.IntegerField(blank=True, null=True)
    vigencia_desde = models.DateTimeField(blank=True, null=True)
    vigencia_hasta = models.DateTimeField(blank=True, null=True)
    vigente_acuerdo = models.SmallIntegerField(blank=True, null=True)
    encabezado = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)
    plaza_afectada_primaria = models.CharField(max_length=50, blank=True)
    plaza_afectada_secundaria = models.CharField(max_length=50, blank=True)
    efecto_general = models.SmallIntegerField(blank=True, null=True)
    codigo_cargo = models.CharField(max_length=15, blank=True)
    descripcion_cargo = models.CharField(max_length=100, blank=True)
    horas_plaza = models.IntegerField(blank=True, null=True)
    identidad_alterna = models.CharField(max_length=13, blank=True)
    nombre_alterno = models.CharField(max_length=80, blank=True)
    edad_alterna = models.IntegerField(blank=True, null=True)
    tiempo_servicio_alterno = models.CharField(max_length=30, blank=True)
    codigo_director = models.CharField(max_length=25, blank=True)
    nombre_director = models.CharField(max_length=80, blank=True)
    codigo_secretario = models.CharField(max_length=25, blank=True)
    nombre_secretario = models.CharField(max_length=80, blank=True)
    numero_impresiones = models.IntegerField(blank=True, null=True)
    fecha_ultima_impresion = models.DateTimeField(blank=True, null=True)
    fecha_creacion_letras = models.CharField(max_length=40, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    codigo_municipio_anterior = models.CharField(max_length=2, blank=True)
    codigo_centro_anterior = models.CharField(max_length=5, blank=True)
    plaza_primaria_anterior = models.CharField(max_length=50, blank=True)
    plaza_secundaria_anterior = models.CharField(max_length=50, blank=True)
    municipio_depurado = models.CharField(max_length=1, blank=True)
    plaza_primaria_muni_depurado = models.CharField(max_length=1, blank=True)
    plaza_secundaria_muni_depurado = models.CharField(max_length=1, blank=True)
    usuario_aprobo = models.CharField(max_length=25, blank=True)
    fecha_aprobo = models.DateTimeField(blank=True, null=True)
    fecha_inicio_obs = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_acuerdos'

class PpAcumuladores(models.Model):
    codigo_transaccion = models.ForeignKey('PpTransacciones', db_column='codigo_transaccion')
    pp_codigo_transaccion = models.ForeignKey('PpTransacciones', db_column='pp__codigo_transaccion') # Field renamed because it contained more than one '_' in a row.
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_acumuladores'

class PpAdjudicacionPlazas(models.Model):
    codigo_unidad = models.ForeignKey('PpUnidadesEjecutoras', db_column='codigo_unidad')
    secuencial_seleccion = models.IntegerField()
    anio_listado = models.IntegerField()
    identidad_empleado = models.ForeignKey('PpEmpleados', db_column='identidad_empleado')
    cuenta = models.ForeignKey('PpPlazas', db_column='cuenta')
    estado_seleccion = models.IntegerField()
    observaciones = models.TextField(blank=True)
    fecha_notificacion = models.DateTimeField(blank=True, null=True)
    fecha_respuesta = models.DateTimeField(blank=True, null=True)
    fecha_a_presentarse = models.DateTimeField(blank=True, null=True)
    fecha_ultimo_estado = models.DateTimeField()
    tipo_listado = models.CharField(max_length=1)
    codigo_registro = models.IntegerField()
    secuencial_concurso = models.IntegerField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_adjudicacion_plazas'

class PpAdminTipos(models.Model):
    codigo_tipo = models.CharField(max_length=50)
    codigo_subtipo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_admin_tipos'

class PpAldeas(models.Model):
    codigo_departamento = models.ForeignKey('PpMunicipios', db_column='codigo_departamento')
    codigo_municipio = models.ForeignKey('PpMunicipios', db_column='codigo_municipio')
    codigo_aldea = models.CharField(max_length=5)
    descripcion_aldea = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    tipo_area = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_aldeas'

class PpAnexoAdmon(models.Model):
    cuenta = models.ForeignKey('PpCatalogos', db_column='cuenta')
    codigo_transaccion = models.ForeignKey('PpTransacciones', db_column='codigo_transaccion')
    anio_anexo = models.IntegerField()
    codigo_modalidad = models.ForeignKey('PpModalidades', db_column='codigo_modalidad', blank=True, null=True)
    descripcion_cargo = models.CharField(max_length=35, blank=True)
    horas_plaza = models.IntegerField(blank=True, null=True)
    identidad_empleado = models.CharField(max_length=13, blank=True)
    nombres_empleado = models.CharField(max_length=35, blank=True)
    apellidos_empleado = models.CharField(max_length=35, blank=True)
    corrent = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    programa = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    subprog = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    proyecto = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    actobra = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    partida = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    codfte = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    org_financ = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    codigo_benef = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    monto_anio_anterior = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_proyectado_anual = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_bajo_techo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_proyeccion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    proyeccion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_anexo_admon'

class PpAnexoColadmon(models.Model):
    anio_anexo = models.IntegerField()
    cuenta = models.CharField(max_length=50)
    codigo_modalidad = models.IntegerField(blank=True, null=True)
    corrent = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    programa = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    subprog = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    proyecto = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    actobra = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    partida = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    codfte = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    monto_sbase = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_antiguedad = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_meritos = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_zonaje = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_cargo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_calificacion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_frontera = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_clase_escuela = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_compensatorias = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_cargo_nocturna = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    org_financ = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    codigo_benef = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_anexo_coladmon'

class PpAnexoColateral(models.Model):
    anio_anexo = models.IntegerField()
    cuenta = models.CharField(max_length=50)
    codigo_modalidad = models.IntegerField(blank=True, null=True)
    corrent = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    programa = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    subprog = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    proyecto = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    actobra = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    partida = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    codfte = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    monto_sbase = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_antiguedad = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_meritos = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_zonaje = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_cargo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_calificacion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_frontera = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_clase_escuela = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_compensatorias = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_cargo_nocturna = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    org_financ = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    codigo_benef = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    monto_cargo_directivo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_anexo_colateral'

class PpAnexoColateralTmp(models.Model):
    anio_anexo = models.IntegerField()
    cuenta = models.CharField(max_length=50)
    codigo_departamento = models.CharField(max_length=2, blank=True)
    codigo_municipio = models.CharField(max_length=2, blank=True)
    codigo_centro = models.CharField(max_length=5, blank=True)
    codigo_modalidad = models.IntegerField(blank=True, null=True)
    corrent = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    programa = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    subprog = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    proyecto = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    actobra = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    partida = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    codfte = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    monto_sbase = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_antiguedad = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_meritos = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_zonaje = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_cargo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_calificacion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_frontera = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_clase_escuela = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_compensatorias = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_cargo_nocturna = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    org_financ = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    codigo_benef = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_anexo_colateral_tmp'

class PpAnexoDesglosado(models.Model):
    cuenta = models.ForeignKey('PpCatalogos', db_column='cuenta')
    codigo_transaccion = models.ForeignKey('PpTransacciones', db_column='codigo_transaccion')
    anio_anexo = models.IntegerField()
    codigo_modalidad = models.ForeignKey('PpModalidades', db_column='codigo_modalidad', blank=True, null=True)
    descripcion_cargo = models.CharField(max_length=35, blank=True)
    horas_plaza = models.IntegerField(blank=True, null=True)
    identidad_empleado = models.CharField(max_length=13, blank=True)
    nombres_empleado = models.CharField(max_length=35, blank=True)
    apellidos_empleado = models.CharField(max_length=35, blank=True)
    corrent = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    programa = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    subprog = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    proyecto = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    actobra = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    partida = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    codfte = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    org_financ = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    codigo_benef = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    monto_anio_anterior = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_proyectado_anual = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_bajo_techo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_proyeccion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    proyeccion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    codigo_cargo = models.CharField(max_length=15, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_anexo_desglosado'

class PpAnexoParamTransacciones(models.Model):
    codigo_transaccion = models.ForeignKey('PpTransacciones', db_column='codigo_transaccion', primary_key=True)
    objeto_aplica_estruc_plaza = models.CharField(max_length=1, blank=True)
    tipo_concepto = models.IntegerField()
    aplicar_inprema = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'pp_anexo_param_transacciones'

class PpAplicar251(models.Model):
    identidad_empleado = models.CharField(max_length=13, blank=True)
    aplicar_251 = models.IntegerField(blank=True, null=True)
    fecha_activacion = models.DateTimeField(blank=True, null=True)
    usuario_activacion = models.CharField(max_length=25, blank=True)
    fecha_desactivacion = models.DateTimeField(blank=True, null=True)
    usuario_desactivacion = models.CharField(max_length=25, blank=True)
    codigo_periodo_activo = models.CharField(max_length=6, blank=True)
    monto_251 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    elimina_sb = models.IntegerField(blank=True, null=True)
    cuenta = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_aplicar_251'

class PpArchTxtPlanillas(models.Model):
    codigo_planilla = models.CharField(max_length=10)
    identidad_empleado = models.CharField(max_length=13)
    cuenta = models.CharField(max_length=50)
    codigo_transaccion = models.IntegerField()
    nombres_empleado = models.CharField(max_length=35, blank=True)
    apellidos_empleado = models.CharField(max_length=35, blank=True)
    codigo_nivel_educativo = models.IntegerField()
    codigo_banco_deposito = models.IntegerField(blank=True, null=True)
    cuenta_bancaria = models.CharField(max_length=25, blank=True)
    codigo_departamento = models.CharField(max_length=2, blank=True)
    codigo_municipio = models.CharField(max_length=2, blank=True)
    codigo_centro = models.CharField(max_length=5, blank=True)
    codigo_aldea = models.CharField(max_length=5, blank=True)
    codigo_clase = models.IntegerField(blank=True, null=True)
    codigo_planta = models.CharField(max_length=2, blank=True)
    codigo_cargo = models.CharField(max_length=15, blank=True)
    codigo_tipo_cargo = models.CharField(max_length=2, blank=True)
    codigo_cargo_generico = models.CharField(max_length=2, blank=True)
    codigo_distrito = models.IntegerField(blank=True, null=True)
    monto_transaccion = models.DecimalField(max_digits=18, decimal_places=2)
    monto_sobregiro = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    estructura_ejecucion = models.CharField(max_length=50, blank=True)
    estado_presupuesto = models.SmallIntegerField(blank=True, null=True)
    clase_transaccion = models.SmallIntegerField(blank=True, null=True)
    descripcion_corta_trans = models.CharField(max_length=25, blank=True)
    descripcion_transaccion = models.CharField(max_length=100, blank=True)
    clase_centro = models.IntegerField(blank=True, null=True)
    codigo_tipo_centro = models.IntegerField(blank=True, null=True)
    codigo_unidad = models.CharField(max_length=1, blank=True)
    anio_cheque = models.CharField(max_length=4, blank=True)
    tipo_pago_cheque = models.CharField(max_length=2, blank=True)
    numero_cheque = models.CharField(max_length=6, blank=True)
    item_matricial = models.IntegerField(blank=True, null=True)
    corrent = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    programa = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    subprog = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    proyecto = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    actobra = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    partida = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    codfte = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    org_financ = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    benef = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    numero_plaza = models.CharField(max_length=6, blank=True)
    horas_clase = models.IntegerField(blank=True, null=True)
    nombre_tipo_cargo = models.CharField(max_length=50, blank=True)
    nombre_cargo_generico = models.CharField(max_length=50, blank=True)
    descripcion_clase = models.CharField(max_length=50, blank=True)
    nombre_unidad = models.CharField(max_length=50, blank=True)
    descripcion_planta = models.CharField(max_length=50, blank=True)
    descripcion_cargo = models.CharField(max_length=50, blank=True)
    descripcion_departamento = models.CharField(max_length=25, blank=True)
    descripcion_municipio = models.CharField(max_length=25, blank=True)
    descripcion_centro = models.CharField(max_length=120, blank=True)
    descripcion_aldea = models.CharField(max_length=25, blank=True)
    descripcion_distrito = models.CharField(max_length=25, blank=True)
    descripcion_tipo_centro = models.CharField(max_length=100, blank=True)
    abreviatura_trans = models.CharField(max_length=10, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    anio_deposito = models.CharField(max_length=4, blank=True)
    tipo_deposito = models.CharField(max_length=2, blank=True)
    numero_deposito = models.CharField(max_length=6, blank=True)
    gerencia_admon = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    unidad_ejecutora = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_arch_txt_planillas'

class PpAsignaturas(models.Model):
    codigo_asignatura = models.IntegerField(unique=True)
    descripcion_asignatura = models.CharField(max_length=100)
    abreviatura_asignatura = models.CharField(max_length=15, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_asignaturas'

class PpBancos(models.Model):
    codigo_banco = models.IntegerField(primary_key=True)
    nombre_banco = models.CharField(max_length=50)
    telefono1_banco = models.CharField(max_length=15, blank=True)
    telefono2_banco = models.CharField(max_length=15, blank=True)
    fax_banco = models.CharField(max_length=15, blank=True)
    email_banco = models.CharField(max_length=25, blank=True)
    direccion_banco = models.CharField(max_length=250, blank=True)
    contacto = models.CharField(max_length=50, blank=True)
    longitud_minima = models.IntegerField(blank=True, null=True)
    longitud_maxima = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    marcado = models.IntegerField(blank=True, null=True)
    codigo_banco_finanzas = models.IntegerField(blank=True, null=True)
    pagar_siafi = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_bancos'

class PpBitacoraErrores(models.Model):
    usuario = models.CharField(unique=True, max_length=25)
    sqlcode = models.IntegerField(blank=True, null=True)
    descripcion_error = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_bitacora_errores'

class PpBitacoraEstadoDocentes(models.Model):
    codigo = models.AutoField(primary_key=True)
    identidad_empleado = models.CharField(max_length=13)
    estado_docente_anterior = models.IntegerField()
    estado_docente_nuevo = models.IntegerField()
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    observarcion = models.TextField()
    class Meta:
        managed = False
        db_table = 'pp_bitacora_estado_docentes'

class PpBitacoraPresupuestos(models.Model):
    anio_carga = models.IntegerField(blank=True, null=True)
    secuencial = models.IntegerField(blank=True, null=True)
    codigo_presupuesto = models.IntegerField(blank=True, null=True)
    cuenta = models.CharField(max_length=50)
    estructura_siafi = models.CharField(max_length=50, blank=True)
    presupuesto_original_siarhd = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    modif_aumento_monto_siarhd = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    modif_mas_siarhd = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    modif_menos_siarhd = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_modificado_siarhd = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    congelamiento_siarhd = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    pagos_ejecutados_siarhd = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    disponible_total_siarhd = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_original_siafi = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    modif_aumento_monto_siafi = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    modif_mas_siafi = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    modif_menos_siafi = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_modificado_siafi = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    congelamiento_siafi = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    pagos_ejecutados_siafi = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    disponible_total_siafi = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    periodo_inicial = models.CharField(max_length=6, blank=True)
    periodo_final = models.CharField(max_length=6, blank=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_bitacora_presupuestos'

class PpCaducidades(models.Model):
    codigo_documento_caduc = models.CharField(unique=True, max_length=20)
    codigo_movimiento = models.ForeignKey('PpMotivosMovimientos', db_column='codigo_movimiento')
    codigo_motivo = models.ForeignKey('PpMotivosMovimientos', db_column='codigo_motivo')
    fecha_emision_doc_caduc = models.DateTimeField(blank=True, null=True)
    identidad_afectada = models.CharField(max_length=13, blank=True)
    numero_acuerdo = models.CharField(max_length=20, blank=True)
    codigo_movimiento_caduc = models.IntegerField(blank=True, null=True)
    codigo_motivo_caduc = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_caducidades'

class PpCapacitaciones(models.Model):
    codigo_capacitacion = models.IntegerField(primary_key=True)
    descripcion_capacitacion = models.CharField(max_length=100)
    puntaje_aprobacion = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_capacitaciones'

class PpCargos(models.Model):
    codigo_cargo = models.CharField(primary_key=True, max_length=15)
    descripcion_cargo = models.CharField(max_length=100, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_cargos'

class PpCargosGenericos(models.Model):
    codigo_tipo_cargo = models.ForeignKey('PpTiposCargos', db_column='codigo_tipo_cargo')
    codigo_cargo_generico = models.CharField(max_length=2)
    nombre_cargo_generico = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_cargos_genericos'

class PpCaserios(models.Model):
    codigo_departamento = models.ForeignKey(PpAldeas, db_column='codigo_departamento')
    codigo_municipio = models.ForeignKey(PpAldeas, db_column='codigo_municipio')
    codigo_aldea = models.ForeignKey(PpAldeas, db_column='codigo_aldea')
    codigo_caserio = models.CharField(max_length=3)
    descripcion_caserio = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_caserios'

class PpCasosHistoIdent2Tmp(models.Model):
    identidad_empleado = models.CharField(max_length=13, blank=True)
    identidad_anterior = models.CharField(max_length=13, blank=True)
    cuenta = models.CharField(max_length=50, blank=True)
    nombre = models.CharField(max_length=255, blank=True)
    apellido = models.CharField(max_length=255, blank=True)
    nombres_apellidos = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_casos_histo_ident2_tmp'

class PpCasosHistoIdentidadesTmp(models.Model):
    identidad_empleado = models.CharField(max_length=13, blank=True)
    nombres_empleado = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_casos_histo_identidades_tmp'

class PpCatalogos(models.Model):
    cuenta = models.CharField(primary_key=True, max_length=50)
    padre = models.CharField(max_length=50, blank=True)
    descripcion_cuenta = models.CharField(max_length=150, blank=True)
    es_estructura = models.SmallIntegerField()
    nivel = models.SmallIntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=30)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    cuenta_cancelada = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_catalogos'

class PpCausasPermisos(models.Model):
    codigo_permiso = models.IntegerField(unique=True)
    descripcion_permiso = models.CharField(max_length=100)
    abreviatura_permiso = models.CharField(max_length=35)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_causas_permisos'

class PpCentrosEducativos(models.Model):
    codigo_departamento = models.ForeignKey('PpMunicipios', db_column='codigo_departamento')
    codigo_municipio = models.ForeignKey('PpMunicipios', db_column='codigo_municipio')
    codigo_centro = models.CharField(max_length=5)
    codigo_nivel_educativo = models.ForeignKey('PpNivelesEducativos', db_column='codigo_nivel_educativo')
    codigo_tipo_centro = models.ForeignKey('PpTiposCentrosEducativos', db_column='codigo_tipo_centro', blank=True, null=True)
    codigo_aldea = models.CharField(max_length=5)
    descripcion_centro = models.CharField(max_length=120)
    abreviatura_centro = models.CharField(max_length=15)
    direccion_centro = models.CharField(max_length=200, blank=True)
    telefono_centro = models.CharField(max_length=15, blank=True)
    ubicacion_centro = models.CharField(max_length=2)
    frontera = models.CharField(max_length=1, blank=True)
    codigo_distrito = models.ForeignKey('PpDistritos', db_column='codigo_distrito')
    codigo_clase = models.ForeignKey('PpClasesCentros', db_column='codigo_clase')
    numero_max_directores = models.IntegerField(blank=True, null=True)
    numero_max_subdirectores = models.IntegerField(blank=True, null=True)
    numero_max_secretarios = models.IntegerField(blank=True, null=True)
    numero_max_docentes = models.IntegerField(blank=True, null=True)
    estado_centro = models.CharField(max_length=1, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    codigo_municipio_anterior = models.CharField(max_length=2, blank=True)
    codigo_centro_anterior = models.CharField(max_length=5, blank=True)
    municipio_depurado = models.CharField(max_length=1, blank=True)
    usuario_modif_tipo_centro = models.CharField(max_length=25, blank=True)
    fecha_modif_tipo_centro = models.DateTimeField(blank=True, null=True)
    usuario_modif_clase = models.CharField(max_length=25, blank=True)
    fecha_modif_clase = models.DateTimeField(blank=True, null=True)
    usuario_modif_desc = models.CharField(max_length=25, blank=True)
    fecha_modif_desc = models.DateTimeField(blank=True, null=True)
    usuario_modif_direccion = models.CharField(max_length=25, blank=True)
    fecha_modif_direccion = models.DateTimeField(blank=True, null=True)
    usuario_modif_frontera = models.CharField(max_length=25, blank=True)
    fecha_modif_frontera = models.DateTimeField(blank=True, null=True)
    usuario_modif_ubicacion = models.CharField(max_length=25, blank=True)
    fecha_modif_ubicacion = models.DateTimeField(blank=True, null=True)
    codigo_caserio = models.CharField(max_length=3, blank=True)
    usuario_modif_aldea = models.CharField(max_length=25, blank=True)
    fecha_modif_aldea = models.DateTimeField(blank=True, null=True)
    usuario_modif_caserio = models.CharField(max_length=25, blank=True)
    fecha_modif_caserio = models.DateTimeField(blank=True, null=True)
    fecha_modif_estado = models.DateTimeField(blank=True, null=True)
    usuario_modif_estado = models.CharField(max_length=25, blank=True)
    codigo_tipo_centro_anterior = models.IntegerField(blank=True, null=True)
    ubicacion_centro_anterior = models.CharField(max_length=2, blank=True)
    direccion_centro_anterior = models.CharField(max_length=200, blank=True)
    descripcion_centro_anterior = models.CharField(max_length=120, blank=True)
    codigo_aldea_anterior = models.CharField(max_length=5, blank=True)
    codigo_caserio_anterior = models.CharField(max_length=3, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_centros_educativos'

class PpCentrosEstudios(models.Model):
    codigo_centro_estudio = models.IntegerField(primary_key=True)
    nombre_centro_estudio = models.CharField(max_length=100)
    abreviatura_centro_estudio = models.CharField(max_length=25)
    universidad_educativa = models.SmallIntegerField(blank=True, null=True)
    verificacion_titulo = models.SmallIntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_centros_estudios'

class PpCentrosPago(models.Model):
    codigo_departamento = models.ForeignKey('PpMunicipios', db_column='codigo_departamento')
    codigo_municipio = models.ForeignKey('PpMunicipios', db_column='codigo_municipio')
    codigo_centro_pago = models.CharField(max_length=5)
    tipo_centro_pago = models.SmallIntegerField()
    abreviatura_centro_pago = models.CharField(max_length=15, blank=True)
    codigo_aldea = models.CharField(max_length=5, blank=True)
    descripcion_centro_pago = models.CharField(max_length=200)
    direccion_centro_pago = models.CharField(max_length=250, blank=True)
    estado_centro_pago = models.SmallIntegerField()
    telefono1_centro_pago = models.CharField(max_length=15, blank=True)
    telefono2_centro_pago = models.CharField(max_length=15, blank=True)
    ubicacion_centro_pago = models.SmallIntegerField(blank=True, null=True)
    numero_patronal_ihss = models.CharField(max_length=15, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    codigo_municipio_anterior = models.CharField(max_length=2, blank=True)
    municipio_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_centros_pago'

class PpCentrosPagoCentros(models.Model):
    pp_codigo_departamento = models.ForeignKey(PpCentrosPago, db_column='pp__codigo_departamento') # Field renamed because it contained more than one '_' in a row.
    pp_codigo_municipio = models.ForeignKey(PpCentrosPago, db_column='pp__codigo_municipio') # Field renamed because it contained more than one '_' in a row.
    codigo_centro = models.ForeignKey(PpCentrosEducativos, db_column='codigo_centro')
    codigo_departamento = models.ForeignKey(PpCentrosEducativos, db_column='codigo_departamento')
    codigo_municipio = models.ForeignKey(PpCentrosEducativos, db_column='codigo_municipio')
    codigo_centro_pago = models.ForeignKey(PpCentrosPago, db_column='codigo_centro_pago')
    codigo_municipio_anterior = models.CharField(max_length=2, blank=True)
    codigo_centro_anterior = models.CharField(max_length=5, blank=True)
    pp_codigo_municipio_anterior = models.CharField(db_column='pp__codigo_municipio_anterior', max_length=2, blank=True) # Field renamed because it contained more than one '_' in a row.
    pp_codigo_centro_anterior = models.CharField(db_column='pp__codigo_centro_anterior', max_length=5, blank=True) # Field renamed because it contained more than one '_' in a row.
    municipio_depurado = models.CharField(max_length=1, blank=True)
    pp_municipio_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_centros_pago_centros'

class PpCertificacionesEstudios(models.Model):
    codigo_certifica_estudio = models.CharField(primary_key=True, max_length=20)
    identidad_empleado = models.ForeignKey('PpEmpleados', db_column='identidad_empleado')
    anio_aprobado = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    codigo_titulo = models.ForeignKey('PpTitulos', db_column='codigo_titulo')
    codigo_centro_estudio = models.ForeignKey(PpCentrosEstudios, db_column='codigo_centro_estudio')
    numero_acuerdo = models.ForeignKey('PpLsgEstudios', db_column='numero_acuerdo')
    fecha_solicitud_estudio = models.DateTimeField()
    periodo_aprobado_estudio = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    clases_aprobadas = models.SmallIntegerField()
    clases_no_aprobadas = models.SmallIntegerField()
    calificacion_promedio = models.DecimalField(max_digits=5, decimal_places=2)
    observacion_estudio = models.CharField(max_length=250, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_certificaciones_estudios'

class PpCertificacionesTrabajos(models.Model):
    codigo_certifica_trabajo = models.CharField(primary_key=True, max_length=20)
    identidad_empleado = models.ForeignKey('PpEmpleados', db_column='identidad_empleado')
    estado_documento_trabajo = models.SmallIntegerField()
    en_vigencia_trabajo = models.SmallIntegerField(blank=True, null=True)
    total_horas_semanales = models.IntegerField(blank=True, null=True)
    observacion_trabajo = models.CharField(max_length=250, blank=True)
    xnearmensaje = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_certificaciones_trabajos'

class PpCheques(models.Model):
    codigo_institucion = models.ForeignKey('PpInstitucionesExternas', db_column='codigo_institucion', blank=True, null=True)
    codigo_periodo = models.CharField(max_length=6, blank=True)
    codigo_planilla = models.CharField(max_length=10, blank=True)
    identidad_empleado = models.ForeignKey('PpEmpleados', db_column='identidad_empleado', blank=True, null=True)
    anio_cheque = models.CharField(max_length=4)
    tipo_pago_cheque = models.CharField(max_length=2)
    numero_cheque = models.CharField(max_length=6)
    beneficiario = models.CharField(max_length=100, blank=True)
    fecha_generacion_cheque = models.DateTimeField()
    fecha_emision_cheque = models.DateTimeField(blank=True, null=True)
    monto_cheque = models.DecimalField(max_digits=18, decimal_places=2)
    estado_cheque = models.SmallIntegerField()
    registro_cheque = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_anulacion_cheque = models.DateTimeField(blank=True, null=True)
    fecha_pago_cheque = models.DateTimeField(blank=True, null=True)
    codigo_identificador = models.CharField(max_length=13, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_cheques'

class PpChequesReintegros(models.Model):
    anio_cheque = models.CharField(max_length=4)
    tipo_pago_cheque = models.CharField(max_length=2)
    numero_cheque = models.CharField(max_length=6)
    monto_reintegro = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    numero_cheque_caja = models.CharField(max_length=20, blank=True)
    codigo_motivo = models.IntegerField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_cheques_reintegros'

class PpClasesCentros(models.Model):
    codigo_clase = models.IntegerField(primary_key=True)
    descripcion_clase = models.CharField(max_length=25)
    abreviatura_clase = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_clases_centros'

class PpCodigosCt(models.Model):
    codigo_ct = models.CharField(unique=True, max_length=3)
    descripcion_ct = models.CharField(max_length=100, blank=True)
    clase_ct = models.SmallIntegerField(blank=True, null=True)
    pago_efectivo = models.SmallIntegerField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_codigos_ct'

class PpColonias(models.Model):
    codigo_departamento = models.ForeignKey(PpAldeas, db_column='codigo_departamento')
    codigo_municipio = models.ForeignKey(PpAldeas, db_column='codigo_municipio')
    codigo_aldea = models.ForeignKey(PpAldeas, db_column='codigo_aldea')
    codigo_colonia = models.CharField(max_length=3)
    descripcion_colonia = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_colonias'

class PpComisionesTramites(models.Model):
    codigo_categoria = models.ForeignKey('PpXcategorias', db_column='codigo_categoria')
    identidad_comision = models.ForeignKey('PpParticipantesComisiones', db_column='identidad_comision')
    codigo_documento = models.CharField(max_length=20)
    xnearmensaje = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_comisiones_tramites'

class PpComprobantes(models.Model):
    codigo_comprobante = models.IntegerField(primary_key=True)
    categoria_tramite = models.CharField(max_length=4)
    tipo_receptor_comprobante = models.SmallIntegerField()
    estado_comprobante = models.SmallIntegerField()
    impresion_comprobante = models.IntegerField(blank=True, null=True)
    observaciones_comprobante = models.CharField(max_length=100, blank=True)
    identidad_comprobante = models.CharField(max_length=13)
    nombre_comprobante = models.CharField(max_length=70)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_comprobantes'

class PpComprobantesDetalles(models.Model):
    codigo_comprobante = models.IntegerField()
    codigo_requisito = models.ForeignKey('PpDocumentosRequisitos', db_column='codigo_requisito')
    cantidad_recibida = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_comprobantes_detalles'

class PpConcursantes(models.Model):
    codigo_unidad = models.ForeignKey('PpConcursos', db_column='codigo_unidad')
    anio_concurso = models.ForeignKey('PpConcursos', db_column='anio_concurso')
    secuencial_concurso = models.ForeignKey('PpConcursos', db_column='secuencial_concurso')
    tipo_concurso = models.ForeignKey('PpConcursos', db_column='tipo_concurso')
    codigo_registro = models.IntegerField()
    identidad_empleado = models.ForeignKey('PpEmpleados', db_column='identidad_empleado')
    estado_candidatura = models.IntegerField()
    fecha_ultimo_estado = models.DateTimeField()
    aplica_interinato = models.SmallIntegerField()
    aplica_rural = models.SmallIntegerField()
    nota_aptitud_conocimiento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nota_meritos = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nota_prueba_psicometrica = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nota_creditos_titulos = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nota_promedio = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    observaciones_concursante = models.TextField(blank=True)
    secuencial_seleccion = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_concursantes'

class PpConcursos(models.Model):
    codigo_unidad = models.ForeignKey('PpUnidadesEjecutoras', db_column='codigo_unidad')
    anio_concurso = models.IntegerField()
    secuencial_concurso = models.IntegerField()
    fecha_concurso = models.DateTimeField()
    estado_concurso = models.IntegerField()
    fecha_ultimo_estado = models.DateTimeField()
    tipo_concurso = models.CharField(max_length=1)
    observaciones_concurso = models.TextField(blank=True)
    codigo_nivel_educativo = models.IntegerField(blank=True, null=True)
    codigo_departamento = models.CharField(max_length=2, blank=True)
    codigo_municipio = models.CharField(max_length=2, blank=True)
    codigo_centro_educativo = models.CharField(max_length=5, blank=True)
    tipo_centro = models.IntegerField(blank=True, null=True)
    clase_centro = models.IntegerField(blank=True, null=True)
    cuenta = models.CharField(max_length=50, blank=True)
    codigo_cargo = models.CharField(max_length=15, blank=True)
    horario_plaza = models.IntegerField(blank=True, null=True)
    horas_plaza = models.IntegerField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_concursos'

class PpConfiguracionCentros(models.Model):
    codigo_departamento = models.ForeignKey(PpCentrosEducativos, db_column='codigo_departamento')
    codigo_municipio = models.ForeignKey(PpCentrosEducativos, db_column='codigo_municipio')
    codigo_centro = models.ForeignKey(PpCentrosEducativos, db_column='codigo_centro')
    codigo_configuracion = models.ForeignKey('PpConfiguraciones', db_column='codigo_configuracion')
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    codigo_municipio_anterior = models.CharField(max_length=2, blank=True)
    codigo_centro_anterior = models.CharField(max_length=5, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_configuracion_centros'

class PpConfiguracionFondos(models.Model):
    codigo_fondo = models.ForeignKey('PpTiposFondos', db_column='codigo_fondo')
    codigo_configuracion = models.ForeignKey('PpConfiguraciones', db_column='codigo_configuracion')
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_configuracion_fondos'

class PpConfiguracionNiveles(models.Model):
    codigo_configuracion = models.ForeignKey('PpConfiguraciones', db_column='codigo_configuracion')
    codigo_nivel_educativo = models.ForeignKey('PpNivelesEducativos', db_column='codigo_nivel_educativo')
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_configuracion_niveles'

class PpConfiguracionTipoemp(models.Model):
    codigo_configuracion = models.ForeignKey('PpConfiguraciones', db_column='codigo_configuracion')
    codigo_tipo_empleado = models.ForeignKey('PpTipoEmpleados', db_column='codigo_tipo_empleado')
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_configuracion_tipoemp'

class PpConfiguracionTransacciones(models.Model):
    codigo_transaccion = models.ForeignKey('PpTransacciones', db_column='codigo_transaccion')
    codigo_configuracion = models.ForeignKey('PpConfiguraciones', db_column='codigo_configuracion')
    orden_aparicion = models.IntegerField(blank=True, null=True)
    aparece_planilla = models.SmallIntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_configuracion_transacciones'

class PpConfiguraciones(models.Model):
    codigo_configuracion = models.IntegerField(primary_key=True)
    descripcion_configuracion = models.CharField(max_length=100, blank=True)
    encabezado1 = models.CharField(max_length=100, blank=True)
    encabezado2 = models.CharField(max_length=100, blank=True)
    tipo_encabezado1 = models.SmallIntegerField(blank=True, null=True)
    tipo_encabezado2 = models.SmallIntegerField(blank=True, null=True)
    fecha_incial_cobertura = models.DateTimeField(blank=True, null=True)
    fecha_final_cobertura = models.DateTimeField(blank=True, null=True)
    tipo_cobertura = models.SmallIntegerField(blank=True, null=True)
    dia_mes = models.IntegerField(blank=True, null=True)
    estado_configuracion = models.SmallIntegerField(blank=True, null=True)
    aviso_importante = models.CharField(max_length=250, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_configuraciones'

class PpContadorProcesos(models.Model):
    codigo_periodo = models.CharField(max_length=6)
    codigo_proceso = models.ForeignKey('PpProcesos', db_column='codigo_proceso')
    contador = models.IntegerField(primary_key=True)
    identidad_empleado = models.CharField(max_length=13, blank=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'pp_contador_procesos'

class PpControlEstadosCuenta(models.Model):
    identidad_empleado = models.CharField(max_length=13)
    codigo_periodo = models.CharField(max_length=6)
    usuario_impresion = models.CharField(max_length=25)
    fecha_impresion = models.DateTimeField()
    secuencial_impresion = models.IntegerField()
    computadora = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_control_estados_cuenta'

class PpControlJornadas(models.Model):
    codigo_jornada = models.IntegerField(primary_key=True)
    descripcion_jornada = models.CharField(max_length=100)
    valor_ini_hora = models.IntegerField()
    valor_fin_hora = models.IntegerField()
    cargo_solicitado = models.SmallIntegerField()
    cargo_actual = models.SmallIntegerField()
    numero_centro = models.SmallIntegerField()
    horarios_diferentes = models.SmallIntegerField()
    registro_activo = models.SmallIntegerField()
    observaciones = models.CharField(max_length=250, blank=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_control_jornadas'

class PpControlProcesosConcurrent(models.Model):
    codigo_proceso = models.ForeignKey('PpProcesosConcurrentes', db_column='codigo_proceso')
    identidad_empleado = models.ForeignKey('PpEmpleados', db_column='identidad_empleado')
    usuario = models.CharField(max_length=25)
    base_datos = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'pp_control_procesos_concurrent'

class PpConversionAniosServicios(models.Model):
    secuencial = models.IntegerField(primary_key=True)
    unidad_der = models.CharField(max_length=1, blank=True)
    valor_der = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    unidad_izq = models.CharField(max_length=1, blank=True)
    valor_izq = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_conversion_anios_servicios'

class PpConversionesAdmonCopia2009(models.Model):
    cuenta = models.CharField(max_length=50)
    codigo_conversion = models.IntegerField()
    corrent = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    programa = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    subprog = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    proyecto = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    actobra = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    partida = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    codfte = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    org_financ = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    codigo_benef = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    estructura_siafi = models.CharField(max_length=50, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    descripcion_estructura = models.CharField(max_length=100, blank=True)
    gerencia_admon = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    unidad_ejecutora = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_conversiones_admon_copia_2009'

class PpCopiaAnexoColateral(models.Model):
    anio_anexo = models.IntegerField()
    cuenta = models.CharField(max_length=50)
    codigo_modalidad = models.IntegerField(blank=True, null=True)
    corrent = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    programa = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    subprog = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    proyecto = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    actobra = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    partida = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    codfte = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    monto_sbase = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_antiguedad = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_meritos = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_zonaje = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_cargo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_calificacion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_frontera = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_clase_escuela = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_compensatorias = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_cargo_nocturna = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    org_financ = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    codigo_benef = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_copia_anexo_colateral'

class PpCopiaAnexoDesglosado(models.Model):
    cuenta = models.CharField(max_length=50)
    codigo_transaccion = models.IntegerField()
    anio_anexo = models.IntegerField()
    codigo_modalidad = models.IntegerField(blank=True, null=True)
    descripcion_cargo = models.CharField(max_length=35, blank=True)
    horas_plaza = models.IntegerField(blank=True, null=True)
    identidad_empleado = models.CharField(max_length=13, blank=True)
    nombres_empleado = models.CharField(max_length=35, blank=True)
    apellidos_empleado = models.CharField(max_length=35, blank=True)
    corrent = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    programa = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    subprog = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    proyecto = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    actobra = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    partida = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    codfte = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    org_financ = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    codigo_benef = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    monto_anio_anterior = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_proyectado_anual = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_bajo_techo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_proyeccion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    proyeccion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_copia_anexo_desglosado'

class PpCopiaEncabezadoAnexo(models.Model):
    anio_anexo = models.IntegerField()
    codigo_departamento = models.CharField(max_length=2)
    estado_anexo = models.SmallIntegerField(blank=True, null=True)
    total_plazas = models.IntegerField(blank=True, null=True)
    monto_bajo_techo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_proyectado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_copia_encabezado_anexo'

class PpCriteriosTipos(models.Model):
    codigo_tipo_evaluacion = models.ForeignKey('PpTiposEvaluaciones', db_column='codigo_tipo_evaluacion')
    codigo_criterio = models.IntegerField()
    descripcion_criterio = models.CharField(max_length=100)
    puntaje_maximo_criterio = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_criterios_tipos'

class PpCuentas(models.Model):
    codigo_banco = models.ForeignKey(PpBancos, db_column='codigo_banco')
    codigo_cuenta = models.CharField(max_length=25)
    identidad_empleado = models.ForeignKey('PpEmpleados', db_column='identidad_empleado', unique=True)
    estado_cuenta = models.SmallIntegerField(blank=True, null=True)
    fecha_apertura = models.DateTimeField(blank=True, null=True)
    fecha_importacion = models.DateTimeField(blank=True, null=True)
    fecha_procesamiento = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    observacion = models.CharField(max_length=50, blank=True)
    fecha_cambio_observacion = models.DateTimeField(blank=True, null=True)
    usuario_cambio_observacion = models.CharField(max_length=25, blank=True)
    observacion_anterior = models.CharField(max_length=50, blank=True)
    cuenta_correcta = models.CharField(max_length=25, blank=True)
    cambiar_cuenta = models.SmallIntegerField(blank=True, null=True)
    igual_fotocopia = models.SmallIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_cuentas'

class PpCursosCapacitaciones(models.Model):
    codigo_capacitacion = models.ForeignKey(PpCapacitaciones, db_column='codigo_capacitacion')
    codigo_curso = models.CharField(max_length=5)
    codigo_departamento = models.ForeignKey('PpMunicipios', db_column='codigo_departamento', blank=True, null=True)
    codigo_municipio = models.ForeignKey('PpMunicipios', db_column='codigo_municipio', blank=True, null=True)
    lugar_capacitacion = models.CharField(max_length=200)
    estado_curso = models.SmallIntegerField()
    fecha_planificacion = models.DateTimeField()
    usuario_planificacion = models.CharField(max_length=25)
    fecha_ejecucion = models.DateTimeField(blank=True, null=True)
    usuario_ejecucion = models.CharField(max_length=25, blank=True)
    duracion_horas_curso = models.DecimalField(max_digits=10, decimal_places=2)
    costo_ejecucion_curso = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_cursos_capacitaciones'

class PpDepartamentos(models.Model):
    codigo_departamento = models.CharField(primary_key=True, max_length=2)
    descripcion_departamento = models.CharField(max_length=25)
    abreviatura_departamento = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_departamentos'

class PpDepositos(models.Model):
    anio_deposito = models.CharField(max_length=4)
    tipo_deposito = models.CharField(max_length=2)
    numero_deposito = models.CharField(max_length=6)
    codigo_planilla = models.CharField(max_length=10, blank=True)
    codigo_periodo = models.CharField(max_length=6, blank=True)
    codigo_banco = models.IntegerField(blank=True, null=True)
    cuenta_bancaria = models.CharField(max_length=25, blank=True)
    codigo_institucion = models.ForeignKey('PpInstitucionesExternas', db_column='codigo_institucion', blank=True, null=True)
    identidad_empleado = models.ForeignKey('PpEmpleados', db_column='identidad_empleado', blank=True, null=True)
    beneficiario = models.CharField(max_length=100, blank=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    monto_deposito = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fecha_deposito = models.DateTimeField(blank=True, null=True)
    codigo_depto_deposito = models.CharField(max_length=2, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_depositos'

class PpDepositosReintegros(models.Model):
    anio_deposito = models.CharField(max_length=4)
    tipo_pago_deposito = models.CharField(max_length=2)
    numero_deposito = models.CharField(max_length=6)
    monto_reintegro = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    numero_cheque_caja = models.CharField(max_length=20, blank=True)
    codigo_motivo = models.IntegerField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_depositos_reintegros'

class PpDepurarMovimientos(models.Model):
    codigo_periodo = models.CharField(max_length=6)
    identidad_empleado = models.CharField(max_length=13)
    cuenta = models.CharField(max_length=50)
    codigo_movimiento_antes = models.IntegerField(blank=True, null=True)
    codigo_motivo_antes = models.IntegerField(blank=True, null=True)
    codigo_movimiento = models.IntegerField(blank=True, null=True)
    codigo_motivo = models.IntegerField(blank=True, null=True)
    fecha_inicial = models.DateTimeField(blank=True, null=True)
    fecha_final = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_depurar_movimientos'

class PpDescripcionEstSiafi(models.Model):
    corrent = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    descripcion_corrent = models.CharField(max_length=50, blank=True)
    programa = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    descripcion_programa = models.CharField(max_length=50, blank=True)
    subprograma = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    descripcion_subprograma = models.CharField(max_length=50, blank=True)
    proyecto = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    descripcion_proyecto = models.CharField(max_length=50, blank=True)
    actobra = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    descripcion_actividad = models.CharField(max_length=50, blank=True)
    partida = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    descripcion_partida = models.CharField(max_length=50, blank=True)
    codfte = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    descripcion_codfte = models.CharField(max_length=50, blank=True)
    org_financ = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    descripcion_org_financ = models.CharField(max_length=50, blank=True)
    codigo_benef = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    descripcion_codigo_benef = models.CharField(max_length=50, blank=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    gerencia_admon = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    unidad_ejecutora = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_descripcion_est_siafi'

class PpDesgloseCargos(models.Model):
    codigo_nivel_cargo = models.IntegerField(primary_key=True)
    desglose_cargo = models.CharField(max_length=25)
    longitud_desglose = models.IntegerField()
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_desglose_cargos'

class PpDetMovPlazas(models.Model):
    codigo_mov_plaza = models.CharField(max_length=20)
    cuenta = models.ForeignKey(PpCatalogos, db_column='cuenta')
    codigo_cargo = models.ForeignKey(PpCargos, db_column='codigo_cargo', blank=True, null=True)
    horas_plaza = models.IntegerField(blank=True, null=True)
    horario = models.IntegerField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_det_mov_plazas'

class PpDetPresupAdmon(models.Model):
    codigo_periodo = models.ForeignKey('PpPeriodos', db_column='codigo_periodo')
    cuenta = models.ForeignKey(PpCatalogos, db_column='cuenta')
    codigo_presupuesto = models.ForeignKey('PpEncabezadoPresupuestos', db_column='codigo_presupuesto')
    presupuesto_original = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_solicitado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_bajo_techo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_anio_anterior = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    modif_aumento_monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    modif_mas = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    modif_menos = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_modificado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    congelamiento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    pagos_ejecutados = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    excedente = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    deficit = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    disponible_total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_comprometido = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_ordenado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    codigo_carga = models.CharField(max_length=10, blank=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_det_presup_admon'

class PpDetalleAcuerdo(models.Model):
    secuencial_detalle_acuerdo = models.IntegerField()
    numero_acuerdo = models.ForeignKey(PpAcuerdos, db_column='numero_acuerdo')
    codigo_modalidad = models.ForeignKey('PpModalidades', db_column='codigo_modalidad')
    codigo_asignatura = models.ForeignKey(PpAsignaturas, db_column='codigo_asignatura')
    curso = models.CharField(max_length=3)
    seccion = models.CharField(max_length=3)
    horas_clase = models.IntegerField()
    lunes = models.SmallIntegerField(blank=True, null=True)
    martes = models.SmallIntegerField(blank=True, null=True)
    miercoles = models.SmallIntegerField(blank=True, null=True)
    jueves = models.SmallIntegerField(blank=True, null=True)
    viernes = models.SmallIntegerField(blank=True, null=True)
    sabado = models.SmallIntegerField(blank=True, null=True)
    domingo = models.SmallIntegerField(blank=True, null=True)
    horas_ini_lunes = models.CharField(max_length=15, blank=True)
    horas_fin_lunes = models.CharField(max_length=15, blank=True)
    horas_ini_martes = models.CharField(max_length=15, blank=True)
    horas_fin_martes = models.CharField(max_length=15, blank=True)
    horas_ini_miercoles = models.CharField(max_length=15, blank=True)
    horas_fin_miercoles = models.CharField(max_length=15, blank=True)
    horas_ini_jueves = models.CharField(max_length=15, blank=True)
    horas_fin_jueves = models.CharField(max_length=15, blank=True)
    horas_ini_viernes = models.CharField(max_length=15, blank=True)
    horas_fin_viernes = models.CharField(max_length=15, blank=True)
    horas_ini_sabado = models.CharField(max_length=15, blank=True)
    horas_fin_sabado = models.CharField(max_length=15, blank=True)
    horas_ini_domingo = models.CharField(max_length=15, blank=True)
    horas_fin_domingo = models.CharField(max_length=15, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_detalle_acuerdo'

class PpDetalleModificaciones(models.Model):
    codigo_modificacion_pres = models.CharField(max_length=20)
    codigo_presupuesto = models.IntegerField()
    cuenta = models.ForeignKey(PpCatalogos, db_column='cuenta')
    codigo_periodo = models.ForeignKey('PpPeriodos', db_column='codigo_periodo')
    monto_decrementado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_incrementado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_detalle_modificaciones'

class PpDetallePeticiones(models.Model):
    numero_peticion_detalle = models.IntegerField()
    codigo_razon = models.ForeignKey('PpRazonesPeticion', db_column='codigo_razon')
    codigo_cargo = models.ForeignKey(PpCargos, db_column='codigo_cargo')
    codigo_modalidad = models.ForeignKey('PpModalidades', db_column='codigo_modalidad', blank=True, null=True)
    codigo_peticion = models.CharField(max_length=20)
    curso = models.CharField(max_length=25)
    horas = models.IntegerField(blank=True, null=True)
    grupo = models.CharField(max_length=2)
    tipo_plaza = models.SmallIntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_detalle_peticiones'

class PpDetallePresupuestos(models.Model):
    codigo_periodo = models.ForeignKey('PpPeriodos', db_column='codigo_periodo')
    cuenta = models.ForeignKey(PpCatalogos, db_column='cuenta')
    codigo_presupuesto = models.ForeignKey('PpEncabezadoPresupuestos', db_column='codigo_presupuesto')
    presupuesto_original = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_solicitado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_bajo_techo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_anio_anterior = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    modif_aumento_monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    modif_mas = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    modif_menos = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_modificado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    congelamiento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    pagos_ejecutados = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    excedente = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    deficit = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    disponible_total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_comprometido = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_ordenado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    codigo_carga = models.CharField(max_length=10, blank=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_detalle_presupuestos'

class PpDetalleRecepcionDoctos(models.Model):
    codigo_recepcion = models.CharField(max_length=20)
    codigo_unidad = models.CharField(max_length=1)
    identidad_empleado = models.ForeignKey('PpEmpleados', db_column='identidad_empleado')
    numero_oficio = models.CharField(max_length=50, blank=True)
    xnearmensaje = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    documentos_entregados = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_detalle_recepcion_doctos'

class PpDetalleReclamosPagos(models.Model):
    codigo_transaccion = models.IntegerField()
    item_matricial = models.IntegerField()
    codigo_reclamo = models.CharField(max_length=20)
    cuenta = models.CharField(max_length=50)
    cuenta_siafi = models.CharField(max_length=50, blank=True)
    cuenta_siafi_format = models.CharField(max_length=50, blank=True)
    codigo_periodo_ini = models.CharField(max_length=6)
    codigo_periodo_fin = models.CharField(max_length=6)
    descripcion_departamento = models.CharField(max_length=50, blank=True)
    descripcion_municipio = models.CharField(max_length=50, blank=True)
    descripcion_centro = models.CharField(max_length=50, blank=True)
    descripcion_transaccion = models.CharField(max_length=50, blank=True)
    descripcion_periodo_ini = models.CharField(max_length=20, blank=True)
    descripcion_periodo_fin = models.CharField(max_length=20, blank=True)
    monto_periodo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    sueldo_nominal = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    aplicar_deduccion = models.CharField(max_length=1, blank=True)
    inprema_patronal = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    inprema_docente = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    xnearmensaje = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_detalle_reclamos_pagos'

class PpDetalleReparos(models.Model):
    codigo_reparo = models.ForeignKey('PpReparos', db_column='codigo_reparo')
    identidad_empleado = models.CharField(max_length=13)
    cuenta = models.CharField(max_length=50)
    codigo_transaccion = models.IntegerField()
    periodo_detalle_reparo = models.CharField(max_length=6)
    monto = models.DecimalField(max_digits=18, decimal_places=2)
    observacion = models.TextField()
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    usuario_aplico = models.CharField(max_length=25)
    class Meta:
        managed = False
        db_table = 'pp_detalle_reparos'

class PpDifuntos(models.Model):
    identidad = models.CharField(db_column='Identidad', max_length=13) # Field name made lowercase.
    primer_nombre = models.CharField(db_column='Primer_Nombre', max_length=50, blank=True) # Field name made lowercase.
    segundo_nombre = models.CharField(db_column='Segundo_Nombre', max_length=50, blank=True) # Field name made lowercase.
    primer_apellido = models.CharField(db_column='Primer_Apellido', max_length=50, blank=True) # Field name made lowercase.
    segundo_apellido = models.CharField(db_column='Segundo_Apellido', max_length=50, blank=True) # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=1, blank=True) # Field name made lowercase.
    fecha_nacimiento_txt = models.CharField(db_column='Fecha_Nacimiento_txt', max_length=10, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'pp_difuntos'

class PpDistribucionPlazas(models.Model):
    codigo_presupuesto = models.ForeignKey('PpEncPresupuestoNuevo', db_column='codigo_presupuesto')
    codigo_departamento = models.ForeignKey(PpCentrosEducativos, db_column='codigo_departamento')
    codigo_municipio = models.ForeignKey(PpCentrosEducativos, db_column='codigo_municipio')
    codigo_centro = models.ForeignKey(PpCentrosEducativos, db_column='codigo_centro')
    codigo_nivel_educativo = models.ForeignKey('PpNivelesEducativos', db_column='codigo_nivel_educativo')
    estado_documento = models.ForeignKey('PpEstadosDocumentos', db_column='estado_documento', blank=True, null=True)
    codigo_razon = models.ForeignKey('PpMotivosRechazos', db_column='codigo_razon', blank=True, null=True)
    total_plazas_disponibles = models.IntegerField(blank=True, null=True)
    total_horas_disponibles = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    codigo_municipio_anterior = models.CharField(max_length=2, blank=True)
    codigo_centro_anterior = models.CharField(max_length=5, blank=True)
    municipio_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_distribucion_plazas'

class PpDistritos(models.Model):
    codigo_distrito = models.IntegerField(primary_key=True)
    codigo_departamento = models.ForeignKey(PpDepartamentos, db_column='codigo_departamento')
    descripcion_distrito = models.CharField(max_length=25)
    abreviacion_distrito = models.CharField(max_length=15)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_distritos'

class PpDocumentosRequisitos(models.Model):
    codigo_requisito = models.IntegerField(primary_key=True)
    codigo_categoria = models.ForeignKey('PpXcategorias', db_column='codigo_categoria')
    descripcion_requisito = models.CharField(max_length=100)
    abreviatura_requisito = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_documentos_requisitos'

class PpEjecucionTransacciones(models.Model):
    codigo_planilla = models.ForeignKey('PpPlanillas', db_column='codigo_planilla')
    codigo_transaccion = models.ForeignKey('PpTransacciones', db_column='codigo_transaccion')
    clase_transaccion = models.SmallIntegerField()
    monto_transaccion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_ejecucion_transacciones'

class PpEjecuciones(models.Model):
    codigo_planilla = models.ForeignKey('PpPlanillas', db_column='codigo_planilla')
    codigo_ct = models.ForeignKey(PpCodigosCt, db_column='codigo_ct', blank=True, null=True)
    estructura_ejecucion = models.CharField(max_length=50, blank=True)
    clave_pad = models.CharField(max_length=5, blank=True)
    cuenta_ingresos = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    monto_ejecutado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_ejec_anterior = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descripcion_ejecucion = models.CharField(max_length=100, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_ejecuciones'

class PpEmbargosDocente(models.Model):
    identidad_empleado = models.CharField(max_length=13)
    porcentaje_embargo = models.DecimalField(max_digits=4, decimal_places=2)
    estado = models.IntegerField()
    codigo_transaccion = models.IntegerField()
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    usuario_aprobar = models.CharField(max_length=25, blank=True)
    fecha_aprobar = models.DateTimeField(blank=True, null=True)
    fecha_inicial = models.DateTimeField(blank=True, null=True)
    fecha_final = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    codigo_embargo = models.CharField(primary_key=True, max_length=20)
    monto_embargo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    aplicar_porcentaje = models.IntegerField(blank=True, null=True)
    aplicar_monto = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_embargos_docente'

class PpEmpleados(models.Model):
    identidad_empleado = models.CharField(primary_key=True, max_length=13)
    codigo_tipo_empleado = models.ForeignKey('PpTipoEmpleados', db_column='codigo_tipo_empleado', blank=True, null=True)
    codigo_grado_academico = models.ForeignKey('PpGradosAcademicos', db_column='codigo_grado_academico', blank=True, null=True)
    codigo_centro_estudio = models.ForeignKey(PpCentrosEstudios, db_column='codigo_centro_estudio', blank=True, null=True)
    codigo_titulo = models.ForeignKey('PpTitulos', db_column='codigo_titulo', blank=True, null=True)
    codigo_tipo_profesional = models.ForeignKey('PpTipoProfesionales', db_column='codigo_tipo_profesional', blank=True, null=True)
    estado_profesionalizacion = models.SmallIntegerField(blank=True, null=True)
    codigo_pais = models.ForeignKey('PpPaises', db_column='codigo_pais')
    codigo_departamento = models.ForeignKey(PpCentrosPago, db_column='codigo_departamento', blank=True, null=True)
    codigo_municipio = models.ForeignKey(PpCentrosPago, db_column='codigo_municipio', blank=True, null=True)
    codigo_centro_pago = models.ForeignKey(PpCentrosPago, db_column='codigo_centro_pago', blank=True, null=True)
    clave_escalafon = models.CharField(max_length=15, blank=True)
    identidad_as = models.CharField(max_length=13, blank=True)
    nombres_empleado = models.CharField(max_length=35)
    apellidos_empleado = models.CharField(max_length=35)
    estado_civil = models.CharField(max_length=1, blank=True)
    sexo_empleado = models.CharField(max_length=1)
    codigo_departamento_nac = models.CharField(max_length=2, blank=True)
    codigo_municipio_nac = models.CharField(max_length=3, blank=True)
    codigo_aldea_nac = models.CharField(max_length=5, blank=True)
    fecha_nacimiento = models.DateTimeField()
    telefono_1 = models.CharField(max_length=15, blank=True)
    telefono_2 = models.CharField(max_length=15, blank=True)
    telefono_3 = models.CharField(max_length=15, blank=True)
    codigo_inprema = models.CharField(max_length=13, blank=True)
    codigo_ihss = models.CharField(max_length=13, blank=True)
    departamento_reside = models.CharField(max_length=2)
    municipio_reside = models.CharField(max_length=3)
    direccion_actual = models.CharField(max_length=100)
    fecha_inscripcion = models.DateTimeField(blank=True, null=True)
    anios_servicios_actual = models.IntegerField(blank=True, null=True)
    meses_servicios_actual = models.IntegerField(blank=True, null=True)
    dias_servicios_actual = models.IntegerField(blank=True, null=True)
    horas_servicios_actual = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fecha_ultimo_analisis_anios = models.DateTimeField(blank=True, null=True)
    acumula_anios = models.SmallIntegerField(blank=True, null=True)
    ultima_categoria = models.IntegerField()
    estado_docente = models.ForeignKey('PpEstadosDocente', db_column='estado_docente', blank=True, null=True)
    direccion_especifica = models.CharField(max_length=250, blank=True)
    forma_pago_docente = models.SmallIntegerField(blank=True, null=True)
    estado_habilitado = models.SmallIntegerField(blank=True, null=True)
    codigo_barra_expediente = models.CharField(max_length=7, blank=True)
    carnet_emitido = models.SmallIntegerField(blank=True, null=True)
    carnet_entregado = models.SmallIntegerField(blank=True, null=True)
    modifica_centro_pago = models.SmallIntegerField(blank=True, null=True)
    fecha_ultima_impresion = models.DateTimeField(blank=True, null=True)
    registrado_tiempo_servicio = models.SmallIntegerField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modif_anios = models.CharField(max_length=25, blank=True)
    fecha_modif_anios = models.DateTimeField(blank=True, null=True)
    usuario_modif_centro = models.CharField(max_length=25, blank=True)
    fecha_modif_centro = models.DateTimeField(blank=True, null=True)
    usuario_modif_profesional = models.CharField(max_length=25, blank=True)
    fecha_modif_profesional = models.DateTimeField(blank=True, null=True)
    usuario_modif_estado = models.CharField(max_length=25, blank=True)
    fecha_modif_estado = models.DateTimeField(blank=True, null=True)
    codigo_banco = models.IntegerField(blank=True, null=True)
    codigo_cuenta = models.CharField(max_length=25, blank=True)
    codigo_municipio_anterior = models.CharField(max_length=2, blank=True)
    codigo_municipio_nac_anterior = models.CharField(max_length=2, blank=True)
    municipio_reside_anterior = models.CharField(max_length=2, blank=True)
    municipio_depurado = models.CharField(max_length=1, blank=True)
    municipio_nac_depurado = models.CharField(max_length=1, blank=True)
    municipio_reside_depurado = models.CharField(max_length=1, blank=True)
    codigo_depto_nac_anterior = models.CharField(max_length=2, blank=True)
    depto_reside_anterior = models.CharField(max_length=2, blank=True)
    usuario_modif_categoria = models.CharField(max_length=25, blank=True)
    fecha_modif_categoria = models.DateTimeField(blank=True, null=True)
    categoria_anterior = models.IntegerField(blank=True, null=True)
    fecha_modif_forma_pago = models.DateTimeField(blank=True, null=True)
    usuario_modif_forma_pago = models.CharField(max_length=25, blank=True)
    categoria_original = models.IntegerField(blank=True, null=True)
    dep_codigo_tipo_profesional = models.ForeignKey('PpTipoProfesionales', db_column='dep_codigo_tipo_profesional', blank=True, null=True)
    dep_codigo_centro_estudio = models.ForeignKey(PpCentrosEstudios, db_column='dep_codigo_centro_estudio', blank=True, null=True)
    dep_codigo_grado_academico = models.ForeignKey('PpGradosAcademicos', db_column='dep_codigo_grado_academico', blank=True, null=True)
    dep_codigo_titulo = models.ForeignKey('PpTitulos', db_column='dep_codigo_titulo', blank=True, null=True)
    usuario_modif_dep_profesional = models.CharField(max_length=25, blank=True)
    usuario_modif_dep_grado = models.CharField(max_length=25, blank=True)
    usuario_modif_dep_centro = models.CharField(max_length=25, blank=True)
    usuario_modif_dep_titulo = models.CharField(max_length=25, blank=True)
    fecha_modif_dep_profesional = models.DateTimeField(blank=True, null=True)
    fecha_modif_dep_grado = models.DateTimeField(blank=True, null=True)
    fecha_modif_dep_centro = models.DateTimeField(blank=True, null=True)
    fecha_modif_dep_titulo = models.DateTimeField(blank=True, null=True)
    fecha_modif_fecha_nac = models.DateTimeField(blank=True, null=True)
    usuario_modif_fecha_nac = models.CharField(max_length=25, blank=True)
    usuario_modif_nombres = models.CharField(max_length=25, blank=True)
    fecha_modif_nombres = models.DateTimeField(blank=True, null=True)
    usuario_modif_apellidos = models.CharField(max_length=25, blank=True)
    fecha_modif_apellidos = models.DateTimeField(blank=True, null=True)
    usuario_modif_genero = models.CharField(max_length=25, blank=True)
    fecha_modif_genero = models.DateTimeField(blank=True, null=True)
    codigo_barra_identidad = models.IntegerField(blank=True, null=True)
    codigo_tipo_id = models.CharField(max_length=3)
    vigente = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'pp_empleados'

class PpEncAnexoAdmon(models.Model):
    anio_anexo = models.IntegerField()
    codigo_departamento = models.ForeignKey(PpDepartamentos, db_column='codigo_departamento')
    estado_anexo = models.SmallIntegerField(blank=True, null=True)
    total_plazas = models.IntegerField(blank=True, null=True)
    monto_bajo_techo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_proyectado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_enc_anexo_admon'

class PpEncMovPlazas(models.Model):
    cuenta = models.ForeignKey(PpCatalogos, db_column='cuenta')
    codigo_mov_plaza = models.CharField(primary_key=True, max_length=20)
    estado_documento = models.ForeignKey('PpEstadosDocumentos', db_column='estado_documento', blank=True, null=True)
    codigo_presupuesto = models.ForeignKey('PpEncabezadoPresupuestos', db_column='codigo_presupuesto')
    codigo_cargo = models.ForeignKey(PpCargos, db_column='codigo_cargo', blank=True, null=True)
    estado_plaza = models.IntegerField(blank=True, null=True)
    tipo_movimiento = models.SmallIntegerField()
    fecha_mov_plaza = models.DateTimeField()
    detalle_mov_plaza = models.TextField(blank=True)
    horas_nuevas = models.IntegerField(blank=True, null=True)
    horas_viejas = models.IntegerField(blank=True, null=True)
    horario_plaza = models.SmallIntegerField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_enc_mov_plazas'

class PpEncPresupuestoNuevo(models.Model):
    anio_presupuesto = models.IntegerField(blank=True, null=True)
    codigo_presupuesto = models.IntegerField(unique=True)
    descripcion_presupuesto = models.CharField(max_length=50, blank=True)
    estado_presupuesto = models.SmallIntegerField()
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_enc_presupuesto_nuevo'

class PpEncabezadoAnexo(models.Model):
    anio_anexo = models.IntegerField()
    codigo_departamento = models.ForeignKey(PpDepartamentos, db_column='codigo_departamento')
    estado_anexo = models.SmallIntegerField(blank=True, null=True)
    total_plazas = models.IntegerField(blank=True, null=True)
    monto_bajo_techo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_proyectado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_encabezado_anexo'

class PpEncabezadoConversiones(models.Model):
    codigo_conversion = models.IntegerField(primary_key=True)
    descripcion_encabezado = models.CharField(max_length=255)
    anio_enlace = models.IntegerField(blank=True, null=True)
    estado_conversion = models.SmallIntegerField()
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_encabezado_conversiones'

class PpEncabezadoModificaciones(models.Model):
    codigo_modificacion_pres = models.CharField(max_length=20)
    codigo_presupuesto = models.ForeignKey('PpEncabezadoPresupuestos', db_column='codigo_presupuesto')
    codigo_modificacion_global = models.CharField(max_length=20, blank=True)
    codigo_mov_presupuestario = models.ForeignKey('PpMovimientosPresupuestarios', db_column='codigo_mov_presupuestario')
    estado_documento = models.ForeignKey('PpEstadosDocumentos', db_column='estado_documento')
    fecha_consolidacion = models.DateTimeField(blank=True, null=True)
    fecha_solicitud = models.DateTimeField(blank=True, null=True)
    numero_resolucion = models.CharField(max_length=20, blank=True)
    fecha_resolucion = models.DateTimeField(blank=True, null=True)
    numero_documento_siafi = models.CharField(max_length=5, blank=True)
    fecha_documento_siafi = models.DateTimeField(blank=True, null=True)
    tipo_modificacion = models.SmallIntegerField()
    detalle_modificacion = models.CharField(max_length=50, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_encabezado_modificaciones'

class PpEncabezadoPeticion(models.Model):
    anio_peticion = models.IntegerField()
    codigo_departamento = models.ForeignKey(PpDepartamentos, db_column='codigo_departamento')
    secuencial_peticion = models.IntegerField()
    estado_peticion = models.SmallIntegerField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_encabezado_peticion'

class PpEncabezadoPresupuestos(models.Model):
    anio_presupuesto = models.IntegerField()
    codigo_presupuesto = models.IntegerField(primary_key=True)
    descripcion_presupuesto = models.CharField(max_length=25, blank=True)
    estado_presupuesto = models.SmallIntegerField()
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_encabezado_presupuestos'

class PpEquivalencia2010(models.Model):
    ano2010 = models.CharField(db_column='Ano2010', max_length=255, blank=True) # Field name made lowercase.
    sip_tit2010 = models.CharField(db_column='sip_Tit2010', max_length=255, blank=True) # Field name made lowercase.
    sip_pro2010 = models.CharField(db_column='sip_Pro2010', max_length=255, blank=True) # Field name made lowercase.
    sip_spro2010 = models.CharField(db_column='sip_Spro2010', max_length=255, blank=True) # Field name made lowercase.
    sip_act2010 = models.CharField(db_column='sip_Act2010', max_length=255, blank=True) # Field name made lowercase.
    sip_fdo2010 = models.CharField(db_column='sip_Fdo2010', max_length=255, blank=True) # Field name made lowercase.
    sip_rgn2010 = models.CharField(db_column='sip_Rgn2010', max_length=255, blank=True) # Field name made lowercase.
    sip_obj2010 = models.CharField(db_column='sip_Obj2010', max_length=255, blank=True) # Field name made lowercase.
    sip_clave2010 = models.CharField(db_column='sip_Clave2010', max_length=255, blank=True) # Field name made lowercase.
    gestion2010 = models.CharField(db_column='Gestion2010', max_length=255, blank=True) # Field name made lowercase.
    inst2010 = models.CharField(db_column='Inst2010', max_length=255, blank=True) # Field name made lowercase.
    ga2010 = models.CharField(db_column='GA2010', max_length=255, blank=True) # Field name made lowercase.
    ue2010 = models.CharField(db_column='UE2010', max_length=255, blank=True) # Field name made lowercase.
    pro2010 = models.CharField(db_column='Pro2010', max_length=255, blank=True) # Field name made lowercase.
    spro2010 = models.CharField(db_column='Spro2010', max_length=255, blank=True) # Field name made lowercase.
    proy2010 = models.CharField(db_column='Proy2010', max_length=255, blank=True) # Field name made lowercase.
    act2010 = models.CharField(db_column='Act2010', max_length=255, blank=True) # Field name made lowercase.
    fte2010 = models.CharField(db_column='Fte2010', max_length=255, blank=True) # Field name made lowercase.
    ofin2010 = models.CharField(db_column='OFin2010', max_length=255, blank=True) # Field name made lowercase.
    obj2010 = models.CharField(db_column='Obj2010', max_length=255, blank=True) # Field name made lowercase.
    benef2010 = models.CharField(db_column='Benef2010', max_length=255, blank=True) # Field name made lowercase.
    gestion2009 = models.CharField(db_column='Gestion2009', max_length=255, blank=True) # Field name made lowercase.
    inst2009 = models.CharField(db_column='Inst2009', max_length=255, blank=True) # Field name made lowercase.
    ga2009 = models.CharField(db_column='GA2009', max_length=255, blank=True) # Field name made lowercase.
    ue2009 = models.CharField(db_column='UE2009', max_length=255, blank=True) # Field name made lowercase.
    pro2009 = models.CharField(db_column='Pro2009', max_length=255, blank=True) # Field name made lowercase.
    spro2009 = models.CharField(db_column='Spro2009', max_length=255, blank=True) # Field name made lowercase.
    proy2009 = models.CharField(db_column='Proy2009', max_length=255, blank=True) # Field name made lowercase.
    act2009 = models.CharField(db_column='Act2009', max_length=255, blank=True) # Field name made lowercase.
    fte2009 = models.CharField(db_column='Fte2009', max_length=255, blank=True) # Field name made lowercase.
    ofin2009 = models.CharField(db_column='OFin2009', max_length=255, blank=True) # Field name made lowercase.
    obj2009 = models.CharField(db_column='Obj2009', max_length=255, blank=True) # Field name made lowercase.
    benef2009 = models.CharField(db_column='Benef2009', max_length=255, blank=True) # Field name made lowercase.
    aprobadosiarhd2010 = models.CharField(db_column='AprobadoSIARHD2010', max_length=255, blank=True) # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'pp_equivalencia_2010'

class PpEquivalenciaSipSiafi2007(models.Model):
    anio = models.IntegerField()
    estructura_sip = models.CharField(max_length=25)
    estructura_siafi = models.CharField(max_length=50)
    clave_pad = models.CharField(max_length=5)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    tipo_estructura = models.IntegerField(blank=True, null=True)
    siafi_new = models.CharField(max_length=50, blank=True)
    sip_new = models.CharField(max_length=50, blank=True)
    clave_padnew = models.CharField(max_length=5, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_equivalencia_sip_siafi_2007'

class PpEquivalenciaSipSiafiCopia2009(models.Model):
    anio = models.IntegerField()
    estructura_sip = models.CharField(max_length=25)
    estructura_siafi = models.CharField(max_length=50)
    clave_pad = models.CharField(max_length=5)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    tipo_estructura = models.IntegerField()
    siafi_new = models.CharField(max_length=50, blank=True)
    sip_new = models.CharField(max_length=50, blank=True)
    clave_padnew = models.CharField(max_length=5, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_equivalencia_sip_siafi_copia_2009'

class PpErrores(models.Model):
    codigo_error = models.IntegerField(unique=True)
    mensaje_error = models.CharField(max_length=250, blank=True)
    tipo_icon = models.CharField(max_length=20, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_errores'

class PpEstadiosAcademicos(models.Model):
    codigo_estadio = models.IntegerField(primary_key=True)
    descripcion_estadio = models.CharField(max_length=30)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_estadios_academicos'

class PpEstadosCheque(models.Model):
    estado_cheque = models.SmallIntegerField(primary_key=True)
    descripcion_cheque = models.CharField(max_length=20)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'pp_estados_cheque'

class PpEstadosDocente(models.Model):
    estado_docente = models.SmallIntegerField(unique=True)
    descripcion_estado = models.CharField(max_length=25)
    abreviatura_estado = models.CharField(max_length=10, blank=True)
    observacion_estado = models.CharField(max_length=250, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_estados_docente'

class PpEstadosDocumentos(models.Model):
    estado_documento = models.SmallIntegerField(primary_key=True)
    descripcion_estado = models.CharField(max_length=20)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_estados_documentos'

class PpEstadosPlazas(models.Model):
    codigo_estado = models.SmallIntegerField(primary_key=True)
    descripcion_estado = models.CharField(max_length=50)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    observacion = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_estados_plazas'

class PpEstructurasSipSiafi(models.Model):
    anio = models.IntegerField(db_column='Anio', blank=True, null=True) # Field name made lowercase.
    sip_tit = models.CharField(db_column='SIP_TIT', max_length=3, blank=True) # Field name made lowercase.
    sip_prog = models.CharField(db_column='SIP_PROG', max_length=3, blank=True) # Field name made lowercase.
    sip_spr = models.CharField(db_column='SIP_SPR', max_length=2, blank=True) # Field name made lowercase.
    sip_act = models.CharField(db_column='SIP_ACT', max_length=2, blank=True) # Field name made lowercase.
    sip_fdo = models.CharField(db_column='SIP_FDO', max_length=2, blank=True) # Field name made lowercase.
    sip_rgl = models.CharField(db_column='SIP_RGL', max_length=3, blank=True) # Field name made lowercase.
    sip_obj = models.CharField(db_column='SIP_OBJ', max_length=3, blank=True) # Field name made lowercase.
    clave_pad = models.DecimalField(db_column='CLAVE_PAD', max_digits=5, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    sia_inst = models.CharField(db_column='SIA_INST', max_length=2, blank=True) # Field name made lowercase.
    sia_prog = models.CharField(db_column='SIA_PROG', max_length=2, blank=True) # Field name made lowercase.
    sia_spr = models.CharField(db_column='SIA_SPR', max_length=2, blank=True) # Field name made lowercase.
    sia_proy = models.CharField(db_column='SIA_PROY', max_length=2, blank=True) # Field name made lowercase.
    sia_act = models.CharField(db_column='SIA_ACT', max_length=2, blank=True) # Field name made lowercase.
    sia_obj = models.CharField(db_column='SIA_OBJ', max_length=3, blank=True) # Field name made lowercase.
    sia_fdo = models.CharField(db_column='SIA_FDO', max_length=2, blank=True) # Field name made lowercase.
    sia_org = models.CharField(db_column='SIA_ORG', max_length=3, blank=True) # Field name made lowercase.
    sia_ben = models.CharField(db_column='SIA_BEN', max_length=4, blank=True) # Field name made lowercase.
    presupuestado = models.DecimalField(db_column='PRESUPUESTADO', max_digits=18, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    tipo_estructura = models.CharField(db_column='TIPO_ESTRUCTURA', max_length=50, blank=True) # Field name made lowercase.
    cod_departamento = models.CharField(db_column='COD_DEPARTAMENTO', max_length=2, blank=True) # Field name made lowercase.
    departamento = models.CharField(db_column='DEPARTAMENTO', max_length=25, blank=True) # Field name made lowercase.
    cod_nivel = models.IntegerField(db_column='COD_NIVEL', blank=True, null=True) # Field name made lowercase.
    nivel_educativo = models.CharField(db_column='NIVEL_EDUCATIVO', max_length=25, blank=True) # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=100, blank=True) # Field name made lowercase.
    estructura_siafi = models.CharField(db_column='ESTRUCTURA_SIAFI', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'pp_estructuras_sip_siafi'

class PpEstudiosMeritos(models.Model):
    oficio_dictamen_meritos = models.ForeignKey('PpResumenMeritos', db_column='oficio_dictamen_meritos')
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    secuencial_meritos = models.IntegerField()
    fecha_estudio_meritos = models.DateTimeField()
    codigo_logro = models.IntegerField(blank=True, null=True)
    codigo_meritos = models.IntegerField(blank=True, null=True)
    cod_institucion_merito = models.IntegerField(blank=True, null=True)
    estado_documento = models.SmallIntegerField(blank=True, null=True)
    fecha_obtencion_meritos = models.DateTimeField()
    puntos_acumulados = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    observaciones_meritos = models.CharField(max_length=200, blank=True)
    fecha_vigencia_meritos = models.DateTimeField(blank=True, null=True)
    xnearmensaje = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    notificado_meritos = models.SmallIntegerField()
    tiempo_vigencia = models.IntegerField(blank=True, null=True)
    descripcion_merito_obtenido = models.CharField(max_length=100, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_estudios_meritos'

class PpEvaluacionDesempenios(models.Model):
    codigo_tipo_evaluacion = models.ForeignKey(PpCriteriosTipos, db_column='codigo_tipo_evaluacion')
    codigo_criterio = models.ForeignKey(PpCriteriosTipos, db_column='codigo_criterio')
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    fecha_evaluacion = models.DateTimeField()
    puntaje_obtenido = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    puntaje_maximo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_evaluacion_desempenios'

class PpExcepcionesCalificacion(models.Model):
    identidad_empleado = models.CharField(max_length=13, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_excepciones_calificacion'

class PpExcluidosCargoAdmon(models.Model):
    identidad_empleado = models.CharField(primary_key=True, max_length=13)
    tipo_profesional_actual = models.CharField(max_length=3, blank=True)
    tipo_profesional_pagar = models.CharField(max_length=3, blank=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_excluidos_cargo_admon'

class PpExcluidosInprema(models.Model):
    identidad_empleado = models.CharField(max_length=13)
    excluido = models.CharField(max_length=1)
    periodo_activacion = models.CharField(max_length=6)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    periodo_desactivacion = models.CharField(max_length=6, blank=True)
    codigo_ex_inprema = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'pp_excluidos_inprema'

class PpExonerados(models.Model):
    codigo_unidad = models.ForeignKey('PpUnidadesEjecutoras', db_column='codigo_unidad')
    anio_exoneracion = models.IntegerField()
    codigo_registro = models.IntegerField()
    fecha_exoneracion = models.DateTimeField(blank=True, null=True)
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    estado_candidatura = models.SmallIntegerField()
    fecha_ultimo_estado = models.DateTimeField()
    aplica_interinato = models.SmallIntegerField()
    aplica_rural = models.SmallIntegerField()
    acta_exoneracion = models.CharField(max_length=25)
    folio_exoneracion = models.CharField(max_length=25)
    observaciones_exoneracion = models.TextField(blank=True)
    nivel_educ_exoneracion = models.IntegerField(blank=True, null=True)
    codigo_departamento = models.CharField(max_length=2)
    codigo_municipio = models.CharField(max_length=2)
    codigo_centro = models.CharField(max_length=5)
    tipo_centro_exoneracion = models.IntegerField()
    clase_centro_exoneracion = models.IntegerField()
    cuenta_exoneracion = models.ForeignKey('PpPlazas', db_column='cuenta_exoneracion')
    cargo_exoneracion = models.CharField(max_length=15)
    horario_plaza = models.IntegerField(blank=True, null=True)
    horas_plaza = models.IntegerField(blank=True, null=True)
    anios_servicio_exoneracion = models.IntegerField()
    meses_servicio_exoneracion = models.IntegerField()
    dias_servicio_exoneracion = models.IntegerField()
    horas_servicio_exoneracion = models.IntegerField()
    fecha_actual_servicio = models.DateTimeField()
    secuencial_seleccion = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_exonerados'

class PpExpedientesTmp(models.Model):
    idexpediente = models.IntegerField(db_column='IDEXPEDIENTE', blank=True, null=True) # Field name made lowercase.
    idpaquete = models.IntegerField(db_column='IDPAQUETE', blank=True, null=True) # Field name made lowercase.
    categoria = models.CharField(db_column='CATEGORIA', max_length=50, blank=True) # Field name made lowercase.
    inicial = models.CharField(db_column='INICIAL', max_length=50, blank=True) # Field name made lowercase.
    idescalafon = models.IntegerField(db_column='IDESCALAFON', blank=True, null=True) # Field name made lowercase.
    identidad = models.CharField(db_column='IDENTIDAD', max_length=50, blank=True) # Field name made lowercase.
    nombre1 = models.CharField(db_column='NOMBRE1', max_length=50, blank=True) # Field name made lowercase.
    nombre2 = models.CharField(db_column='NOMBRE2', max_length=50, blank=True) # Field name made lowercase.
    apellido1 = models.CharField(db_column='APELLIDO1', max_length=50, blank=True) # Field name made lowercase.
    apellido2 = models.CharField(db_column='APELLIDO2', max_length=50, blank=True) # Field name made lowercase.
    nombre_completo = models.CharField(db_column='NOMBRE_COMPLETO', max_length=50, blank=True) # Field name made lowercase.
    clave_escalafon = models.CharField(db_column='CLAVE_ESCALAFON', max_length=50, blank=True) # Field name made lowercase.
    identidad_empleado = models.CharField(db_column='IDENTIDAD_EMPLEADO', max_length=13, blank=True) # Field name made lowercase.
    en_siarhd = models.SmallIntegerField(db_column='EN_SIARHD', blank=True, null=True) # Field name made lowercase.
    en_periodo = models.SmallIntegerField(db_column='EN_PERIODO', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'pp_expedientes_tmp'

class PpFallosEstadoCuenta(models.Model):
    codigo_barra_leido = models.CharField(max_length=15)
    fecha_lectura = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'pp_fallos_estado_cuenta'

class PpFaltasDiariasDocentes(models.Model):
    codigo_falta = models.CharField(max_length=20)
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    cuenta = models.ForeignKey('PpPlazas', db_column='cuenta')
    codigo_departamento = models.ForeignKey(PpCentrosEducativos, db_column='codigo_departamento')
    codigo_municipio = models.ForeignKey(PpCentrosEducativos, db_column='codigo_municipio')
    codigo_centro = models.ForeignKey(PpCentrosEducativos, db_column='codigo_centro')
    codigo_motivo_falta = models.ForeignKey('PpMotivosFaltas', db_column='codigo_motivo_falta')
    estado_documento = models.ForeignKey(PpEstadosDocumentos, db_column='estado_documento')
    dias_inasistencias = models.SmallIntegerField()
    en_vigencia_falta = models.SmallIntegerField()
    fecha_solicitud_falta = models.DateTimeField(blank=True, null=True)
    monto_documento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    observaciones_falta = models.CharField(max_length=150, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_faltas_diarias_docentes'

class PpFaltasMultas(models.Model):
    cuenta = models.ForeignKey('PpPlazas', db_column='cuenta')
    codigo_multa = models.CharField(max_length=20)
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    codigo_departamento = models.ForeignKey(PpCentrosEducativos, db_column='codigo_departamento')
    codigo_municipio = models.ForeignKey(PpCentrosEducativos, db_column='codigo_municipio')
    codigo_centro = models.ForeignKey(PpCentrosEducativos, db_column='codigo_centro')
    codigo_motivo_falta = models.ForeignKey('PpMotivosFaltas', db_column='codigo_motivo_falta')
    estado_documento = models.ForeignKey(PpEstadosDocumentos, db_column='estado_documento')
    fecha_solicitud_multa = models.DateTimeField()
    porcentaje_multa = models.DecimalField(max_digits=5, decimal_places=2)
    en_vigencia_multa = models.SmallIntegerField()
    observaciones_multa = models.CharField(max_length=250, blank=True)
    monto_documento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_faltas_multas'

class PpFuncionesCalculo(models.Model):
    codigo_funcion = models.IntegerField(unique=True)
    descripcion_funcion = models.CharField(max_length=100, blank=True)
    objetivo_funcion = models.CharField(max_length=250, blank=True)
    numero_parametros = models.SmallIntegerField(blank=True, null=True)
    observaciones_funcion = models.TextField(blank=True)
    tipo_funcion = models.SmallIntegerField(blank=True, null=True)
    invocacion_funcion = models.SmallIntegerField(blank=True, null=True)
    vigente_funcion = models.SmallIntegerField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    funcion_fuente = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_funciones_calculo'

class PpGradosAcademicos(models.Model):
    codigo_grado_academico = models.IntegerField(primary_key=True)
    codigo_estadio = models.ForeignKey(PpEstadiosAcademicos, db_column='codigo_estadio')
    descripcion_grado = models.CharField(max_length=50)
    abreviatura_grado = models.CharField(max_length=15)
    prioridad_grado = models.IntegerField()
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_grados_academicos'

class PpGraduados(models.Model):
    codigo_centro_estudio = models.ForeignKey(PpCentrosEstudios, db_column='codigo_centro_estudio')
    tomo_graduado = models.CharField(max_length=15)
    folio_graduado = models.CharField(max_length=15)
    fecha_graduacion = models.DateTimeField()
    identidad_graduado = models.CharField(max_length=13, blank=True)
    nombre_graduado = models.CharField(max_length=100, blank=True)
    titulo_graduado = models.CharField(max_length=100, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_graduados'

class PpHistoAjustesSueldos(models.Model):
    codigo_periodo = models.CharField(max_length=6, blank=True)
    cuenta = models.CharField(max_length=50, blank=True)
    identidad_empleado = models.CharField(max_length=13, blank=True)
    codigo_transaccion = models.IntegerField()
    secuencial_histo_tran = models.IntegerField()
    codigo_periodo_ajuste = models.CharField(max_length=6, blank=True)
    codigo_transaccion_ajuste = models.IntegerField(blank=True, null=True)
    secuencial_tran_ajuste = models.IntegerField(blank=True, null=True)
    item_matricial_ajuste = models.IntegerField(blank=True, null=True)
    monto_transaccion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    valor_hora = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    no_horas = models.IntegerField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=50, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=50, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    no_dias = models.IntegerField(blank=True, null=True)
    tipo_generacion = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_histo_ajustes_sueldos'

class PpHistoAniosPlazas(models.Model):
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    secuencial = models.IntegerField()
    cuenta = models.CharField(max_length=50, blank=True)
    codigo_cargo = models.ForeignKey(PpCargos, db_column='codigo_cargo', blank=True, null=True)
    codigo_pais = models.ForeignKey('PpPaises', db_column='codigo_pais', blank=True, null=True)
    codigo_departamento = models.ForeignKey(PpCentrosEducativos, db_column='codigo_departamento', blank=True, null=True)
    codigo_municipio = models.ForeignKey(PpCentrosEducativos, db_column='codigo_municipio', blank=True, null=True)
    codigo_centro = models.ForeignKey(PpCentrosEducativos, db_column='codigo_centro', blank=True, null=True)
    codigo_tipo_profesional = models.ForeignKey('PpTipoProfesionales', db_column='codigo_tipo_profesional', blank=True, null=True)
    fecha_inicial = models.DateTimeField(blank=True, null=True)
    fecha_ultimo_calculo = models.DateTimeField()
    horario_plaza = models.SmallIntegerField(blank=True, null=True)
    tipo_plaza = models.SmallIntegerField(blank=True, null=True)
    anios_servicio = models.IntegerField(blank=True, null=True)
    meses_servicio = models.IntegerField(blank=True, null=True)
    dias_servicio = models.IntegerField(blank=True, null=True)
    horas_servicio = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    anios_servicio_originales = models.IntegerField(blank=True, null=True)
    meses_servicio_originales = models.IntegerField(blank=True, null=True)
    dias_servicio_originales = models.IntegerField(blank=True, null=True)
    horas_servicio_originales = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tipo_generacion_calculo = models.SmallIntegerField(blank=True, null=True)
    pagar_anios_servicios = models.SmallIntegerField(blank=True, null=True)
    xnearmensaje = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_histo_anios_plazas'

class PpHistoAprobarDocente(models.Model):
    identidad_empleado = models.CharField(max_length=13)
    usuario_actualizar = models.CharField(max_length=25)
    fecha_actualizar = models.DateTimeField()
    usuario_aprobar = models.CharField(max_length=25)
    observacion = models.CharField(max_length=255)
    item_error = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_histo_aprobar_docente'

class PpHistoControlTransacciones(models.Model):
    codigo_periodo = models.CharField(max_length=6)
    identidad_empleado = models.CharField(max_length=13)
    cuenta = models.CharField(max_length=50)
    codigo_transaccion = models.IntegerField()
    monto_transaccion = models.DecimalField(max_digits=18, decimal_places=2)
    usuario_creacion = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField()
    usuario_autorizo = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'pp_histo_control_transacciones'

class PpHistoCtasBancarias(models.Model):
    identidad = models.CharField(max_length=13)
    cuenta_bancaria = models.CharField(max_length=50)
    codigo_banco = models.IntegerField()
    observacion = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_ingreso_historico = models.DateTimeField()
    usuario_ingreso_historico = models.CharField(max_length=25)
    comentario_adicional = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_histo_ctas_bancarias'

class PpHistoIdentidades(models.Model):
    identidad_empleado = models.CharField(max_length=13)
    identidad_anterior = models.CharField(max_length=13)
    cuenta = models.CharField(max_length=50)
    nombres_id_anterior = models.CharField(max_length=35)
    apellidos_id_anterior = models.CharField(max_length=35)
    periodo_inicial = models.CharField(max_length=6, blank=True)
    periodo_final = models.CharField(max_length=6, blank=True)
    estado_registro = models.SmallIntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    cuenta_reemplazo = models.CharField(max_length=50, blank=True)
    marcador = models.SmallIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_histo_identidades'

class PpHistoMovPlazas(models.Model):
    codigo_movimiento = models.CharField(max_length=30)
    cuenta = models.CharField(max_length=50)
    fecha_movimiento = models.DateTimeField()
    tipo_movimiento = models.IntegerField()
    horas_originales = models.IntegerField()
    horas_despues = models.IntegerField()
    usuario_creacion_mov = models.CharField(max_length=25)
    usuario_modificacion_mov = models.CharField(max_length=25)
    fecha_creacion_mov = models.DateTimeField()
    fecha_modificacion_mov = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'pp_histo_mov_plazas'

class PpHistoMovimientos(models.Model):
    codigo_histo_movimiento = models.DateTimeField(primary_key=True)
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    codigo_movimiento = models.ForeignKey('PpMotivosMovimientos', db_column='codigo_movimiento')
    codigo_motivo = models.ForeignKey('PpMotivosMovimientos', db_column='codigo_motivo')
    codigo_departamento = models.ForeignKey(PpCentrosEducativos, db_column='codigo_departamento', blank=True, null=True)
    codigo_municipio = models.ForeignKey(PpCentrosEducativos, db_column='codigo_municipio', blank=True, null=True)
    codigo_centro = models.ForeignKey(PpCentrosEducativos, db_column='codigo_centro', blank=True, null=True)
    codigo_tipo_profesional = models.ForeignKey('PpTipoProfesionales', db_column='codigo_tipo_profesional', blank=True, null=True)
    fecha_inicial = models.DateTimeField(blank=True, null=True)
    fecha_final = models.DateTimeField(blank=True, null=True)
    plaza_primaria = models.CharField(max_length=50, blank=True)
    e_plaza_primaria_anterior = models.SmallIntegerField(blank=True, null=True)
    e_plaza_secundaria_anterior = models.SmallIntegerField(blank=True, null=True)
    plaza_secundaria = models.CharField(max_length=50, blank=True)
    plaza_actual = models.SmallIntegerField(blank=True, null=True)
    estado_plaza_registro = models.SmallIntegerField(blank=True, null=True)
    fecha_activacion = models.DateTimeField(blank=True, null=True)
    fecha_desactivacion = models.DateTimeField(blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    numero_documento = models.CharField(max_length=20, blank=True)
    tipo_generacion = models.SmallIntegerField(blank=True, null=True)
    anios_servicio = models.SmallIntegerField(blank=True, null=True)
    pagar_plaza_primaria = models.SmallIntegerField(blank=True, null=True)
    licencia_goce = models.SmallIntegerField(blank=True, null=True)
    horas_clase = models.IntegerField(blank=True, null=True)
    e_plaza_primaria_generar = models.SmallIntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    observaciones = models.CharField(max_length=255, blank=True)
    codigo_municipio_anterior = models.CharField(max_length=2, blank=True)
    codigo_centro_anterior = models.CharField(max_length=5, blank=True)
    municipio_depurado = models.CharField(max_length=1, blank=True)
    plaza_primaria_anterior = models.CharField(max_length=50, blank=True)
    plaza_secundaria_anterior = models.CharField(max_length=50, blank=True)
    plaza_primaria_muni_depurado = models.CharField(max_length=1, blank=True)
    plaza_secundaria_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_histo_movimientos'

class PpHistoPlazas(models.Model):
    codigo_histo_plazas = models.DateTimeField(primary_key=True)
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado', blank=True, null=True)
    cuenta = models.ForeignKey('PpPlazas', db_column='cuenta', blank=True, null=True)
    e_general_plaza = models.SmallIntegerField(blank=True, null=True)
    e_particular_plaza = models.SmallIntegerField(blank=True, null=True)
    fecha_inicial = models.DateTimeField(blank=True, null=True)
    fecha_final = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_histo_plazas'

class PpHistoRecalcularDocente(models.Model):
    codigo_periodo = models.CharField(max_length=6)
    identidad_empleado = models.CharField(max_length=13)
    cuenta = models.CharField(max_length=50)
    codigo_transaccion = models.IntegerField()
    monto_transaccion = models.DecimalField(max_digits=18, decimal_places=2)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'pp_histo_recalcular_docente'

class PpHistoSueldosDocentes(models.Model):
    codigo_periodo = models.ForeignKey('PpPeriodos', db_column='codigo_periodo')
    identidad_empleado = models.CharField(max_length=13)
    cuenta = models.ForeignKey(PpCatalogos, db_column='cuenta')
    cuenta_siafi = models.CharField(max_length=50, blank=True)
    pagos = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    deducciones = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    sueldo_neto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descripcion_departamento = models.CharField(max_length=30, blank=True)
    descripcion_municipio = models.CharField(max_length=30, blank=True)
    descripcion_nivel_educativo = models.CharField(max_length=30, blank=True)
    descripcion_centro = models.CharField(max_length=30, blank=True)
    observaciones = models.CharField(max_length=1, blank=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_histo_sueldos_docentes'

class PpHistoTransEliminadas(models.Model):
    codigo_periodo = models.CharField(max_length=6)
    identidad_empleado = models.CharField(max_length=13)
    cuenta = models.CharField(max_length=50)
    codigo_transaccion = models.IntegerField()
    secuencial_histo_trans = models.IntegerField()
    codigo_planilla = models.CharField(max_length=10, blank=True)
    monto_transaccion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    periodo_transaccion = models.CharField(max_length=6, blank=True)
    item_matricial = models.IntegerField(blank=True, null=True)
    estado_transaccion = models.SmallIntegerField(blank=True, null=True)
    fecha_activacion = models.DateTimeField(blank=True, null=True)
    fecha_desactivacion = models.DateTimeField(blank=True, null=True)
    presupuesto_congelado = models.SmallIntegerField(blank=True, null=True)
    monto_sobregiro = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    numero_documento = models.CharField(max_length=20, blank=True)
    estructura_periodo = models.CharField(max_length=50, blank=True)
    tipo_generacion = models.SmallIntegerField(blank=True, null=True)
    aparecio_planilla = models.SmallIntegerField(blank=True, null=True)
    periodo_original = models.CharField(max_length=6, blank=True)
    valor_recuperar = models.SmallIntegerField(blank=True, null=True)
    observacion_tran_periodo = models.CharField(max_length=250, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    usuario_elimino = models.CharField(max_length=25, blank=True)
    fecha_elimino = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_histo_trans_eliminadas'

class PpHistoTransPeriodos(models.Model):
    codigo_periodo = models.CharField(max_length=6)
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    cuenta = models.ForeignKey('PpPlazas', db_column='cuenta')
    codigo_transaccion = models.ForeignKey('PpTransacciones', db_column='codigo_transaccion')
    secuencial_histo_trans = models.IntegerField()
    codigo_planilla = models.CharField(max_length=10, blank=True)
    monto_transaccion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    periodo_transaccion = models.CharField(max_length=6, blank=True)
    item_matricial = models.IntegerField(blank=True, null=True)
    estado_transaccion = models.SmallIntegerField(blank=True, null=True)
    fecha_activacion = models.DateTimeField(blank=True, null=True)
    fecha_desactivacion = models.DateTimeField(blank=True, null=True)
    presupuesto_congelado = models.SmallIntegerField(blank=True, null=True)
    monto_sobregiro = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    numero_documento = models.CharField(max_length=20, blank=True)
    estructura_periodo = models.CharField(max_length=50, blank=True)
    tipo_generacion = models.SmallIntegerField(blank=True, null=True)
    aparecio_planilla = models.SmallIntegerField(blank=True, null=True)
    periodo_original = models.CharField(max_length=6, blank=True)
    valor_recuperar = models.SmallIntegerField(blank=True, null=True)
    observacion_tran_periodo = models.CharField(max_length=250, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_histo_trans_periodos'

class PpHistoricoTitulos(models.Model):
    codigo_titulo = models.ForeignKey('PpTitulos', db_column='codigo_titulo')
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    codigo_centro_estudio = models.ForeignKey(PpCentrosEstudios, db_column='codigo_centro_estudio')
    fecha_graduacion = models.DateTimeField()
    codigo_documento = models.CharField(max_length=25, blank=True)
    numero_folio_titulo = models.CharField(max_length=15, blank=True)
    numero_tomo = models.CharField(max_length=15, blank=True)
    codigo_grado_academico = models.ForeignKey(PpGradosAcademicos, db_column='codigo_grado_academico', blank=True, null=True)
    codigo_tipo_profesional = models.ForeignKey('PpTipoProfesionales', db_column='codigo_tipo_profesional')
    estado_documento = models.ForeignKey(PpEstadosDocumentos, db_column='estado_documento')
    promedio_obtenido = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    tipo_titulo = models.SmallIntegerField(blank=True, null=True)
    titulo_buen_estado = models.CharField(max_length=1, blank=True)
    observaciones_titulo = models.CharField(max_length=255, blank=True)
    usuario_verifico_titulo = models.CharField(max_length=25, blank=True)
    fecha_verifico_titulo = models.DateTimeField(blank=True, null=True)
    usuario_aprobacion_titulo = models.CharField(max_length=25, blank=True)
    fecha_aprobacion_titulo = models.DateTimeField(blank=True, null=True)
    usuario_reversion_titulo = models.CharField(max_length=25, blank=True)
    fecha_reversion_titulo = models.DateTimeField(blank=True, null=True)
    entrego_fotocopia = models.SmallIntegerField(blank=True, null=True)
    xnearmensaje = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    estado_profesionalizacion = models.IntegerField(blank=True, null=True)
    usuario_autorizo = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_historico_titulos'

class PpHistoricoTransPeriodos(models.Model):
    codigo_periodo = models.CharField(max_length=6)
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    cuenta = models.ForeignKey('PpPlazas', db_column='cuenta')
    codigo_transaccion = models.ForeignKey('PpTransacciones', db_column='codigo_transaccion')
    secuencial_histo_trans = models.IntegerField()
    codigo_planilla = models.CharField(max_length=10, blank=True)
    monto_transaccion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    periodo_transaccion = models.CharField(max_length=6, blank=True)
    item_matricial = models.IntegerField(blank=True, null=True)
    estado_transaccion = models.SmallIntegerField(blank=True, null=True)
    fecha_activacion = models.DateTimeField(blank=True, null=True)
    fecha_desactivacion = models.DateTimeField(blank=True, null=True)
    presupuesto_congelado = models.SmallIntegerField(blank=True, null=True)
    monto_sobregiro = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    numero_documento = models.CharField(max_length=20, blank=True)
    estructura_periodo = models.CharField(max_length=50, blank=True)
    tipo_generacion = models.SmallIntegerField(blank=True, null=True)
    aparecio_planilla = models.SmallIntegerField(blank=True, null=True)
    periodo_original = models.CharField(max_length=6, blank=True)
    valor_recuperar = models.SmallIntegerField(blank=True, null=True)
    observacion_tran_periodo = models.CharField(max_length=250, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_historico_trans_periodos'

class PpHorarios(models.Model):
    codigo_horario = models.SmallIntegerField(primary_key=True)
    descripcion_horario = models.CharField(max_length=25)
    hora_inicio = models.DateTimeField()
    hora_final = models.DateTimeField()
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_horarios'

class PpInstitucionMeritos(models.Model):
    cod_institucion_merito = models.IntegerField(primary_key=True)
    descripcion_institucion_merito = models.CharField(max_length=100)
    abreviatura_institucion_merito = models.CharField(max_length=30)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_institucion_meritos'

class PpInstitucionesExternas(models.Model):
    codigo_institucion = models.CharField(primary_key=True, max_length=13)
    nombre_institucion = models.CharField(max_length=100)
    siglas_institucion = models.CharField(max_length=20)
    num_miembros_junta = models.SmallIntegerField(blank=True, null=True)
    tipo_institucion = models.SmallIntegerField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_instituciones_externas'

class PpLimiteDepositos(models.Model):
    anio_deposito = models.CharField(max_length=4, blank=True)
    codigo_planilla = models.CharField(max_length=10, blank=True)
    monto_total_depositos = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    numero_deposito_inf = models.CharField(max_length=6, blank=True)
    numero_deposito_sup = models.CharField(max_length=6, blank=True)
    numero_total_depositos = models.IntegerField(blank=True, null=True)
    tipo_pago_deposito = models.CharField(max_length=2, blank=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_limite_depositos'

class PpLimitesCheques(models.Model):
    codigo_planilla = models.ForeignKey('PpPlanillas', db_column='codigo_planilla', unique=True)
    anio_cheque = models.CharField(max_length=4, blank=True)
    tipo_pago_cheque = models.CharField(max_length=2, blank=True)
    numero_cheque_inf = models.CharField(max_length=6, blank=True)
    numero_cheque_sup = models.CharField(max_length=6, blank=True)
    numero_total_cheques = models.IntegerField(blank=True, null=True)
    monto_total_cheques = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_limites_cheques'

class PpListaGeneralDocentes(models.Model):
    codigo_periodo = models.CharField(max_length=6)
    identidad = models.CharField(max_length=13)
    cuenta = models.CharField(max_length=50)
    codigo_transaccion = models.IntegerField()
    secuencial_histo_trans = models.IntegerField()
    codigo_planilla = models.CharField(max_length=10, blank=True)
    monto_transaccion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    periodo_transaccion = models.CharField(max_length=6, blank=True)
    item_matricial = models.IntegerField(blank=True, null=True)
    estado_transaccion = models.SmallIntegerField(blank=True, null=True)
    fecha_activacion = models.DateTimeField(blank=True, null=True)
    fecha_desactivacion = models.DateTimeField(blank=True, null=True)
    presupuesto_congelado = models.SmallIntegerField(blank=True, null=True)
    monto_sobregiro = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    numero_documento = models.CharField(max_length=20, blank=True)
    estructura_periodo = models.CharField(max_length=50, blank=True)
    tipo_generacion = models.SmallIntegerField(blank=True, null=True)
    aparecio_planilla = models.SmallIntegerField(blank=True, null=True)
    periodo_original = models.CharField(max_length=6, blank=True)
    valor_recuperar = models.SmallIntegerField(blank=True, null=True)
    observacion_tran_periodo = models.CharField(max_length=250, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_lista_general_docentes'

class PpLogrosMeritos(models.Model):
    codigo_logro = models.IntegerField(primary_key=True)
    descripcion_logro = models.CharField(max_length=100)
    abreviatura_logro = models.CharField(max_length=30)
    puntaje_maximo = models.IntegerField(blank=True, null=True)
    vigencia_anos = models.SmallIntegerField(blank=True, null=True)
    unidad_medida = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_logros_meritos'

class PpLsgEstudios(models.Model):
    numero_acuerdo = models.ForeignKey(PpAcuerdos, db_column='numero_acuerdo', unique=True)
    codigo_pais = models.ForeignKey('PpPaises', db_column='codigo_pais')
    codigo_titulo = models.ForeignKey('PpTitulos', db_column='codigo_titulo')
    codigo_centro_estudio = models.ForeignKey(PpCentrosEstudios, db_column='codigo_centro_estudio')
    becado = models.SmallIntegerField(blank=True, null=True)
    duracion_estudios_anos = models.SmallIntegerField(blank=True, null=True)
    duracion_estudios_meses = models.SmallIntegerField(blank=True, null=True)
    numero_clases = models.SmallIntegerField(blank=True, null=True)
    periodos_academicos = models.SmallIntegerField(blank=True, null=True)
    meses_por_periodo = models.SmallIntegerField(blank=True, null=True)
    meses_revision = models.SmallIntegerField(blank=True, null=True)
    meses_maximo_revision = models.SmallIntegerField(blank=True, null=True)
    clases_licencia_anterior = models.SmallIntegerField(blank=True, null=True)
    proxima_fecha_revision = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_lsg_estudios'

class PpMatrizTransacciones(models.Model):
    codigo_transaccion = models.ForeignKey('PpTransacciones', db_column='codigo_transaccion')
    item_matricial = models.IntegerField()
    descripcion_item = models.CharField(max_length=50, blank=True)
    codigo_nivel = models.IntegerField(blank=True, null=True)
    codigo_cargo = models.CharField(max_length=15, blank=True)
    codigo_tipo_profesional = models.CharField(max_length=3, blank=True)
    codigo_grado_academico = models.IntegerField(blank=True, null=True)
    codigo_departameto = models.CharField(max_length=2, blank=True)
    codigo_municipio = models.CharField(max_length=2, blank=True)
    codigo_centro = models.CharField(max_length=5, blank=True)
    clase_centro = models.IntegerField(blank=True, null=True)
    codigo_tipo_centro = models.IntegerField(blank=True, null=True)
    ubicacion_centro = models.CharField(max_length=2, blank=True)
    codigo_titulo = models.IntegerField(blank=True, null=True)
    valor_inicial = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    simbolo_control = models.CharField(max_length=2, blank=True)
    valor_final = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    valor_aplicado = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    docente_profesionalizacion = models.SmallIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_matriz_transacciones'

class PpMayorTmp(models.Model):
    corrent = models.CharField(max_length=2, blank=True)
    programa = models.CharField(max_length=2, blank=True)
    sub_programa = models.CharField(max_length=2, blank=True)
    proyecto = models.CharField(max_length=2, blank=True)
    act_obra = models.CharField(max_length=2, blank=True)
    partida = models.CharField(max_length=3, blank=True)
    codigo_fuente = models.CharField(max_length=2, blank=True)
    organirmo_financ = models.CharField(max_length=3, blank=True)
    codigo_beneficiario = models.CharField(max_length=4, blank=True)
    original_e = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    original_d = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    modif_aumento_e = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    modif_aumento_d = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    modif_mas_e = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    modif_mas_d = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    modif_menos_e = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    modif_menos_d = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    modificado_e = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    modificado_d = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    congelamientos_e = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    congelamientos_d = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    pagos_e = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    pagos_d = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    disponible_e = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    disponible_d = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_mayor_tmp'

class PpMensajes(models.Model):
    codigo_mensajes = models.IntegerField(unique=True)
    texto = models.TextField(blank=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_mensajes'

class PpMeses(models.Model):
    codigo_mes = models.SmallIntegerField(primary_key=True)
    descripcion_mes = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_meses'

class PpMiembrosColegios(models.Model):
    codigo_institucion = models.ForeignKey(PpInstitucionesExternas, db_column='codigo_institucion')
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_miembros_colegios'

class PpModalidades(models.Model):
    codigo_modalidad = models.IntegerField(primary_key=True)
    nombre_modalidad = models.CharField(max_length=50)
    abreviatura_modalidad = models.CharField(max_length=15, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25)
    class Meta:
        managed = False
        db_table = 'pp_modalidades'

class PpMonitoreo(models.Model):
    usuario = models.CharField(max_length=20)
    fecha_acceso = models.DateTimeField()
    codigo_tipo = models.CharField(max_length=20)
    codigo_subtipo = models.CharField(max_length=22)
    hora_inicio = models.DateTimeField()
    hora_final = models.DateTimeField(blank=True, null=True)
    nombre_objeto = models.CharField(max_length=40)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=20, blank=True)
    hora = models.CharField(max_length=2)
    minutos = models.CharField(max_length=2)
    segundos = models.CharField(max_length=2)
    m_segundos = models.IntegerField(blank=True, null=True)
    host_name = models.CharField(max_length=20, blank=True)
    usuario_win = models.CharField(max_length=20, blank=True)
    descripcion = models.CharField(max_length=40, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_monitoreo'

class PpMotivosFaltas(models.Model):
    codigo_motivo_falta = models.IntegerField(primary_key=True)
    descripcion_inasitencia = models.CharField(max_length=100)
    tipo_falta = models.SmallIntegerField(blank=True, null=True)
    falta_inasistencia = models.SmallIntegerField()
    abreviatura_falta = models.CharField(max_length=40)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_motivos_faltas'

class PpMotivosMovimientos(models.Model):
    codigo_movimiento = models.ForeignKey('PpTiposMovimientos', db_column='codigo_movimiento')
    codigo_motivo = models.IntegerField()
    descripcion_motivo_mov = models.CharField(max_length=100)
    abreviatura_motivo_mov = models.CharField(max_length=10)
    descripcion_corta_motivo = models.CharField(max_length=25)
    interpretacion = models.CharField(max_length=255)
    movimiento_permanente = models.SmallIntegerField(blank=True, null=True)
    movimiento_general = models.SmallIntegerField(blank=True, null=True)
    movimiento_automatico = models.SmallIntegerField(blank=True, null=True)
    movimiento_acuerdo = models.SmallIntegerField(blank=True, null=True)
    plaza_actual = models.SmallIntegerField(blank=True, null=True)
    propietario_plaza = models.SmallIntegerField(blank=True, null=True)
    e_plaza_primaria_req = models.SmallIntegerField(blank=True, null=True)
    e_plaza_secundaria_req = models.SmallIntegerField(blank=True, null=True)
    inactivar_padre = models.SmallIntegerField(blank=True, null=True)
    movimiento_padre = models.IntegerField(blank=True, null=True)
    motivo_padre = models.IntegerField(blank=True, null=True)
    mov_generado_caducar = models.IntegerField(blank=True, null=True)
    motivo_generado_caducar = models.IntegerField(blank=True, null=True)
    e_plaza_primaria_habilitar = models.SmallIntegerField(blank=True, null=True)
    e_generado_habilitar_histo = models.SmallIntegerField(blank=True, null=True)
    e_plaza_primaria_generar = models.SmallIntegerField(blank=True, null=True)
    e_plaza_secundaria_generar = models.SmallIntegerField(blank=True, null=True)
    e_docente_generar = models.SmallIntegerField(blank=True, null=True)
    e_docente_habilitar_gen = models.SmallIntegerField(blank=True, null=True)
    pagar_plaza_primaria = models.SmallIntegerField(blank=True, null=True)
    pagar_plaza_secundaria = models.SmallIntegerField(blank=True, null=True)
    licencia_goce = models.SmallIntegerField(blank=True, null=True)
    estructura_financia_mov = models.CharField(max_length=50, blank=True)
    tipo_enlace = models.SmallIntegerField(blank=True, null=True)
    anios_servicio = models.SmallIntegerField(blank=True, null=True)
    movimiento_seleccion = models.SmallIntegerField(blank=True, null=True)
    validar_jornadas = models.SmallIntegerField(blank=True, null=True)
    solicita_identidad_alterna = models.SmallIntegerField(blank=True, null=True)
    verifica_existencia_plaza = models.SmallIntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_motivos_movimientos'

class PpMotivosRechazos(models.Model):
    codigo_razon = models.IntegerField(primary_key=True)
    descripcion_razon = models.CharField(max_length=100)
    abreviatura_razon = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_motivos_rechazos'

class PpMotivosReintegro(models.Model):
    codigo_motivo = models.IntegerField(primary_key=True)
    descripcion_motivo = models.CharField(max_length=50)
    estado_motivo = models.IntegerField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_motivos_reintegro'

class PpMotivosTraslados(models.Model):
    codigo_motivo_traslado = models.IntegerField(primary_key=True)
    descripcion_motivo_traslado = models.CharField(max_length=80)
    prioridad_motivo_traslado = models.IntegerField()
    prioriza_tiempo_servicio = models.SmallIntegerField()
    permite_varios_nombramientos = models.SmallIntegerField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_motivos_traslados'

class PpMovimientosPresupuestarios(models.Model):
    codigo_mov_presupuestario = models.SmallIntegerField(primary_key=True)
    descripcion_movimiento = models.CharField(max_length=50)
    abreviatura_movimiento = models.CharField(max_length=15)
    clase_modificacion = models.SmallIntegerField()
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_movimientos_presupuestarios'

class PpMunicipios(models.Model):
    codigo_departamento = models.ForeignKey(PpDepartamentos, db_column='codigo_departamento')
    codigo_municipio = models.CharField(max_length=2)
    descripcion_municipio = models.CharField(max_length=25)
    abreviatura_municipio = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    municipio_depurado = models.CharField(max_length=1, blank=True)
    municipio_cancelado = models.CharField(max_length=1, blank=True)
    codigo_municipio_anterior = models.CharField(max_length=2, blank=True)
    codigo_departamento_anterior = models.CharField(max_length=2, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_municipios'

class PpNivelesCatalogos(models.Model):
    codigo_nivel_catalogo = models.SmallIntegerField(primary_key=True)
    descripcion_nivel_catalogo = models.CharField(max_length=25, blank=True)
    tamanio = models.SmallIntegerField(blank=True, null=True)
    inicio_nivel = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_niveles_catalogos'

class PpNivelesCatalogosNuevos(models.Model):
    codigo_nivel_catalogo = models.SmallIntegerField(primary_key=True)
    descripcion_nivel_catalogo = models.CharField(max_length=25, blank=True)
    tamanio = models.SmallIntegerField(blank=True, null=True)
    inicio_nivel = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_niveles_catalogos_nuevos'

class PpNivelesCentro(models.Model):
    codigo_departamento = models.ForeignKey(PpCentrosEducativos, db_column='codigo_departamento')
    codigo_municipio = models.ForeignKey(PpCentrosEducativos, db_column='codigo_municipio')
    codigo_centro = models.ForeignKey(PpCentrosEducativos, db_column='codigo_centro')
    codigo_nivel_educativo = models.ForeignKey('PpNivelesEducativos', db_column='codigo_nivel_educativo')
    codigo_centro_anterior = models.CharField(max_length=5, blank=True)
    codigo_municipio_anterior = models.CharField(max_length=2, blank=True)
    municipio_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_niveles_centro'

class PpNivelesEducativos(models.Model):
    codigo_nivel_educativo = models.IntegerField(primary_key=True)
    codigo_unidad = models.ForeignKey('PpUnidadOrganizacionales', db_column='codigo_unidad', blank=True, null=True)
    abreviatura_nivel_educativo = models.CharField(max_length=15)
    descripcion_nivel_educativo = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    prioridad_nivel_educativo = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_niveles_educativos'

class PpObjetosGastos(models.Model):
    codigo_objeto = models.IntegerField(primary_key=True)
    descripcion_objeto = models.CharField(max_length=25)
    abreviatura_objeto = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_objetos_gastos'

class PpObservacionesBancos(models.Model):
    observacion_banco = models.CharField(max_length=60)
    observacion_equivalente = models.CharField(max_length=60)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'pp_observaciones_bancos'

class PpOpcionesReclamoPago(models.Model):
    opcion = models.CharField(primary_key=True, max_length=1)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_opciones_reclamo_pago'

class PpOrganismosFinanciadores(models.Model):
    codigo_organismo = models.IntegerField(primary_key=True)
    descripcion_organismo = models.CharField(max_length=50)
    abreviatura_organismo = models.CharField(max_length=15, blank=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_organismos_financiadores'

class PpPaises(models.Model):
    codigo_pais = models.IntegerField(primary_key=True)
    nombre_pais = models.CharField(max_length=30)
    tiene_corresponsabilidad = models.SmallIntegerField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_paises'

class PpParametrosCargo(models.Model):
    secuencial = models.IntegerField(db_column='Secuencial', blank=True, null=True) # Field name made lowercase.
    fecha_activacion = models.DateTimeField(db_column='Fecha_activacion', blank=True, null=True) # Field name made lowercase.
    usuario_activacion = models.CharField(max_length=25, blank=True)
    fecha_desactivacion = models.DateTimeField(blank=True, null=True)
    usuario_desactivacion = models.CharField(max_length=25, blank=True)
    codigo_transaccion = models.IntegerField(blank=True, null=True)
    codigo_planta = models.CharField(max_length=2, blank=True)
    codigo_tipo_cargo = models.CharField(max_length=2, blank=True)
    codigo_cargo_generico = models.CharField(max_length=2, blank=True)
    codigo_unidad = models.CharField(max_length=1, blank=True)
    codigo_clase = models.CharField(max_length=2, blank=True)
    aplicar_251 = models.IntegerField(blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_fijo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    codigo_tipo_profesional = models.CharField(max_length=3, blank=True)
    aplicar_monto_fijo = models.IntegerField(blank=True, null=True)
    aplicar_porcentaje = models.IntegerField(blank=True, null=True)
    aplicar_a_calificacion = models.IntegerField(blank=True, null=True)
    codigo_tipo_centro = models.IntegerField(blank=True, null=True)
    eliminar_sb = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_parametros_cargo'

class PpParametrosCargo2006(models.Model):
    secuencial = models.IntegerField(db_column='Secuencial', blank=True, null=True) # Field name made lowercase.
    fecha_activacion = models.DateTimeField(db_column='Fecha_activacion', blank=True, null=True) # Field name made lowercase.
    usuario_activacion = models.CharField(max_length=25, blank=True)
    fecha_desactivacion = models.DateTimeField(blank=True, null=True)
    usuario_desactivacion = models.CharField(max_length=25, blank=True)
    codigo_transaccion = models.IntegerField(blank=True, null=True)
    codigo_planta = models.CharField(max_length=2, blank=True)
    codigo_tipo_cargo = models.CharField(max_length=2, blank=True)
    codigo_cargo_generico = models.CharField(max_length=2, blank=True)
    codigo_unidad = models.CharField(max_length=1, blank=True)
    codigo_clase = models.CharField(max_length=2, blank=True)
    aplicar_251 = models.IntegerField(blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_fijo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    codigo_tipo_profesional = models.CharField(max_length=3, blank=True)
    aplicar_monto_fijo = models.IntegerField(blank=True, null=True)
    aplicar_porcentaje = models.IntegerField(blank=True, null=True)
    aplicar_a_calificacion = models.IntegerField(blank=True, null=True)
    codigo_tipo_centro = models.IntegerField(blank=True, null=True)
    eliminar_sb = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_parametros_cargo_2006'

class PpParametrosGenerales(models.Model):
    periodo_anual = models.IntegerField(primary_key=True)
    codigo_nivel_educativo = models.IntegerField(blank=True, null=True)
    fecha_inicial_vigencia = models.DateTimeField()
    fecha_final_vigencia = models.DateTimeField()
    valor_hora_clase = models.DecimalField(max_digits=18, decimal_places=2)
    valor_hora_referencial = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    sueldo_base = models.DecimalField(max_digits=18, decimal_places=2)
    sueldo_base_referencial = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    horas_clase_mensuales = models.IntegerField()
    horas_clase_semanales = models.IntegerField()
    horas_clase_semanales_noc = models.IntegerField(blank=True, null=True)
    horas_clase_mensuales_noc = models.IntegerField(blank=True, null=True)
    sueldo_base_noc = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    edad_jubilacion_voluntaria = models.SmallIntegerField()
    edad_jubilacion_obligatoria1 = models.SmallIntegerField()
    edad_jubilacion_obligatoria2 = models.SmallIntegerField()
    codigo_meritos_eventos = models.IntegerField(blank=True, null=True)
    fecha_realizacion_meritos = models.DateTimeField(blank=True, null=True)
    porcentaje_deduccion = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    limite_superior_pagado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    limite_inferior_pagado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    lcg_estudio_promedio = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    dia_cierre_planilla = models.SmallIntegerField(blank=True, null=True)
    dia_cobertura_inicial = models.SmallIntegerField(blank=True, null=True)
    dia_cobertura_final = models.SmallIntegerField(blank=True, null=True)
    codigo_titulo_notitulado = models.IntegerField(blank=True, null=True)
    centro_estudios_notitulado = models.SmallIntegerField(blank=True, null=True)
    tasa_reparo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    porcentaje_inprema_patronal = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fecha_fin_peticion = models.DateTimeField(blank=True, null=True)
    porcentaje_inprema_docente = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tiempo_proporcional_anios = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    numero_negativas_seleccion = models.SmallIntegerField(blank=True, null=True)
    semanas_base_creacion_plazas = models.SmallIntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    codigo_periodo_dss = models.CharField(max_length=6, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_parametros_generales'

class PpParientes(models.Model):
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    identidad_pariente = models.CharField(max_length=13)
    nombres_pariente = models.CharField(max_length=30)
    apellidos_pariente = models.CharField(max_length=30)
    tipo_pariente = models.CharField(max_length=1, blank=True)
    fecha_nacimiento_pariente = models.DateTimeField()
    sexo_pariente = models.CharField(max_length=1, blank=True)
    observaciones_pariente = models.CharField(max_length=100, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_parientes'

class PpParticipantesComisiones(models.Model):
    identidad_comision = models.CharField(unique=True, max_length=13)
    nombres_comision = models.CharField(max_length=35)
    apellidos_comision = models.CharField(max_length=35)
    fecha_nacimiento = models.DateTimeField(blank=True, null=True)
    grado_academico = models.SmallIntegerField(blank=True, null=True)
    titulo1 = models.CharField(max_length=100, blank=True)
    titulo2 = models.CharField(max_length=100, blank=True)
    titulo3 = models.CharField(max_length=100, blank=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_participantes_comisiones'

class PpParticipantesCursos(models.Model):
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    codigo_capacitacion = models.ForeignKey(PpCursosCapacitaciones, db_column='codigo_capacitacion')
    codigo_curso = models.ForeignKey(PpCursosCapacitaciones, db_column='codigo_curso')
    calificacion_curso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    asignacion_meritos = models.SmallIntegerField()
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_participantes_cursos'

class PpPeriodos(models.Model):
    codigo_periodo = models.CharField(unique=True, max_length=6)
    codigo_mes = models.IntegerField()
    descripcion_periodo = models.CharField(max_length=50)
    fecha_inicial_cobertura = models.DateTimeField()
    fecha_final_cobertura = models.DateTimeField()
    fecha_cierre_periodo = models.DateTimeField(blank=True, null=True)
    estado_periodo = models.SmallIntegerField()
    periodo_actual_abierto = models.SmallIntegerField(blank=True, null=True)
    tipo_periodo = models.SmallIntegerField(blank=True, null=True)
    fecha_bloqueo = models.DateTimeField(blank=True, null=True)
    fecha_apertura = models.DateTimeField(blank=True, null=True)
    fecha_cierre = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    vigente = models.CharField(max_length=1, blank=True)
    codigo_etapa = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_periodos'

class PpPermisos(models.Model):
    usuario = models.CharField(max_length=25)
    codigo_subtipo = models.CharField(max_length=50)
    permiso_agregar = models.CharField(max_length=1)
    permiso_modificar = models.CharField(max_length=1)
    permiso_eliminar = models.CharField(max_length=1)
    permiso_imprimir = models.CharField(max_length=1)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    vigente = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_permisos'

class PpPermisosDocentes(models.Model):
    codigo_solicita_permiso = models.CharField(unique=True, max_length=20)
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    codigo_permiso = models.ForeignKey(PpCausasPermisos, db_column='codigo_permiso', blank=True, null=True)
    cuenta = models.ForeignKey('PpPlazas', db_column='cuenta')
    fecha_ini_permiso = models.DateTimeField()
    fecha_fin_permiso = models.DateTimeField()
    dias_permiso = models.IntegerField()
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_permisos_docentes'

class PpPermisosInscripDocente(models.Model):
    identificador = models.IntegerField()
    usuario = models.CharField(max_length=25)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    supervisor = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_permisos_inscrip_docente'

class PpPermisosProcesos(models.Model):
    identificador = models.IntegerField()
    usuario = models.CharField(max_length=25)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    supervisor = models.IntegerField(blank=True, null=True)
    proceso = models.ForeignKey('PpProcesos', db_column='proceso')
    class Meta:
        managed = False
        db_table = 'pp_permisos_procesos'

class PpPermisosVisualizador(models.Model):
    identificador = models.IntegerField()
    usuario = models.CharField(max_length=25)
    sueldo_bruto_promedio = models.IntegerField(blank=True, null=True)
    dias_laborados = models.IntegerField(blank=True, null=True)
    plaza_complementaria = models.IntegerField(blank=True, null=True)
    planillas_identidad = models.IntegerField(blank=True, null=True)
    datos_generales = models.IntegerField(blank=True, null=True)
    historial_movimiento = models.IntegerField(blank=True, null=True)
    transacciones_actuales = models.IntegerField(blank=True, null=True)
    calculadora = models.IntegerField(blank=True, null=True)
    historial_transacciones = models.IntegerField(blank=True, null=True)
    modificar_transacciones = models.IntegerField(blank=True, null=True)
    imagenes = models.IntegerField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    administrador = models.IntegerField(blank=True, null=True)
    ajuste = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_permisos_visualizador'

class PpPetTransadmon(models.Model):
    anio_peticion = models.IntegerField()
    secuencial_peticion = models.IntegerField()
    codigo_departamento = models.CharField(max_length=2)
    codigo_municipio = models.SmallIntegerField()
    codigo_centro = models.CharField(max_length=5)
    codigo_nivel_educativo = models.IntegerField()
    codigo_transaccion = models.ForeignKey('PpTransacciones', db_column='codigo_transaccion')
    proyectado_plazas = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    proyectado_horas = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_pet_transadmon'

class PpPeticionesAdicionales(models.Model):
    codigo_peticion = models.CharField(primary_key=True, max_length=20)
    codigo_departamento = models.ForeignKey(PpCentrosEducativos, db_column='codigo_departamento', blank=True, null=True)
    codigo_municipio = models.ForeignKey(PpCentrosEducativos, db_column='codigo_municipio', blank=True, null=True)
    codigo_centro = models.ForeignKey(PpCentrosEducativos, db_column='codigo_centro', blank=True, null=True)
    codigo_nivel_educativo = models.ForeignKey(PpNivelesEducativos, db_column='codigo_nivel_educativo', blank=True, null=True)
    estado_documento = models.ForeignKey(PpEstadosDocumentos, db_column='estado_documento')
    fecha_solicitud = models.DateTimeField(blank=True, null=True)
    observaciones_peticion = models.CharField(max_length=50, blank=True)
    anio_peticion = models.IntegerField(blank=True, null=True)
    secuencial_peticion = models.IntegerField(blank=True, null=True)
    consolidada = models.SmallIntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_peticiones_adicionales'

class PpPeticionesCentro(models.Model):
    anio_peticion = models.IntegerField()
    secuencial_peticion = models.IntegerField()
    codigo_departamento = models.ForeignKey(PpCentrosEducativos, db_column='codigo_departamento')
    codigo_municipio = models.ForeignKey(PpCentrosEducativos, db_column='codigo_municipio')
    codigo_centro = models.ForeignKey(PpCentrosEducativos, db_column='codigo_centro')
    codigo_nivel_educativo = models.ForeignKey(PpNivelesEducativos, db_column='codigo_nivel_educativo')
    total_plazas = models.IntegerField(blank=True, null=True)
    total_horas = models.IntegerField(blank=True, null=True)
    presupuesto_plazas = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_horas = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_proyectado_plazas = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_proyectado_horas = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_peticiones_centro'

class PpPeticionesTransaccion(models.Model):
    anio_peticion = models.ForeignKey(PpPeticionesCentro, db_column='anio_peticion')
    secuencial_peticion = models.ForeignKey(PpPeticionesCentro, db_column='secuencial_peticion')
    codigo_departamento = models.ForeignKey(PpPeticionesCentro, db_column='codigo_departamento')
    codigo_municipio = models.ForeignKey(PpPeticionesCentro, db_column='codigo_municipio')
    codigo_centro = models.ForeignKey(PpPeticionesCentro, db_column='codigo_centro')
    codigo_nivel_educativo = models.ForeignKey(PpPeticionesCentro, db_column='codigo_nivel_educativo')
    codigo_transaccion = models.ForeignKey('PpTransacciones', db_column='codigo_transaccion')
    proyectado_plazas = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    proyectado_horas = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_peticiones_transaccion'

class PpPlanillas(models.Model):
    codigo_planilla = models.CharField(primary_key=True, max_length=10)
    codigo_configuracion = models.ForeignKey(PpConfiguraciones, db_column='codigo_configuracion')
    codigo_periodo = models.ForeignKey(PpPeriodos, db_column='codigo_periodo')
    orden_pago = models.CharField(max_length=10, blank=True)
    codigo_depto_cheque = models.CharField(max_length=2, blank=True)
    codigo_muni_cheque = models.CharField(max_length=3, blank=True)
    codigo_centro_cheque = models.CharField(max_length=5, blank=True)
    descripcion_banco = models.CharField(max_length=50, blank=True)
    descripcion_depto_cheque = models.CharField(max_length=25, blank=True)
    descripcion_muni_cheque = models.CharField(max_length=25, blank=True)
    descripcion_centro_cheque = models.CharField(max_length=120, blank=True)
    fecha_generacion_planilla = models.DateTimeField(blank=True, null=True)
    fecha_emision_planilla = models.DateTimeField(blank=True, null=True)
    numero_impresiones = models.IntegerField(blank=True, null=True)
    numero_docentes = models.IntegerField(blank=True, null=True)
    forma_pago_plan = models.SmallIntegerField(blank=True, null=True)
    codigo_banco_deposito = models.IntegerField(blank=True, null=True)
    monto_pagos = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_deducciones = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_sobregiro = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    estado_planilla = models.SmallIntegerField()
    estado_general = models.SmallIntegerField()
    estado_confirma_ejecucion = models.SmallIntegerField(blank=True, null=True)
    fecha_confirma_ejecucion = models.DateTimeField(blank=True, null=True)
    fecha_estado_planilla = models.DateTimeField(blank=True, null=True)
    fecha_estado_general = models.DateTimeField(blank=True, null=True)
    fecha_ultima_impresion = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    codigo_depto_deposito = models.CharField(max_length=2, blank=True)
    desc_depto_deposito = models.CharField(max_length=50, blank=True)
    forma_pago_siafi_o_sip = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'pp_planillas'

class PpPlantas(models.Model):
    codigo_planta = models.CharField(primary_key=True, max_length=2)
    descripcion_planta = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_plantas'

class PpPlazas(models.Model):
    cuenta = models.ForeignKey(PpCatalogos, db_column='cuenta', primary_key=True)
    codigo_cargo = models.ForeignKey(PpCargos, db_column='codigo_cargo', blank=True, null=True)
    codigo_modalidad = models.ForeignKey(PpModalidades, db_column='codigo_modalidad', blank=True, null=True)
    horas_plaza = models.IntegerField(blank=True, null=True)
    horas_coprogramaticas = models.IntegerField(blank=True, null=True)
    estado_plaza = models.ForeignKey(PpEstadosPlazas, db_column='estado_plaza')
    tipo_plaza = models.SmallIntegerField()
    horario_plaza = models.SmallIntegerField()
    documento_respaldo = models.CharField(max_length=50, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    usuario_modif_horas = models.CharField(max_length=25, blank=True)
    fecha_modif_horas = models.DateTimeField(blank=True, null=True)
    usuario_modif_copro = models.CharField(max_length=25, blank=True)
    fecha_modif_copro = models.DateTimeField(blank=True, null=True)
    usuario_modif_horario = models.CharField(max_length=25, blank=True)
    fecha_modif_horario = models.DateTimeField(blank=True, null=True)
    usuario_modif_modalidad = models.CharField(max_length=25, blank=True)
    fecha_modif_modalidad = models.DateTimeField(blank=True, null=True)
    usuario_modif_estado = models.CharField(max_length=25, blank=True)
    fecha_modif_estado = models.DateTimeField(blank=True, null=True)
    usuario_modif_cargo = models.CharField(max_length=25, blank=True)
    fecha_modif_cargo = models.DateTimeField(blank=True, null=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_plazas'

class PpPlazasAnexoAdmon2005(models.Model):
    institucion = models.CharField(max_length=2, blank=True)
    programa = models.CharField(max_length=2, blank=True)
    subprograma = models.CharField(max_length=2, blank=True)
    proyecto = models.CharField(max_length=2, blank=True)
    actividad = models.CharField(max_length=2, blank=True)
    area = models.CharField(max_length=2, blank=True)
    seccion = models.CharField(max_length=3, blank=True)
    clave = models.CharField(max_length=5, blank=True)
    clase = models.CharField(max_length=6, blank=True)
    sclase = models.CharField(max_length=3, blank=True)
    escala = models.CharField(max_length=2, blank=True)
    paso = models.CharField(max_length=2, blank=True)
    plaza = models.CharField(max_length=45, blank=True)
    sueldo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    programado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    n_sueldo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    n_programado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_plazas_anexo_admon_2005'

class PpPlazasAsignadas(models.Model):
    codigo_departamento = models.ForeignKey(PpCentrosEducativos, db_column='codigo_departamento')
    codigo_municipio = models.ForeignKey(PpCentrosEducativos, db_column='codigo_municipio')
    codigo_centro = models.ForeignKey(PpCentrosEducativos, db_column='codigo_centro')
    codigo_nivel_educativo = models.ForeignKey(PpNivelesEducativos, db_column='codigo_nivel_educativo')
    numero_plaza = models.IntegerField()
    estado_documento = models.ForeignKey(PpEstadosDocumentos, db_column='estado_documento', blank=True, null=True)
    codigo_cargo = models.CharField(max_length=15, blank=True)
    codigo_modalidad = models.ForeignKey(PpModalidades, db_column='codigo_modalidad', blank=True, null=True)
    codigo_presupuesto = models.ForeignKey(PpEncPresupuestoNuevo, db_column='codigo_presupuesto')
    horas_plaza = models.SmallIntegerField(blank=True, null=True)
    tipo_plaza = models.SmallIntegerField()
    horario_plaza = models.SmallIntegerField()
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    plaza_creada = models.CharField(max_length=50, blank=True)
    objetos_gasto = models.CharField(max_length=50, blank=True)
    codigo_municipio_anterior = models.CharField(max_length=2, blank=True)
    codigo_centro_anterior = models.CharField(max_length=5, blank=True)
    municipio_depurado = models.CharField(max_length=1, blank=True)
    plaza_creada_anterior = models.CharField(max_length=50, blank=True)
    plaza_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_plazas_asignadas'

class PpPlazasCentralDeptal(models.Model):
    cuenta = models.CharField(primary_key=True, max_length=50)
    codigo_cargo = models.CharField(max_length=15, blank=True)
    codigo_modalidad = models.IntegerField(blank=True, null=True)
    horas_plaza = models.IntegerField(blank=True, null=True)
    horas_coprogramaticas = models.IntegerField(blank=True, null=True)
    estado_plaza = models.SmallIntegerField()
    tipo_plaza = models.SmallIntegerField()
    horario_plaza = models.SmallIntegerField()
    documento_respaldo = models.CharField(max_length=50, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    usuario_modif_horas = models.CharField(max_length=25, blank=True)
    fecha_modif_horas = models.DateTimeField(blank=True, null=True)
    usuario_modif_copro = models.CharField(max_length=25, blank=True)
    fecha_modif_copro = models.DateTimeField(blank=True, null=True)
    usuario_modif_horario = models.CharField(max_length=25, blank=True)
    fecha_modif_horario = models.DateTimeField(blank=True, null=True)
    usuario_modif_modalidad = models.CharField(max_length=25, blank=True)
    fecha_modif_modalidad = models.DateTimeField(blank=True, null=True)
    usuario_modif_estado = models.CharField(max_length=25, blank=True)
    fecha_modif_estado = models.DateTimeField(blank=True, null=True)
    usuario_modif_cargo = models.CharField(max_length=25, blank=True)
    fecha_modif_cargo = models.DateTimeField(blank=True, null=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_plazas_central_deptal'

class PpPlazasDocenteAcuerdo(models.Model):
    numero_acuerdo = models.CharField(max_length=20)
    codigo_departamento = models.CharField(max_length=2)
    codigo_municipio = models.CharField(max_length=2)
    codigo_centro = models.CharField(max_length=5)
    descripcion_departamento = models.CharField(max_length=25, blank=True)
    descripcion_municipio = models.CharField(max_length=25, blank=True)
    descripcion_centro = models.CharField(max_length=120, blank=True)
    numero_plaza = models.CharField(max_length=6)
    codigo_cargo = models.CharField(max_length=15, blank=True)
    descripcion_cargo = models.CharField(max_length=100, blank=True)
    descripcion_motivo = models.CharField(max_length=100, blank=True)
    horas_plaza = models.IntegerField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    codigo_municipio_anterior = models.CharField(max_length=2, blank=True)
    codigo_centro_anterior = models.CharField(max_length=5, blank=True)
    municipio_depurado = models.CharField(max_length=1, blank=True)
    numero_plaza_anterior = models.CharField(max_length=6, blank=True)
    numero_plaza_depurada = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_plazas_docente_acuerdo'

class PpPlazasEmpleados(models.Model):
    codigo_movimiento = models.ForeignKey(PpMotivosMovimientos, db_column='codigo_movimiento')
    codigo_motivo = models.ForeignKey(PpMotivosMovimientos, db_column='codigo_motivo')
    cuenta = models.ForeignKey(PpPlazas, db_column='cuenta')
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    numero_documento = models.CharField(max_length=20, blank=True)
    fecha_posesion = models.DateTimeField(blank=True, null=True)
    prioridad_plaza = models.SmallIntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_plazas_empleados'

class PpPlazasTemporales(models.Model):
    codigo_mov_plaza = models.CharField(max_length=20, blank=True)
    codigo_presupuesto = models.IntegerField(blank=True, null=True)
    numero_plaza_temporal = models.IntegerField()
    cuenta = models.CharField(max_length=50)
    codigo_cargo = models.CharField(max_length=15, blank=True)
    estado = models.SmallIntegerField()
    codigo_modalidad = models.IntegerField(blank=True, null=True)
    horas_plaza = models.SmallIntegerField(blank=True, null=True)
    tipo_plaza = models.SmallIntegerField()
    horario_plaza = models.SmallIntegerField()
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_plazas_temporales'

class PpPlazasTmp(models.Model):
    codigo_nivel = models.CharField(max_length=4, blank=True)
    codigo_departamento = models.CharField(max_length=2, blank=True)
    codigo_municipio = models.CharField(max_length=2, blank=True)
    codigo_centro = models.CharField(max_length=5, blank=True)
    codigo_municipio_anterior = models.CharField(max_length=2, blank=True)
    codigo_centro_anterior = models.CharField(max_length=5, blank=True)
    municipio_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_plazas_tmp'

class PpPorcentajesAjuste251(models.Model):
    anio = models.CharField(primary_key=True, max_length=4)
    porcentaje = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_porcentajes_ajuste_251'

class PpPresupuestoAnexo(models.Model):
    codigo_anio = models.CharField(max_length=4)
    cuenta = models.CharField(max_length=50)
    presupuesto_mensual = models.DecimalField(max_digits=18, decimal_places=2)
    presupuesto_anual = models.DecimalField(max_digits=18, decimal_places=2)
    presupuesto_aguinaldo = models.DecimalField(max_digits=18, decimal_places=2)
    presupuesto_catorceavo = models.DecimalField(max_digits=18, decimal_places=2)
    presupuesto_vacaciones = models.DecimalField(max_digits=18, decimal_places=2)
    comprometido_anual = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comprometido_aguinaldo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comprometido_catorceavo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comprometido_vacaciones = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    ejecutado_anual = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    ejecutado_aguinaldo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    ejecutado_catorceavo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    ejecutado_vacaciones = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    hora_clase_sueldo_base = models.DecimalField(max_digits=18, decimal_places=2)
    antiguedad_servicio = models.DecimalField(max_digits=18, decimal_places=2)
    meritos_profesionales = models.DecimalField(max_digits=18, decimal_places=2)
    zona_trabajo = models.DecimalField(max_digits=18, decimal_places=2)
    cargo_directivo = models.DecimalField(max_digits=18, decimal_places=2)
    calificacion_academica = models.DecimalField(max_digits=18, decimal_places=2)
    frontera = models.DecimalField(max_digits=18, decimal_places=2)
    cargo_administrativo = models.DecimalField(max_digits=18, decimal_places=2)
    horas_coprogramaticas = models.DecimalField(max_digits=18, decimal_places=2)
    ajustes_251 = models.DecimalField(max_digits=18, decimal_places=2)
    clase_escuela = models.DecimalField(max_digits=18, decimal_places=2)
    cargo_directivo_nocturna = models.DecimalField(max_digits=18, decimal_places=2)
    colectivo = models.DecimalField(max_digits=18, decimal_places=2)
    horas_compensatorias_18 = models.DecimalField(max_digits=18, decimal_places=2)
    numero_resolucion = models.CharField(max_length=400, blank=True)
    bloqueada = models.BooleanField()
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=50, blank=True)
    usuario_modificacion = models.CharField(max_length=50, blank=True)
    vacaciones_admin = models.DecimalField(max_digits=18, decimal_places=2)
    class Meta:
        managed = False
        db_table = 'pp_presupuesto_anexo'

class PpPresupuestoPlazasNuevas(models.Model):
    cuenta = models.ForeignKey(PpCatalogos, db_column='cuenta')
    codigo_presupuesto = models.ForeignKey(PpEncPresupuestoNuevo, db_column='codigo_presupuesto')
    total_plazas_disponibles = models.IntegerField(blank=True, null=True)
    total_horas_disponibles = models.IntegerField(blank=True, null=True)
    total_plazas_ejecutadas = models.IntegerField(blank=True, null=True)
    total_horas_ejecutadas = models.IntegerField(blank=True, null=True)
    presupuesto_plazas = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_horas = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_ejecutado_plazas = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_ejecutado_horas = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fecha_creacion_plazas = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_presupuesto_plazas_nuevas'

class PpPresupuestosCuenta(models.Model):
    codigo_periodo = models.ForeignKey(PpPeriodos, db_column='codigo_periodo')
    cuenta = models.ForeignKey(PpCatalogos, db_column='cuenta')
    codigo_presupuesto = models.ForeignKey(PpEncabezadoPresupuestos, db_column='codigo_presupuesto')
    presupuesto_original = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_solicitado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_bajo_techo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_anio_anterior = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    modif_aumento_monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    modif_mas = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    modif_menos = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_modificado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    congelamiento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    pagos_ejecutados = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    excedente = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    deficit = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    disponible_total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_comprometido = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    presupuesto_ordenado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    nivel = models.SmallIntegerField(blank=True, null=True)
    codigo_carga = models.CharField(max_length=10, blank=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    cuenta_cancelada = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_presupuestos_cuenta'

class PpProcesos(models.Model):
    codigo_proceso = models.IntegerField(primary_key=True)
    nombre_proceso = models.CharField(max_length=100)
    estado_proceso = models.IntegerField()
    observacion_proceso = models.CharField(max_length=255)
    tipo_proceso = models.CharField(max_length=2)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_procesos'

class PpProcesosConcurrentes(models.Model):
    codigo_proceso = models.IntegerField(unique=True)
    nombre_proceso = models.CharField(max_length=50)
    estado_proceso = models.SmallIntegerField()
    tipo_proceso = models.SmallIntegerField(blank=True, null=True)
    observacion_proceso = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_procesos_concurrentes'

class PpProfesionalizaciones(models.Model):
    codigo_documento_profesional = models.CharField(unique=True, max_length=20)
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    codigo_centro_estudio = models.IntegerField(blank=True, null=True)
    codigo_pais = models.IntegerField(blank=True, null=True)
    codigo_titulo = models.IntegerField(blank=True, null=True)
    estado_documento = models.ForeignKey(PpEstadosDocumentos, db_column='estado_documento')
    fecha_solicitud_profesional = models.DateTimeField()
    duracion_estudios_anios = models.SmallIntegerField(blank=True, null=True)
    duracion_estudios_meses = models.SmallIntegerField(blank=True, null=True)
    clases_requisitos = models.SmallIntegerField(blank=True, null=True)
    numero_periodo_estudios = models.SmallIntegerField(blank=True, null=True)
    fecha_inicio_estudios = models.DateTimeField(blank=True, null=True)
    numero_periodos_aprobados = models.SmallIntegerField(blank=True, null=True)
    clases_reportadas = models.SmallIntegerField(blank=True, null=True)
    tipo_profesional_anterior = models.CharField(max_length=3, blank=True)
    en_vigencia_profesionalizacion = models.SmallIntegerField(blank=True, null=True)
    xnearmensaje = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    observacion_profesional = models.TextField(blank=True)
    presenta_certificacion = models.SmallIntegerField()
    meses_por_periodo = models.SmallIntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_profesionalizaciones'

class PpPuntajesMeritos(models.Model):
    codigo_logro = models.IntegerField()
    codigo_meritos = models.IntegerField()
    descripcion_meritos = models.CharField(max_length=100)
    duracion_minima = models.IntegerField(blank=True, null=True)
    duracion_maxima = models.IntegerField(blank=True, null=True)
    puntajes_meritos = models.IntegerField()
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_puntajes_meritos'

class PpRazonesPeticion(models.Model):
    codigo_razon = models.SmallIntegerField(primary_key=True)
    descripcion_razon = models.CharField(max_length=100)
    abreviatura_razon = models.CharField(max_length=15)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_razones_peticion'

class PpReactivaciones(models.Model):
    codigo_reactivar = models.CharField(primary_key=True, max_length=20)
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    estado_documento = models.ForeignKey(PpEstadosDocumentos, db_column='estado_documento')
    fecha_solicitud_reactivar = models.DateTimeField()
    motivo_reactivacion = models.CharField(max_length=50)
    observacion_reactivar = models.TextField(blank=True)
    presenta_dictamen = models.SmallIntegerField(blank=True, null=True)
    xnearmensaje = models.DecimalField(max_digits=10, decimal_places=0)
    documentos = models.SmallIntegerField()
    en_vigencia = models.SmallIntegerField()
    edad_reactivar = models.SmallIntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_reactivaciones'

class PpReclamosPagos(models.Model):
    codigo_reclamo = models.CharField(primary_key=True, max_length=20)
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    estado_documento = models.ForeignKey(PpEstadosDocumentos, db_column='estado_documento')
    fecha_reclamo = models.DateTimeField()
    xnearmensaje = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    inprema_docente = models.DecimalField(max_digits=18, decimal_places=2)
    inprema_patronal = models.DecimalField(max_digits=18, decimal_places=2)
    sueldo_nominal = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    sueldo_neto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    observaciones_reclamo = models.TextField(blank=True)
    numero_oficio = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_reclamos_pagos'

class PpRegistroAniosServicios(models.Model):
    identidad_empleado = models.CharField(primary_key=True, max_length=13)
    anios_servicios = models.IntegerField(blank=True, null=True)
    meses_servicios = models.IntegerField(blank=True, null=True)
    dias_servicios = models.IntegerField(blank=True, null=True)
    observacion = models.CharField(max_length=250, blank=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    horas_servicios = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    fecha_ultimo_analisis = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_registro_anios_servicios'

class PpReparos(models.Model):
    codigo_reparo = models.CharField(primary_key=True, max_length=20)
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    fecha_estudio_reparo = models.DateTimeField()
    codigo_tipo_profesional = models.ForeignKey('PpTipoProfesionales', db_column='codigo_tipo_profesional', blank=True, null=True)
    estado_documento = models.ForeignKey(PpEstadosDocumentos, db_column='estado_documento', blank=True, null=True)
    total_favor_estado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    total_favor_docente = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cuota_reparo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    saldo_reparo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    en_vigencia = models.SmallIntegerField()
    descripcion_periodo = models.CharField(max_length=20, blank=True)
    observaciones_reparo = models.TextField(blank=True)
    xnearmensaje = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    saldo_cobrado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_reparos'

class PpRequisitos(models.Model):
    codigo_titulo_requisito = models.IntegerField()
    codigo_titulo = models.ForeignKey('PpTitulos', db_column='codigo_titulo')
    codigo_nivel_educativo = models.ForeignKey(PpNivelesEducativos, db_column='codigo_nivel_educativo', blank=True, null=True)
    codigo_tipo_profesional = models.ForeignKey('PpTipoProfesionales', db_column='codigo_tipo_profesional')
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_requisitos'

class PpRequisitosCargos(models.Model):
    codigo_cargo = models.ForeignKey(PpCargos, db_column='codigo_cargo')
    codigo_grado_academico = models.ForeignKey(PpGradosAcademicos, db_column='codigo_grado_academico')
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_requisitos_cargos'

class PpResumenMeritos(models.Model):
    oficio_dictamen_meritos = models.CharField(primary_key=True, max_length=20)
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    estado_documento = models.ForeignKey(PpEstadosDocumentos, db_column='estado_documento', blank=True, null=True)
    fecha_estudio_meritos = models.DateTimeField()
    fecha_dictamen_meritos = models.DateTimeField()
    fecha_recepcion_dictamen = models.DateTimeField()
    puntaje_total_aprobado = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    xnearmensaje = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    observaciones_dictamen = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_resumen_meritos'

class PpRotulosAnexoAdmon2005(models.Model):
    institucion = models.CharField(max_length=2, blank=True)
    programa = models.CharField(max_length=2, blank=True)
    subprograma = models.CharField(max_length=2, blank=True)
    proyecto = models.CharField(max_length=2, blank=True)
    actividad = models.CharField(max_length=2, blank=True)
    area = models.CharField(max_length=2, blank=True)
    seccion = models.CharField(max_length=3, blank=True)
    descripcion = models.CharField(max_length=60, blank=True)
    ejecutora = models.CharField(max_length=45, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_rotulos_anexo_admon_2005'

class PpScanvisionDocentes(models.Model):
    identidad = models.CharField(max_length=13)
    nombre = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'pp_scanvision_docentes'

class PpSecuenciaCheques(models.Model):
    anio_cheque = models.CharField(max_length=4)
    tipo_cheque = models.CharField(max_length=2)
    secuencial_cheque = models.DecimalField(max_digits=6, decimal_places=0)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_secuencia_cheques'

class PpSecuencialDepositos(models.Model):
    anio_deposito = models.CharField(max_length=4)
    tipo_deposito = models.CharField(max_length=2)
    secuencial_deposito = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_secuencial_depositos'

class PpSecuencialDocumentos(models.Model):
    categoria_tramite = models.CharField(max_length=4)
    anio_secuencial = models.DecimalField(max_digits=4, decimal_places=0)
    secuencial_documento = models.IntegerField(blank=True, null=True)
    codigo_unidad = models.ForeignKey('PpUnidadesEjecutoras', db_column='codigo_unidad')
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=30)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_secuencial_documentos'

class PpSeguimientosDocumentos(models.Model):
    codigo_documento_enviado = models.CharField(max_length=37)
    fecha_emision = models.DateTimeField()
    secuencial_documento = models.IntegerField()
    estado_documento = models.ForeignKey(PpEstadosDocumentos, db_column='estado_documento')
    rol_creacion = models.CharField(max_length=25, blank=True)
    unidad_ejecutora_creacion = models.CharField(max_length=2, blank=True)
    rol_anterior = models.CharField(max_length=25, blank=True)
    unidad_ejecutora_anterior = models.CharField(max_length=2, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_seguimientos_documentos'

class PpSeleccionados(models.Model):
    codigo_seleccionado = models.IntegerField()
    fecha_seleccion = models.DateTimeField()
    cuenta = models.ForeignKey(PpPlazas, db_column='cuenta', blank=True, null=True)
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado', blank=True, null=True)
    codigo_unidad = models.ForeignKey('PpUnidadesEjecutoras', db_column='codigo_unidad')
    tipo_seleccionado = models.SmallIntegerField()
    fecha_creacion = models.DateTimeField()
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_seleccionados'

class PpSiafiClasePlanillas(models.Model):
    codigo_clase_pla = models.CharField(primary_key=True, max_length=3)
    descripcion_clase_planilla = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_siafi_clase_planillas'

class PpSiafiDetDocPlanillasRegenerar(models.Model):
    codigo_periodo = models.CharField(max_length=6)
    identidad_empleado = models.CharField(max_length=13)
    codigo_planilla = models.CharField(max_length=50)
    pagado = models.CharField(max_length=1)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'pp_siafi_det_doc_planillas_regenerar'

class PpSiafiEncDocPlanillasNopagados(models.Model):
    codigo_periodo = models.CharField(max_length=6)
    identidad_empleado = models.CharField(max_length=13)
    pagado = models.CharField(max_length=1)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'pp_siafi_enc_doc_planillas_nopagados'

class PpSiafiSacadosperiodosSingenerar(models.Model):
    codigo_periodo = models.CharField(max_length=6)
    identidad_empleado = models.CharField(max_length=13)
    observacion_siafi = models.CharField(max_length=255, blank=True)
    pagado = models.CharField(max_length=1, blank=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'pp_siafi_sacadosperiodos_singenerar'

class PpSolicitudDocumentos(models.Model):
    codigo_solicita_docto = models.CharField(unique=True, max_length=20)
    codigo_categoria = models.CharField(max_length=4)
    identidad_empleado = models.CharField(max_length=13, blank=True)
    estado_documento = models.SmallIntegerField()
    fecha_solicitud = models.DateTimeField()
    fecha_impresion = models.DateTimeField(blank=True, null=True)
    numero_impresiones = models.IntegerField(blank=True, null=True)
    entregado_docente = models.SmallIntegerField()
    observaciones_docto = models.TextField(blank=True)
    xnearmensaje = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    cuenta_prespuesto = models.CharField(max_length=50, blank=True)
    reparo = models.CharField(max_length=50, blank=True)
    cuenta_constancia = models.CharField(max_length=50, blank=True)
    cuenta_solicitud = models.CharField(max_length=50, blank=True)
    cuenta_siafi = models.CharField(max_length=50, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=15, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=15, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_solicitud_documentos'

class PpSolicitudesPagos(models.Model):
    codigo_solicitud_pago = models.CharField(primary_key=True, max_length=20)
    codigo_departamento = models.ForeignKey(PpCentrosEducativos, db_column='codigo_departamento')
    codigo_municipio = models.ForeignKey(PpCentrosEducativos, db_column='codigo_municipio')
    codigo_centro = models.ForeignKey(PpCentrosEducativos, db_column='codigo_centro')
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    cuenta = models.ForeignKey(PpPlazas, db_column='cuenta')
    estado_documento = models.ForeignKey(PpEstadosDocumentos, db_column='estado_documento')
    fecha_solicitud_pago = models.DateTimeField(blank=True, null=True)
    en_vigencia_pago = models.SmallIntegerField(blank=True, null=True)
    observacion_solicitud_pago = models.CharField(max_length=250, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_solicitudes_pagos'

class PpTablaAntiguedad(models.Model):
    anio_inicial = models.IntegerField()
    anio_final = models.IntegerField()
    monto_pagado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_nuevo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    anio = models.CharField(max_length=4)
    class Meta:
        managed = False
        db_table = 'pp_tabla_antiguedad'

class PpTablaCargos(models.Model):
    codigo_cargo_generico = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=100, blank=True)
    monto_pagado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_nuevo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    anio = models.CharField(max_length=4)
    class Meta:
        managed = False
        db_table = 'pp_tabla_cargos'

class PpTablaEmpleados(models.Model):
    identidad_empleado = models.CharField(max_length=13)
    codigo_tipo_profesional = models.CharField(max_length=3, blank=True)
    ultima_categoria = models.IntegerField(blank=True, null=True)
    anio_inicial = models.IntegerField(blank=True, null=True)
    anio_final = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_tabla_empleados'

class PpTablaHorasClase(models.Model):
    tipo_profesional = models.CharField(max_length=2, blank=True)
    horas_clase = models.IntegerField(blank=True, null=True)
    sueldo_base = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    sueldo_calificacion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    sueldo_total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    sueldo_base_nuevo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    sueldo_calificacion_nuevo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    sueldo_total_nuevo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    anio = models.CharField(max_length=4, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_tabla_horas_clase'

class PpTablaMeritos(models.Model):
    categoria = models.IntegerField()
    monto_pagado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_nuevo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    anio = models.CharField(max_length=4)
    class Meta:
        managed = False
        db_table = 'pp_tabla_meritos'

class PpTablaPlazas(models.Model):
    cuenta = models.CharField(unique=True, max_length=50)
    horas_clase = models.IntegerField(blank=True, null=True)
    codigo_cargo_generico = models.CharField(max_length=2, blank=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_tabla_plazas'

class PpTablasConversionesCopia2009(models.Model):
    cuenta = models.CharField(max_length=50)
    codigo_conversion = models.IntegerField()
    corrent = models.DecimalField(max_digits=4, decimal_places=0)
    programa = models.DecimalField(max_digits=2, decimal_places=0)
    subprog = models.DecimalField(max_digits=2, decimal_places=0)
    proyecto = models.DecimalField(max_digits=3, decimal_places=0)
    actobra = models.DecimalField(max_digits=3, decimal_places=0)
    partida = models.DecimalField(max_digits=5, decimal_places=0)
    codfte = models.DecimalField(max_digits=5, decimal_places=0)
    org_financ = models.DecimalField(max_digits=3, decimal_places=0)
    codigo_benef = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    estructura_siafi = models.CharField(max_length=50, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    gerencia_admon = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    unidad_ejecutora = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_tablas_conversiones_copia_2009'

class PpTemarios(models.Model):
    codigo_capacitacion = models.ForeignKey(PpCapacitaciones, db_column='codigo_capacitacion')
    codigo_temario = models.IntegerField()
    descripcion_temario = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_temarios'

class PpTiempoLaboral(models.Model):
    codigo_nivel_educativo = models.ForeignKey(PpNivelesEducativos, db_column='codigo_nivel_educativo')
    horario_plaza = models.SmallIntegerField()
    codigo_planta = models.ForeignKey(PpPlantas, db_column='codigo_planta')
    horas_semanales = models.IntegerField(blank=True, null=True)
    tipo_plaza = models.SmallIntegerField()
    meses_laborables = models.IntegerField(blank=True, null=True)
    meses_no_incluidos = models.CharField(max_length=50, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_tiempo_laboral'

class PpTipoEmpleados(models.Model):
    codigo_tipo_empleado = models.IntegerField(primary_key=True)
    descripcion_tipo_empleado = models.CharField(max_length=25)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_tipo_empleados'

class PpTipoProfesionales(models.Model):
    codigo_tipo_profesional = models.CharField(primary_key=True, max_length=3)
    descripcion_tipo_profesional = models.CharField(max_length=30)
    pago_anios_servicios = models.SmallIntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_tipo_profesionales'

class PpTiposCargos(models.Model):
    codigo_tipo_cargo = models.CharField(primary_key=True, max_length=2)
    nombre_tipo_cargo = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_tipos_cargos'

class PpTiposCentrosEducativos(models.Model):
    codigo_tipo_centro = models.IntegerField(primary_key=True)
    codigo_unidad = models.ForeignKey('PpUnidadOrganizacionales', db_column='codigo_unidad', blank=True, null=True)
    descripcion_tipo_centro = models.CharField(max_length=100)
    abreviatura_tipo_centro = models.CharField(max_length=15, blank=True)
    es_especial = models.SmallIntegerField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_tipos_centros_educativos'

class PpTiposEvaluaciones(models.Model):
    codigo_tipo_evaluacion = models.IntegerField(primary_key=True)
    descripcion_evaluacion = models.CharField(max_length=100)
    abreviatura_evaluacion = models.CharField(max_length=25)
    puntaje_maximo_tipo = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_tipos_evaluaciones'

class PpTiposFondos(models.Model):
    codigo_fondo = models.IntegerField(primary_key=True)
    descripcion_fondo = models.CharField(max_length=25)
    abreviatura_fondo = models.CharField(max_length=15, blank=True)
    tipo_fondo = models.CharField(max_length=1)
    usuario_creacion = models.CharField(max_length=25)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField()
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_tipos_fondos'

class PpTiposMovPlazas(models.Model):
    codigo_tipo_mov = models.IntegerField(primary_key=True)
    descripcion_mov = models.CharField(max_length=50)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_tipos_mov_plazas'

class PpTiposMovimientos(models.Model):
    codigo_movimiento = models.IntegerField(primary_key=True)
    descripcion_mov = models.CharField(max_length=100)
    abreviatura_mov = models.CharField(max_length=10)
    descripcion_corta_mov = models.CharField(max_length=25)
    interpretacion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    clase_movimientos = models.SmallIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_tipos_movimientos'

class PpTiposTransacciones(models.Model):
    codigo_tipo = models.IntegerField(primary_key=True)
    descripcion_tipo_trans = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_tipos_transacciones'

class PpTitulos(models.Model):
    codigo_titulo = models.IntegerField(primary_key=True)
    codigo_grado_academico = models.ForeignKey(PpGradosAcademicos, db_column='codigo_grado_academico')
    codigo_tipo_profesional = models.ForeignKey(PpTipoProfesionales, db_column='codigo_tipo_profesional')
    descripcion_titulo = models.CharField(max_length=200)
    abreviatura_titulo = models.CharField(max_length=25)
    licencias_estudio = models.SmallIntegerField()
    requisito_diplomado = models.SmallIntegerField()
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    pagar_titulo = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_titulos'

class PpTitulosCensoTmp(models.Model):
    identidad_empleado = models.CharField(max_length=13, blank=True)
    apellidos = models.CharField(db_column='Apellidos', max_length=255, blank=True) # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=255, blank=True) # Field name made lowercase.
    gradoacademico = models.CharField(db_column='GradoAcademico', max_length=255, blank=True) # Field name made lowercase.
    siarhd = models.SmallIntegerField(db_column='SIARHD', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'pp_titulos_censo_tmp'

class PpTransPlanillas(models.Model):
    codigo_planilla = models.CharField(max_length=10)
    identidad_empleado = models.CharField(max_length=13)
    cuenta = models.CharField(max_length=50)
    codigo_transaccion = models.IntegerField()
    nombres_empleado = models.CharField(max_length=35, blank=True)
    apellidos_empleado = models.CharField(max_length=35, blank=True)
    codigo_nivel_educativo = models.IntegerField()
    codigo_banco_deposito = models.IntegerField(blank=True, null=True)
    cuenta_bancaria = models.CharField(max_length=25, blank=True)
    codigo_departamento = models.CharField(max_length=2, blank=True)
    codigo_municipio = models.CharField(max_length=2, blank=True)
    codigo_centro = models.CharField(max_length=5, blank=True)
    codigo_aldea = models.CharField(max_length=5, blank=True)
    codigo_clase = models.IntegerField(blank=True, null=True)
    codigo_planta = models.CharField(max_length=2, blank=True)
    codigo_cargo = models.CharField(max_length=15, blank=True)
    codigo_tipo_cargo = models.CharField(max_length=2, blank=True)
    codigo_cargo_generico = models.CharField(max_length=2, blank=True)
    codigo_distrito = models.IntegerField(blank=True, null=True)
    monto_transaccion = models.DecimalField(max_digits=18, decimal_places=2)
    monto_sobregiro = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    estructura_ejecucion = models.CharField(max_length=50, blank=True)
    estado_presupuesto = models.SmallIntegerField(blank=True, null=True)
    clase_transaccion = models.SmallIntegerField(blank=True, null=True)
    descripcion_corta_trans = models.CharField(max_length=25, blank=True)
    descripcion_transaccion = models.CharField(max_length=100, blank=True)
    clase_centro = models.IntegerField(blank=True, null=True)
    codigo_tipo_centro = models.IntegerField(blank=True, null=True)
    codigo_unidad = models.CharField(max_length=1, blank=True)
    anio_cheque = models.CharField(max_length=4, blank=True)
    tipo_pago_cheque = models.CharField(max_length=2, blank=True)
    numero_cheque = models.CharField(max_length=6, blank=True)
    item_matricial = models.IntegerField(blank=True, null=True)
    corrent = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    programa = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    subprog = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    proyecto = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    actobra = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    partida = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    codfte = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    org_financ = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    benef = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    numero_plaza = models.CharField(max_length=6, blank=True)
    horas_clase = models.IntegerField(blank=True, null=True)
    nombre_tipo_cargo = models.CharField(max_length=50, blank=True)
    nombre_cargo_generico = models.CharField(max_length=50, blank=True)
    descripcion_clase = models.CharField(max_length=50, blank=True)
    nombre_unidad = models.CharField(max_length=50, blank=True)
    descripcion_planta = models.CharField(max_length=50, blank=True)
    descripcion_cargo = models.CharField(max_length=50, blank=True)
    descripcion_departamento = models.CharField(max_length=25, blank=True)
    descripcion_municipio = models.CharField(max_length=25, blank=True)
    descripcion_centro = models.CharField(max_length=120, blank=True)
    descripcion_aldea = models.CharField(max_length=25, blank=True)
    descripcion_distrito = models.CharField(max_length=25, blank=True)
    descripcion_tipo_centro = models.CharField(max_length=100, blank=True)
    abreviatura_trans = models.CharField(max_length=10, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    anio_deposito = models.CharField(max_length=4, blank=True)
    tipo_deposito = models.CharField(max_length=2, blank=True)
    numero_deposito = models.CharField(max_length=6, blank=True)
    gerencia_admon = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    unidad_ejecutora = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_trans_planillas'

class PpTransacciones(models.Model):
    codigo_transaccion = models.IntegerField(primary_key=True)
    codigo_tipo = models.ForeignKey(PpTiposTransacciones, db_column='codigo_tipo')
    codigo_institucion = models.ForeignKey(PpInstitucionesExternas, db_column='codigo_institucion', blank=True, null=True)
    codigo_horario = models.ForeignKey(PpHorarios, db_column='codigo_horario', blank=True, null=True)
    codigo_ct = models.ForeignKey(PpCodigosCt, db_column='codigo_ct', blank=True, null=True)
    pp_codigo_ct = models.ForeignKey(PpCodigosCt, db_column='pp__codigo_ct', blank=True, null=True) # Field renamed because it contained more than one '_' in a row.
    codigo_funcion = models.ForeignKey(PpFuncionesCalculo, db_column='codigo_funcion', blank=True, null=True)
    descripcion_trans = models.CharField(max_length=100)
    abreviatura_trans = models.CharField(max_length=10)
    descripcion_corta_trans = models.CharField(max_length=25, blank=True)
    clase_transaccion = models.SmallIntegerField()
    prioridad_clase = models.SmallIntegerField(blank=True, null=True)
    acumulador = models.SmallIntegerField()
    posteable = models.SmallIntegerField(blank=True, null=True)
    repetible = models.SmallIntegerField(blank=True, null=True)
    recalcular = models.SmallIntegerField(blank=True, null=True)
    calculo_automatico = models.SmallIntegerField(blank=True, null=True)
    importada = models.SmallIntegerField(blank=True, null=True)
    calculo_diario = models.SmallIntegerField(blank=True, null=True)
    horas_maximo = models.IntegerField(blank=True, null=True)
    tipo_control = models.SmallIntegerField(blank=True, null=True)
    emite_cheque = models.SmallIntegerField(blank=True, null=True)
    descripcion_cheque = models.CharField(max_length=100, blank=True)
    estructura_financia_trans = models.CharField(max_length=50, blank=True)
    estructura_alterna = models.CharField(max_length=50, blank=True)
    generar_transferencia = models.SmallIntegerField(blank=True, null=True)
    tipo_enlace = models.SmallIntegerField(blank=True, null=True)
    tipo_valor_aplicado = models.SmallIntegerField(blank=True, null=True)
    monto_valor_aplicado = models.SmallIntegerField(blank=True, null=True)
    restriccion_nivel = models.SmallIntegerField(blank=True, null=True)
    restriccion_cargo = models.SmallIntegerField(blank=True, null=True)
    restriccion_titulo = models.SmallIntegerField(blank=True, null=True)
    restriccion_tipo_prof = models.SmallIntegerField(blank=True, null=True)
    restriccion_grado = models.SmallIntegerField(blank=True, null=True)
    restriccion_departamento = models.SmallIntegerField(blank=True, null=True)
    restriccion_municipio = models.SmallIntegerField(blank=True, null=True)
    restriccion_centro = models.SmallIntegerField(blank=True, null=True)
    restriccion_merito = models.SmallIntegerField(blank=True, null=True)
    categoria_documento = models.CharField(max_length=4, blank=True)
    restriccion_documento = models.SmallIntegerField(blank=True, null=True)
    restriccion_ubicacion = models.SmallIntegerField(blank=True, null=True)
    restriccion_tipo_centro = models.SmallIntegerField(blank=True, null=True)
    restriccion_clase_centro = models.SmallIntegerField(blank=True, null=True)
    restriccion_montos = models.SmallIntegerField(blank=True, null=True)
    fecha_activacion = models.DateTimeField(blank=True, null=True)
    fecha_desactivacion = models.DateTimeField(blank=True, null=True)
    estado_transaccion = models.SmallIntegerField()
    modo_aplicacion = models.SmallIntegerField()
    campo_aplicacion = models.SmallIntegerField()
    meses = models.IntegerField(blank=True, null=True)
    tipo_valores = models.SmallIntegerField(blank=True, null=True)
    fecha_graduacion1 = models.DateTimeField(blank=True, null=True)
    fecha_graduacion2 = models.DateTimeField(blank=True, null=True)
    promedio = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    estado_titulo = models.SmallIntegerField(blank=True, null=True)
    codigo_centro_estudio = models.IntegerField(blank=True, null=True)
    frontera_centro = models.CharField(max_length=2, blank=True)
    cuenta_presupuesto = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    parametro1 = models.SmallIntegerField(blank=True, null=True)
    parametro2 = models.SmallIntegerField(blank=True, null=True)
    monto_inferior = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_superior = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fondo01 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    fondo02 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    partida_gasto_f01 = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    partida_gasto_f02 = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    estructura_f01 = models.CharField(max_length=50, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    sueldo_fijo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    eliminar_colaterales = models.SmallIntegerField(blank=True, null=True)
    codigo_identificador = models.CharField(max_length=13, blank=True)
    tipo_siafi = models.CharField(db_column='tipo_SIAFI', max_length=2, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'pp_transacciones'

class PpTransaccionesEmpleadosPendientePago(models.Model):
    codigo_periodo = models.CharField(max_length=6)
    identidad_empleado = models.CharField(max_length=13)
    cuenta = models.CharField(max_length=50)
    codigo_transaccion = models.IntegerField()
    secuencial_tran = models.IntegerField()
    item_matricial = models.IntegerField(blank=True, null=True)
    fecha_inicial = models.DateTimeField(blank=True, null=True)
    fecha_final = models.DateTimeField(blank=True, null=True)
    transaccion_permanente = models.SmallIntegerField(blank=True, null=True)
    estado_plaza_registro = models.SmallIntegerField(blank=True, null=True)
    periodo_original = models.CharField(max_length=6, blank=True)
    fecha_activacion = models.DateTimeField(blank=True, null=True)
    fecha_desactivacion = models.DateTimeField(blank=True, null=True)
    monto_periodo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    numero_documento = models.CharField(max_length=20, blank=True)
    estructura = models.CharField(max_length=50, blank=True)
    tipo_generacion = models.SmallIntegerField(blank=True, null=True)
    observacion_tran = models.CharField(max_length=250, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_transacciones_empleados_pendiente_pago'

class PpTransaccionesInstituciones(models.Model):
    codigo_periodo = models.ForeignKey(PpPeriodos, db_column='codigo_periodo')
    codigo_transaccion = models.ForeignKey(PpTransacciones, db_column='codigo_transaccion')
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    monto = models.DecimalField(max_digits=18, decimal_places=2)
    estado_aplicado = models.SmallIntegerField(blank=True, null=True)
    estado_distribuido = models.SmallIntegerField(blank=True, null=True)
    fecha_cargado = models.DateTimeField(blank=True, null=True)
    fecha_aplicado = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_transacciones_instituciones'

class PpTransferenciasPlazas(models.Model):
    codigo_transferencia_plaza = models.CharField(primary_key=True, max_length=20)
    fecha_transferencia = models.DateTimeField(blank=True, null=True)
    codigo_fondo = models.ForeignKey(PpTiposFondos, db_column='codigo_fondo')
    codigo_organismo = models.ForeignKey(PpOrganismosFinanciadores, db_column='codigo_organismo')
    estado_documento = models.ForeignKey(PpEstadosDocumentos, db_column='estado_documento')
    codigo_presupuesto = models.ForeignKey(PpEncabezadoPresupuestos, db_column='codigo_presupuesto')
    codigo_nivel_origen = models.IntegerField()
    codigo_depto_origen = models.CharField(max_length=2)
    codigo_depto_destino = models.CharField(max_length=2)
    codigo_muni_origen = models.CharField(max_length=2)
    codigo_muni_destino = models.CharField(max_length=2)
    codigo_centro_origen = models.CharField(max_length=5)
    codigo_centro_destino = models.CharField(max_length=5)
    plaza_origen = models.CharField(max_length=50)
    plaza_destino = models.CharField(max_length=50, blank=True)
    observaciones = models.TextField(blank=True)
    xnearmensaje = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    plaza_nueva_creada = models.SmallIntegerField()
    plaza_nueva_cancelada = models.SmallIntegerField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.CharField(max_length=25, blank=True)
    municipio_origen_anterior = models.CharField(max_length=2, blank=True)
    centro_origen_anterior = models.CharField(max_length=5, blank=True)
    municipio_origen_depurado = models.CharField(max_length=1, blank=True)
    municipio_destino_anterior = models.CharField(max_length=2, blank=True)
    centro_destino_anterior = models.CharField(max_length=5, blank=True)
    municipio_destino_depurado = models.CharField(max_length=1, blank=True)
    plaza_destino_anterior = models.CharField(max_length=50, blank=True)
    plaza_destino_muni_depurado = models.CharField(max_length=1, blank=True)
    plaza_origen_anterior = models.CharField(max_length=50, blank=True)
    plaza_origen_muni_depurado = models.CharField(max_length=1, blank=True)
    codigo_nivel_destino = models.IntegerField(blank=True, null=True)
    usuario_supervisor = models.CharField(max_length=25, blank=True)
    fecha_aprobacion = models.DateTimeField(blank=True, null=True)
    no_resolucion = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_transferencias_plazas'

class PpTraslados(models.Model):
    codigo_unidad_origen = models.ForeignKey('PpUnidadesEjecutoras', db_column='codigo_unidad_origen')
    anio_traslados = models.IntegerField()
    codigo_registro_origen = models.IntegerField()
    codigo_departamento_destino = models.ForeignKey(PpDepartamentos, db_column='codigo_departamento_destino', blank=True, null=True)
    codigo_municipio_destino = models.CharField(max_length=2, blank=True)
    codigo_nivel_educ_destino = models.IntegerField(blank=True, null=True)
    codigo_centro_destino = models.CharField(max_length=5, blank=True)
    codigo_registro_destino = models.IntegerField()
    fecha_traslado = models.DateTimeField()
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    estado_candidatura = models.SmallIntegerField()
    fecha_ultimo_estado = models.DateTimeField()
    aplica_interinato = models.SmallIntegerField()
    aplica_rural = models.SmallIntegerField()
    codigo_motivo_traslado = models.ForeignKey(PpMotivosTraslados, db_column='codigo_motivo_traslado')
    observaciones_traslado = models.TextField(blank=True)
    nivel_educativo_actual = models.IntegerField()
    cargo_actual = models.CharField(max_length=15)
    codigo_centro_actual = models.CharField(max_length=5)
    clase_centro_actual = models.IntegerField()
    tipo_centro_actual = models.IntegerField()
    cuenta_actual = models.ForeignKey(PpPlazas, db_column='cuenta_actual')
    anios_servicio_traslado = models.IntegerField()
    meses_servicio_traslado = models.IntegerField()
    dias_servicio_traslado = models.IntegerField()
    horas_servicio_traslado = models.IntegerField()
    fecha_actual_servicio = models.DateTimeField()
    secuencial_seleccion = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_traslados'

class PpTscMantenimiento(models.Model):
    tipo_colateral = models.IntegerField()
    identidad_empleado = models.CharField(max_length=13)
    estado = models.CharField(max_length=1)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    observacion_tsc = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_tsc_mantenimiento'

class PpUnidadOrganizacionales(models.Model):
    codigo_unidad = models.CharField(primary_key=True, max_length=1)
    nombre_unidad = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_unidad_organizacionales'

class PpUnidadesEjecutoras(models.Model):
    codigo_unidad = models.CharField(primary_key=True, max_length=2)
    codigo_departamento = models.ForeignKey(PpDepartamentos, db_column='codigo_departamento')
    descripcion_unidad = models.CharField(max_length=50, blank=True)
    tipo_unidad = models.SmallIntegerField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_unidades_ejecutoras'

class PpUsuarios(models.Model):
    usuario = models.CharField(max_length=25)
    codigo_unidad = models.ForeignKey(PpUnidadesEjecutoras, db_column='codigo_unidad')
    nombre_usuario = models.CharField(max_length=50, blank=True)
    tipo_cargo = models.CharField(max_length=1, blank=True)
    estado = models.SmallIntegerField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25)
    fecha_creacion = models.DateTimeField()
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    infotecnologia = models.SmallIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_usuarios'

class PpUsuariosDocentes(models.Model):
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    usuario = models.CharField(max_length=25)
    class Meta:
        managed = False
        db_table = 'pp_usuarios_docentes'

class PpUsuariosEstadosCuenta(models.Model):
    usuario = models.CharField(primary_key=True, max_length=25)
    limite_impresion = models.IntegerField()
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pp_usuarios_estados_cuenta'

class PpUsuariosLicencias(models.Model):
    usuario = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_usuarios_licencias'

class PpValRecuDocente(models.Model):
    codigo_periodo = models.ForeignKey(PpPeriodos, db_column='codigo_periodo')
    identidad_empleado = models.ForeignKey(PpEmpleados, db_column='identidad_empleado')
    saldo_deudor_docente = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    saldo_pagado_docente = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    estado_deudor_docente = models.SmallIntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_val_recu_docente'

class PpValRecuInstitucion(models.Model):
    codigo_institucion = models.ForeignKey(PpInstitucionesExternas, db_column='codigo_institucion')
    codigo_periodo = models.ForeignKey(PpPeriodos, db_column='codigo_periodo')
    saldo_deudor_institucion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    saldo_pagado_institucion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    estado_deudor_institucion = models.SmallIntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_val_recu_institucion'

class PpValidacionFaltas(models.Model):
    tipo_falta = models.SmallIntegerField()
    tipo_sancion = models.SmallIntegerField()
    sancion_rango1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sancion_rango2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_validacion_faltas'

class PpXcategorias(models.Model):
    codigo_categoria = models.CharField(unique=True, max_length=4)
    tipo = models.CharField(max_length=40, blank=True)
    subtipo = models.CharField(max_length=40, blank=True)
    vigencia = models.CharField(max_length=1, blank=True)
    tabla_asociada = models.CharField(max_length=40, blank=True)
    llave_tabla_asociada = models.CharField(max_length=80, blank=True)
    campo_vigente = models.CharField(max_length=40, blank=True)
    campo_estado = models.CharField(max_length=40, blank=True)
    fecha_solicitud = models.CharField(max_length=40, blank=True)
    flujo = models.CharField(max_length=1, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_xcategorias'

class PpXdetalleReparo(models.Model):
    codigo_transaccion = models.IntegerField()
    periodo_detalle_reparo = models.CharField(max_length=6)
    cuenta = models.CharField(max_length=50)
    codigo_reparo = models.CharField(max_length=20)
    secuencial_histo_trans = models.IntegerField()
    departamento = models.CharField(max_length=50, blank=True)
    municipio = models.CharField(max_length=50, blank=True)
    nivel = models.CharField(max_length=50, blank=True)
    centro = models.CharField(max_length=50, blank=True)
    cargo = models.CharField(max_length=50, blank=True)
    transaccion = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_xdetalle_reparo'

class PpfParametros(models.Model):
    codigo_param = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=350)
    tipo_param = models.SmallIntegerField(blank=True, null=True)
    hora_1 = models.CharField(max_length=10, blank=True)
    hora_2 = models.CharField(max_length=10, blank=True)
    fecha_inicio = models.CharField(max_length=11, blank=True)
    fecha_final = models.CharField(max_length=11, blank=True)
    dia_semana = models.CharField(max_length=9, blank=True)
    inmediato = models.SmallIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ppf_parametros'

class PpfReportes(models.Model):
    codigo = models.IntegerField(primary_key=True)
    sintaxis = models.TextField()
    habilitado = models.IntegerField()
    nombre = models.CharField(max_length=1000)
    tipo_validacion = models.IntegerField(blank=True, null=True)
    base_datos = models.CharField(max_length=50, blank=True)
    orden = models.IntegerField(blank=True, null=True)
    ejecutar_local = models.SmallIntegerField(blank=True, null=True)
    nombre_funcion = models.CharField(max_length=40, blank=True)
    class Meta:
        managed = False
        db_table = 'ppf_reportes'

class PpfReportesDet(models.Model):
    codigo_rep = models.IntegerField()
    codigo_param = models.IntegerField()
    valor_default = models.CharField(max_length=1000, blank=True)
    class Meta:
        managed = False
        db_table = 'ppf_reportes_det'

class PpfReportesxrol(models.Model):
    rol = models.IntegerField()
    reporte = models.IntegerField()
    habilitado = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'ppf_reportesxrol'

class PpfRolxusuario(models.Model):
    usuario = models.CharField(primary_key=True, max_length=20)
    rol = models.IntegerField()
    estado = models.IntegerField()
    seguridad = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'ppf_rolxusuario'

class PpfTipoActualizacion(models.Model):
    codigo_actualizacion = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=300)
    class Meta:
        managed = False
        db_table = 'ppf_tipo_actualizacion'

class PpfTipoParametros(models.Model):
    codigo_parm = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    parametro = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'ppf_tipo_parametros'

class PpfTipoReportes(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=1000)
    class Meta:
        managed = False
        db_table = 'ppf_tipo_reportes'

class PpfUsuariosxetapa(models.Model):
    codigo_etapa = models.IntegerField()
    usuario = models.CharField(max_length=25)
    activo = models.NullBooleanField()
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.CharField(max_length=25, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'ppf_usuariosxetapa'

class TmpAjusteTransEmpleados(models.Model):
    identidad_empleado = models.CharField(max_length=13)
    cuenta = models.CharField(max_length=50)
    codigo_transaccion = models.IntegerField()
    secuencial_tran = models.IntegerField()
    item_matricial = models.IntegerField(blank=True, null=True)
    fecha_inicial = models.DateTimeField(blank=True, null=True)
    fecha_final = models.DateTimeField(blank=True, null=True)
    transaccion_permanente = models.SmallIntegerField(blank=True, null=True)
    estado_plaza_registro = models.SmallIntegerField(blank=True, null=True)
    periodo_original = models.CharField(max_length=6, blank=True)
    fecha_activacion = models.DateTimeField(blank=True, null=True)
    fecha_desactivacion = models.DateTimeField(blank=True, null=True)
    monto_periodo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    numero_documento = models.CharField(max_length=20, blank=True)
    estructura = models.CharField(max_length=50, blank=True)
    tipo_generacion = models.SmallIntegerField(blank=True, null=True)
    observacion_tran = models.CharField(max_length=250, blank=True)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    cuenta_anterior = models.CharField(max_length=50, blank=True)
    cuenta_muni_depurado = models.CharField(max_length=1, blank=True)
    periodo = models.CharField(max_length=6, blank=True)
    class Meta:
        managed = False
        db_table = 'tmp_ajuste_trans_empleados'

class TmpAnexoDescripciones(models.Model):
    corrent = models.FloatField(blank=True, null=True)
    gerencia_admon = models.FloatField(blank=True, null=True)
    gerencia_admon_desc = models.CharField(max_length=255, blank=True)
    unidad_ejecutora = models.FloatField(blank=True, null=True)
    unidad_ejecutora_desc = models.CharField(max_length=255, blank=True)
    programa = models.FloatField(blank=True, null=True)
    programa_desc = models.CharField(max_length=255, blank=True)
    subprog = models.FloatField(blank=True, null=True)
    subprog_desc = models.CharField(max_length=255, blank=True)
    proyecto = models.FloatField(blank=True, null=True)
    proyecto_desc = models.CharField(db_column='proyecto_Desc', max_length=255, blank=True) # Field name made lowercase.
    actobra = models.FloatField(blank=True, null=True)
    actobra_desc = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'tmp_anexo_descripciones'

class TmpAnexoPlanillaPagos(models.Model):
    codigo_periodo = models.CharField(max_length=6, blank=True)
    descripcion_departamento = models.CharField(max_length=25)
    descripcion_nivel_educativo = models.CharField(max_length=25)
    descripcion_municipio = models.CharField(max_length=25)
    descripcion_centro = models.CharField(max_length=120)
    identidad_empleado = models.CharField(max_length=13)
    nombre = models.CharField(max_length=71)
    cuenta = models.CharField(max_length=50)
    horas = models.IntegerField()
    trans_1 = models.DecimalField(max_digits=18, decimal_places=2)
    ftrans_2 = models.DecimalField(max_digits=18, decimal_places=2)
    ftrans_3 = models.DecimalField(max_digits=18, decimal_places=2)
    ftrans_4 = models.DecimalField(max_digits=18, decimal_places=2)
    ftrans_5 = models.DecimalField(max_digits=18, decimal_places=2)
    ftrans_7 = models.DecimalField(max_digits=18, decimal_places=2)
    ftrans_8 = models.DecimalField(max_digits=18, decimal_places=2)
    ftrans_21 = models.DecimalField(max_digits=18, decimal_places=2)
    ftrans_45 = models.DecimalField(max_digits=18, decimal_places=2)
    ftrans_48 = models.DecimalField(max_digits=18, decimal_places=2)
    ftrans_55 = models.DecimalField(max_digits=18, decimal_places=2)
    ftrans_98 = models.DecimalField(max_digits=18, decimal_places=2)
    ftrans_110 = models.DecimalField(max_digits=18, decimal_places=2)
    ftrans_146 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    ftrans_113 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tmp_anexo_planilla_pagos'

class ZSinIncremento(models.Model):
    cuenta = models.CharField(max_length=50)
    identidad_empleado = models.CharField(max_length=13)
    monto = models.DecimalField(max_digits=18, decimal_places=2)
    class Meta:
        managed = False
        db_table = 'z_sin_incremento'

class ZzTempoConvPlazas(models.Model):
    sector = models.CharField(max_length=1)
    depto = models.IntegerField(blank=True, null=True)
    munic = models.IntegerField(blank=True, null=True)
    centro = models.IntegerField(blank=True, null=True)
    codpla = models.IntegerField(blank=True, null=True)
    numpla = models.CharField(max_length=2)
    numemp = models.IntegerField(blank=True, null=True)
    orifon = models.CharField(max_length=2)
    codigo_plaza_siarhd = models.CharField(max_length=50)
    aniomes = models.CharField(max_length=6, blank=True)
    numpag = models.IntegerField(blank=True, null=True)
    identidad_as = models.CharField(max_length=14, blank=True)
    identidad_siarhd = models.CharField(max_length=13, blank=True)
    estado_plaza = models.IntegerField(blank=True, null=True)
    plaza_siarhd_anterior = models.CharField(max_length=50, blank=True)
    plaza_siarhd_muni_depurado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'zz_tempo_conv_plazas'

