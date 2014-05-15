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

class ArchivoBancosMg(models.Model):
    clave_centro = models.CharField(db_column='Clave_Centro', max_length=15) # Field name made lowercase.
    nombre_centro = models.CharField(max_length=150)
    direccion_especifica = models.CharField(max_length=150, blank=True)
    telefono_centro = models.CharField(max_length=13, blank=True)
    codigo_departamento_siarhd = models.CharField(max_length=2)
    codigo_municipio_siarhd = models.CharField(max_length=2)
    codigo_centro_siarhd = models.CharField(max_length=5)
    codigo_departamento_ee = models.CharField(max_length=2, blank=True)
    codigo_municipio_ee = models.CharField(max_length=2, blank=True)
    codigo_centro_ee = models.CharField(max_length=9, blank=True)
    codigo_banco = models.IntegerField(blank=True, null=True)
    tipo_cuenta = models.CharField(max_length=1, blank=True)
    numero_cuenta = models.CharField(max_length=50, blank=True)
    forma_pago = models.CharField(max_length=1, blank=True)
    nombre_exacto_cuenta = models.CharField(max_length=80, blank=True)
    generar_fo1 = models.CharField(max_length=1, blank=True)
    cuenta_aperturada = models.CharField(max_length=1, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    observacion = models.CharField(max_length=200, blank=True)
    usuario_verificacion = models.CharField(max_length=15, blank=True)
    fecha_verificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=15, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    sin_validar = models.CharField(max_length=1, blank=True)
    clave_centro_bloqueada = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'Archivo_Bancos_MG'

class ChChatrooms(models.Model):
    nombre_sala = models.CharField(max_length=50, blank=True)
    usuario_creador = models.ForeignKey('EeUsuarios', db_column='usuario_creador', blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    abierto = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'ch_chatrooms'

class ChMensajes(models.Model):
    chat_room_id = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    mensaje = models.CharField(max_length=255, blank=True)
    usuario = models.ForeignKey('EeUsuarios', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ch_mensajes'

class ChMensajesPrivados(models.Model):
    usuario = models.ForeignKey('EeUsuarios', blank=True, null=True)
    titulo = models.CharField(max_length=100, blank=True)
    contenido = models.CharField(max_length=2048, blank=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hilo = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ch_mensajes_privados'

class ChMensajesPrivadosDestinatarios(models.Model):
    mensaje = models.ForeignKey(ChMensajesPrivados)
    usuario = models.ForeignKey('EeUsuarios')
    class Meta:
        managed = False
        db_table = 'ch_mensajes_privados_destinatarios'

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

class EeAdultosEstadisticaEgresados(models.Model):
    boleta = models.ForeignKey('EeBoletasAdultos', blank=True, null=True)
    edad = models.ForeignKey('EeEdades', blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_adultos_estadistica_egresados'

class EeAdultosEstadisticaFinal(models.Model):
    boleta_id = models.IntegerField(blank=True, null=True)
    grado_id = models.IntegerField(blank=True, null=True)
    clase_estadistica_id = models.IntegerField(blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_adultos_estadistica_final'

class EeAdultosEstadisticaInicial(models.Model):
    seccion = models.ForeignKey('EeAdultosSeccionesEstadisticaInicial', blank=True, null=True)
    edad = models.ForeignKey('EeEdades', blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_adultos_estadistica_inicial'

class EeAdultosSeccionesEstadisticaInicial(models.Model):
    boleta = models.ForeignKey('EeBoletasAdultos', blank=True, null=True)
    repitentes = models.CharField(max_length=1, blank=True)
    grado = models.ForeignKey('EeGrados', blank=True, null=True)
    seccion = models.CharField(max_length=3, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_adultos_secciones_estadistica_inicial'

class EeAldeas(models.Model):
    municipio = models.ForeignKey('EeMunicipios')
    codigo_departamento = models.CharField(max_length=2, blank=True)
    codigo_municipio = models.CharField(max_length=2, blank=True)
    codigo_aldea = models.CharField(max_length=2, blank=True)
    descripcion_aldea = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_aldeas'

class EeAlmacenamientoAgua(models.Model):
    descripcion_almacenamiento = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_almacenamiento_agua'

class EeArchivosDescargables(models.Model):
    nombre_archivo = models.CharField(unique=True, max_length=255, blank=True)
    ruta_archivo = models.CharField(max_length=1024, blank=True)
    descripcion_archivo = models.CharField(max_length=1024, blank=True)
    longitud_bytes = models.BigIntegerField(blank=True, null=True)
    tipo_archivo = models.CharField(max_length=512, blank=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    descargas = models.IntegerField(blank=True, null=True)
    eliminado = models.NullBooleanField()
    usuario_creacion = models.ForeignKey('EeUsuarios', db_column='usuario_creacion', blank=True, null=True)
    usuario_actualizo = models.ForeignKey('EeUsuarios', db_column='usuario_actualizo', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_archivos_descargables'

class EeBarriosColonias(models.Model):
    caserio = models.ForeignKey('EeCaserios')
    codigo_departamento = models.CharField(max_length=2, blank=True)
    codigo_municipio = models.CharField(max_length=2, blank=True)
    codigo_aldea = models.CharField(max_length=2, blank=True)
    codigo_caserio = models.CharField(max_length=3, blank=True)
    codigo_barrio_colonia = models.CharField(max_length=3, blank=True)
    descripcion_barrio_colonia = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_barrios_colonias'

class EeBasicaEstadisticaClases(models.Model):
    boleta = models.ForeignKey('EeBoletasBasica', blank=True, null=True)
    grado = models.ForeignKey('EeGrados', blank=True, null=True)
    clase = models.ForeignKey('EeClasesAreas', blank=True, null=True)
    aprobados_femenino = models.IntegerField(blank=True, null=True)
    aprobados_masculino = models.IntegerField(blank=True, null=True)
    reprobados_femenino = models.IntegerField(blank=True, null=True)
    reprobados_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_basica_estadistica_clases'

class EeBasicaEstadisticaFinal(models.Model):
    boleta = models.ForeignKey('EeBoletasBasica', blank=True, null=True)
    grado = models.ForeignKey('EeGrados', blank=True, null=True)
    clase_estadistica = models.ForeignKey('EeClasesEstadisticas', blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_basica_estadistica_final'

class EeBasicaEstadisticaGraduados(models.Model):
    boleta = models.ForeignKey('EeBoletasBasica', blank=True, null=True)
    edad = models.ForeignKey('EeEdades', blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_basica_estadistica_graduados'

class EeBasicaEstadisticaInicial(models.Model):
    boleta = models.ForeignKey('EeBoletasBasica', blank=True, null=True)
    jornada = models.CharField(max_length=1, blank=True)
    repitentes = models.CharField(max_length=1, blank=True)
    grado = models.ForeignKey('EeGrados', blank=True, null=True)
    edad = models.ForeignKey('EeEdades', blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_basica_estadistica_inicial'

class EeBasicaEstadisticaInicialTrabajoInfantil(models.Model):
    boleta = models.ForeignKey('EeBoletasBasica', blank=True, null=True)
    jornada = models.CharField(max_length=1, blank=True)
    repitentes = models.CharField(max_length=1, blank=True)
    grado = models.ForeignKey('EeGrados', blank=True, null=True)
    edad = models.ForeignKey('EeEdades', blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_basica_estadistica_inicial_trabajo_infantil'

class EeBitacora(models.Model):
    usuario = models.ForeignKey('EeUsuarios', blank=True, null=True)
    operacion = models.ForeignKey('EeBitacoraOperaciones', blank=True, null=True)
    tabla = models.ForeignKey('EeBitacoraTablas', blank=True, null=True)
    afectado_id = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_bitacora'

class EeBitacoraOperaciones(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion_operacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_bitacora_operaciones'

class EeBitacoraTablas(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_tabla = models.CharField(max_length=100, blank=True)
    nombre_modulo = models.CharField(max_length=100, blank=True)
    vista_asociada = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_bitacora_tablas'

class EeBoletaAdministrativoGrados(models.Model):
    boleta = models.ForeignKey('EeBoletas')
    grado = models.ForeignKey('EeGrados')
    cargo = models.ForeignKey('EeCargos')
    tipo_centro = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_boleta_administrativo_grados'

class EeBoletaOrganizaciones(models.Model):
    boleta = models.ForeignKey('EeBoletas')
    organizacion = models.ForeignKey('EeOrganizaciones')
    class Meta:
        managed = False
        db_table = 'ee_boleta_organizaciones'

class EeBoletaProgramas(models.Model):
    boleta = models.ForeignKey('EeBoletas')
    programa = models.ForeignKey('EeProgramas')
    class Meta:
        managed = False
        db_table = 'ee_boleta_programas'

class EeBoletaRecursosDiscapacitados(models.Model):
    boleta = models.ForeignKey('EeBoletas')
    recurso_discapacitados = models.ForeignKey('EeRecursosDiscapacitados')
    class Meta:
        managed = False
        db_table = 'ee_boleta_recursos_discapacitados'

class EeBoletas(models.Model):
    nombre_centro = models.CharField(max_length=255, blank=True)
    centro = models.ForeignKey('EeCentros')
    tipo_boleta = models.ForeignKey('EeTiposBoleta')
    periodo = models.ForeignKey('EePeriodos')
    aldea = models.ForeignKey(EeAldeas, blank=True, null=True)
    caserio = models.ForeignKey('EeCaserios', blank=True, null=True)
    barrio_colonia = models.ForeignKey(EeBarriosColonias, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True)
    telefono_fijo = models.CharField(max_length=10, blank=True)
    telefono_comunitario_celular = models.CharField(max_length=12, blank=True)
    correo_electronico = models.CharField(max_length=255, blank=True)
    en_funcionamiento = models.BooleanField()
    inicio_funcionamiento = models.IntegerField(blank=True, null=True)
    motivo_cierre = models.CharField(max_length=25, blank=True)
    cambio_nombre = models.BooleanField()
    nombre_anterior = models.CharField(max_length=255, blank=True)
    fecha_cambio_nombre = models.DateTimeField(blank=True, null=True)
    acuerdo_cambio_nombre = models.CharField(max_length=20, blank=True)
    funciona_edificio_propio = models.NullBooleanField()
    comparte_edificio = models.NullBooleanField()
    centros_comparte_edificio = models.CharField(max_length=255, blank=True)
    tipo_administracion = models.ForeignKey('EeTiposAdministracion', blank=True, null=True)
    tipo_zona = models.ForeignKey('EeTiposZona', blank=True, null=True)
    pais_frontera = models.ForeignKey('EePaisFrontera', blank=True, null=True)
    distancia = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tipo_centro = models.ForeignKey('EeTiposCentro', blank=True, null=True)
    periodo_escolar = models.CharField(max_length=1, blank=True)
    director = models.ForeignKey('EeDirectores', blank=True, null=True)
    director_modo_cargo = models.ForeignKey('EeModosCargo', blank=True, null=True)
    fecha_llenado = models.DateTimeField(blank=True, null=True)
    llenado_por = models.IntegerField(blank=True, null=True)
    infraestructura = models.ForeignKey('EeInfraestructuras', blank=True, null=True)
    aplica_curriculo = models.NullBooleanField()
    razon_no_aplica_curriculo = models.CharField(max_length=100, blank=True)
    utiliza_textos_secretaria = models.NullBooleanField()
    razon_no_usa_textos = models.CharField(max_length=100, blank=True)
    aplica_adecuaciones = models.NullBooleanField()
    razon_aplica_adecuaciones = models.CharField(max_length=100, blank=True)
    materiales_discapacidad = models.NullBooleanField()
    razon_no_materiales_discapacidad = models.CharField(max_length=100, blank=True)
    eliminada = models.BooleanField()
    bloqueada = models.BooleanField()
    director_distrital = models.ForeignKey('EeDirectoresDistritales', blank=True, null=True)
    advertencias = models.NullBooleanField()
    justificacion_advertencias = models.CharField(max_length=100, blank=True)
    no_acuerdo_creacion = models.CharField(max_length=12, blank=True)
    fecha_acuerdo_creacion = models.DateTimeField(blank=True, null=True)
    num_aeco = models.CharField(max_length=50, blank=True)
    tipo_acuerdo = models.ForeignKey('EeTiposAcuerdo', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_boletas'

class EeBoletasAdultos(models.Model):
    id = models.ForeignKey(EeBoletas, db_column='id', primary_key=True)
    otro_tipo_centro = models.CharField(max_length=50, blank=True)
    otro_tipo_organizacion = models.CharField(max_length=50, blank=True)
    docentes_un_nivel_femenino = models.IntegerField(blank=True, null=True)
    docentes_un_nivel_masculino = models.IntegerField(blank=True, null=True)
    docentes_mas_niveles_femenino = models.IntegerField(blank=True, null=True)
    docentes_mas_niveles_masculino = models.IntegerField(blank=True, null=True)
    docentes_clases_especiales_femenino = models.IntegerField(blank=True, null=True)
    docentes_clases_especiales_masculino = models.IntegerField(blank=True, null=True)
    docentes_sin_nivel_femenino = models.IntegerField(blank=True, null=True)
    docentes_sin_nivel_masculino = models.IntegerField(blank=True, null=True)
    embarazos_men_10 = models.CharField(max_length=3, blank=True)
    embarazos_10_12 = models.CharField(max_length=3, blank=True)
    embarazos_12_14 = models.CharField(max_length=3, blank=True)
    embarazos_14_16 = models.CharField(max_length=3, blank=True)
    embarazos_16_18 = models.CharField(max_length=3, blank=True)
    embarazos_may_18 = models.CharField(max_length=3, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_boletas_adultos'

class EeBoletasBasica(models.Model):
    id = models.ForeignKey(EeBoletas, db_column='id', primary_key=True)
    tipo_docentes = models.ForeignKey('EeTipoDocentes', blank=True, null=True)
    pueblo_etnico = models.ForeignKey('EePueblosEtnicos', blank=True, null=True)
    otros_programas = models.CharField(max_length=50, blank=True)
    secciones_un_grado = models.IntegerField(blank=True, null=True)
    secciones_varios_grados = models.IntegerField(blank=True, null=True)
    ingresos_con_preparatoria_f = models.IntegerField(blank=True, null=True)
    ingresos_con_preparatoria_m = models.IntegerField(blank=True, null=True)
    ingresos_sin_preparatoria_f = models.IntegerField(blank=True, null=True)
    ingresos_sin_preparatoria_m = models.IntegerField(blank=True, null=True)
    otros_recursos_discapacitados = models.CharField(max_length=200, blank=True)
    numero_chorti = models.IntegerField(blank=True, null=True)
    numero_lenca = models.IntegerField(blank=True, null=True)
    numero_garifuna = models.IntegerField(blank=True, null=True)
    numero_tolupan = models.IntegerField(blank=True, null=True)
    numero_isleno = models.IntegerField(blank=True, null=True)
    numero_tawahka = models.IntegerField(blank=True, null=True)
    numero_pech = models.IntegerField(blank=True, null=True)
    numero_misquito = models.IntegerField(blank=True, null=True)
    numero_nahua = models.IntegerField(blank=True, null=True)
    docentes_primer_grado = models.CharField(max_length=2, blank=True)
    docentes_segundo_grado = models.CharField(max_length=2, blank=True)
    docentes_tercer_grado = models.CharField(max_length=2, blank=True)
    docentes_cuarto_grado = models.CharField(max_length=2, blank=True)
    docentes_quinto_grado = models.CharField(max_length=2, blank=True)
    docentes_sexto_grado = models.CharField(max_length=2, blank=True)
    embarazos_men_10 = models.CharField(max_length=3, blank=True)
    embarazos_10_12 = models.CharField(max_length=3, blank=True)
    embarazos_12_14 = models.CharField(max_length=3, blank=True)
    embarazos_14_16 = models.CharField(max_length=3, blank=True)
    embarazos_16_18 = models.CharField(max_length=3, blank=True)
    embarazos_may_18 = models.CharField(max_length=3, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_boletas_basica'

class EeBoletasCcepreb(models.Model):
    id = models.ForeignKey(EeBoletas, db_column='id', primary_key=True)
    ccepreb_grado_educador = models.ForeignKey('EeCceprebGradosEducador', blank=True, null=True)
    obtuvo_titulo_responsable = models.NullBooleanField()
    titulo_responsable = models.CharField(max_length=50, blank=True)
    mes_inicio = models.IntegerField(blank=True, null=True)
    anio_inicio = models.IntegerField(blank=True, null=True)
    ccepreb_local = models.ForeignKey('EeCceprebLocales', blank=True, null=True)
    escuela_donde_funciona = models.CharField(max_length=255, blank=True)
    ccepreb_patrocinador = models.ForeignKey('EeCceprebPatrocinadores', blank=True, null=True)
    otro_patrocinador = models.CharField(max_length=100, blank=True)
    recibe_merienda_escolar = models.NullBooleanField()
    cambio_direccion = models.NullBooleanField()
    direccion_anterior = models.CharField(max_length=255, blank=True)
    otros_recursos_discapacitados = models.CharField(max_length=200, blank=True)
    tiene_paquete_metodologico = models.NullBooleanField()
    tiene_guia_metodologica = models.NullBooleanField()
    tiene_mobiliario = models.NullBooleanField()
    tiene_material_fungible = models.NullBooleanField()
    estado_paquete_metodologico = models.CharField(max_length=10, blank=True)
    jornada = models.CharField(max_length=10, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_boletas_ccepreb'

class EeBoletasMedia(models.Model):
    id = models.ForeignKey(EeBoletas, db_column='id', primary_key=True)
    otro_tipo_centro = models.CharField(max_length=30, blank=True)
    otras_organizaciones = models.CharField(max_length=50, blank=True)
    otros_programas = models.CharField(max_length=150, blank=True)
    modalidad_director = models.CharField(max_length=255, blank=True)
    modalidad_secretario = models.CharField(max_length=255, blank=True)
    modalidad_coordinador = models.CharField(max_length=255, blank=True)
    otras_organizaciones_iher = models.CharField(max_length=1000, blank=True)
    embarazos_men_10 = models.CharField(max_length=3, blank=True)
    embarazos_10_12 = models.CharField(max_length=3, blank=True)
    embarazos_12_14 = models.CharField(max_length=3, blank=True)
    embarazos_14_16 = models.CharField(max_length=3, blank=True)
    embarazos_16_18 = models.CharField(max_length=3, blank=True)
    embarazos_may_18 = models.CharField(max_length=3, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_boletas_media'

class EeBoletasPrebasica(models.Model):
    id = models.ForeignKey(EeBoletas, db_column='id', primary_key=True)
    tipo_docentes = models.ForeignKey('EeTipoDocentes', blank=True, null=True)
    pueblo_etnico = models.ForeignKey('EePueblosEtnicos', blank=True, null=True)
    otros_programas = models.CharField(max_length=50, blank=True)
    numero_secciones_prekinder = models.IntegerField(blank=True, null=True)
    numero_secciones_kinder = models.IntegerField(blank=True, null=True)
    numero_secciones_preparatoria = models.IntegerField(blank=True, null=True)
    numero_secciones_multiples = models.IntegerField(blank=True, null=True)
    docentes_prekinder_femenino = models.IntegerField(blank=True, null=True)
    docentes_prekinder_masculino = models.IntegerField(blank=True, null=True)
    docentes_kinder_femenino = models.IntegerField(blank=True, null=True)
    docentes_kinder_masculino = models.IntegerField(blank=True, null=True)
    docentes_preparatoria_femenino = models.IntegerField(blank=True, null=True)
    docentes_preparatoria_masculino = models.IntegerField(blank=True, null=True)
    otros_recursos_discapacitados = models.CharField(max_length=200, blank=True)
    numero_chorti = models.IntegerField(blank=True, null=True)
    numero_lenca = models.IntegerField(blank=True, null=True)
    numero_garifuna = models.IntegerField(blank=True, null=True)
    numero_tolupan = models.IntegerField(blank=True, null=True)
    numero_isleno = models.IntegerField(blank=True, null=True)
    numero_tawahka = models.IntegerField(blank=True, null=True)
    numero_pech = models.IntegerField(blank=True, null=True)
    numero_misquito = models.IntegerField(blank=True, null=True)
    numero_nahua = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_boletas_prebasica'

class EeCargos(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion_cargo = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_cargos'

class EeCaserios(models.Model):
    aldea = models.ForeignKey(EeAldeas)
    codigo_departamento = models.CharField(max_length=2, blank=True)
    codigo_municipio = models.CharField(max_length=2, blank=True)
    codigo_aldea = models.CharField(max_length=2, blank=True)
    codigo_caserio = models.CharField(max_length=3, blank=True)
    descripcion_caserio = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_caserios'

class EeCceprebEstadisticaFinal(models.Model):
    boleta = models.ForeignKey(EeBoletasCcepreb, blank=True, null=True)
    clase_estadistica = models.ForeignKey('EeClasesEstadisticas', blank=True, null=True)
    edad = models.ForeignKey('EeEdades', blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_ccepreb_estadistica_final'

class EeCceprebEstadisticaInicial(models.Model):
    boleta = models.ForeignKey(EeBoletasCcepreb, blank=True, null=True)
    edad = models.ForeignKey('EeEdades', blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_ccepreb_estadistica_inicial'

class EeCceprebEstudiantes(models.Model):
    boleta = models.ForeignKey(EeBoletasCcepreb, blank=True, null=True)
    estudiante = models.ForeignKey('EeEstudiantes', blank=True, null=True)
    edad_anios = models.IntegerField(blank=True, null=True)
    edad_meses = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_ccepreb_estudiantes'

class EeCceprebGradosEducador(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion_grado_educador = models.CharField(max_length=20, blank=True)
    abreviatura_grado_educador = models.CharField(max_length=5, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_ccepreb_grados_educador'

class EeCceprebLocales(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion_local_ccepreb = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_ccepreb_locales'

class EeCceprebPatrocinadores(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_patrocinador = models.CharField(max_length=100, blank=True)
    id_periodo = models.IntegerField(blank=True, null=True)
    periodo = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_ccepreb_patrocinadores'

class EeCentros(models.Model):
    codigo_centro = models.CharField(unique=True, max_length=9)
    nombre_centro = models.CharField(max_length=255, blank=True)
    municipio = models.ForeignKey('EeMunicipios')
    direccion = models.CharField(max_length=255, blank=True)
    telefono_fijo = models.CharField(max_length=10, blank=True)
    telefono_comunitario_celular = models.CharField(max_length=12, blank=True)
    correo_electronico = models.CharField(max_length=255, blank=True)
    en_funcionamiento = models.BooleanField()
    inicio_funcionamiento = models.IntegerField(blank=True, null=True)
    motivo_cierre = models.CharField(max_length=25, blank=True)
    cambio_nombre = models.BooleanField()
    nombre_anterior = models.CharField(max_length=255, blank=True)
    fecha_cambio_nombre = models.DateTimeField(blank=True, null=True)
    acuerdo_cambio_nombre = models.CharField(max_length=20, blank=True)
    tipo_administracion = models.ForeignKey('EeTiposAdministracion', blank=True, null=True)
    tipo_zona = models.ForeignKey('EeTiposZona', blank=True, null=True)
    pais_frontera = models.ForeignKey('EePaisFrontera', blank=True, null=True)
    distancia = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tipo_docentes = models.ForeignKey('EeTipoDocentes', blank=True, null=True)
    tipo_centro = models.ForeignKey('EeTiposCentro', blank=True, null=True)
    periodo_escolar = models.CharField(max_length=1, blank=True)
    pueblo_etnico = models.ForeignKey('EePueblosEtnicos', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_centros'

class EeCentrosEliminados(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo_centro = models.CharField(max_length=9)
    nombre_centro = models.CharField(max_length=255, blank=True)
    municipio_id = models.IntegerField()
    direccion = models.CharField(max_length=255, blank=True)
    telefono_fijo = models.CharField(max_length=10, blank=True)
    telefono_comunitario_celular = models.CharField(max_length=12, blank=True)
    correo_electronico = models.CharField(max_length=255, blank=True)
    en_funcionamiento = models.BooleanField()
    inicio_funcionamiento = models.IntegerField(blank=True, null=True)
    motivo_cierre = models.CharField(max_length=25, blank=True)
    cambio_nombre = models.BooleanField()
    nombre_anterior = models.CharField(max_length=255, blank=True)
    fecha_cambio_nombre = models.DateTimeField(blank=True, null=True)
    acuerdo_cambio_nombre = models.CharField(max_length=20, blank=True)
    tipo_administracion_id = models.IntegerField(blank=True, null=True)
    tipo_zona_id = models.IntegerField(blank=True, null=True)
    pais_frontera_id = models.IntegerField(blank=True, null=True)
    distancia = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tipo_docentes_id = models.IntegerField(blank=True, null=True)
    tipo_centro_id = models.IntegerField(blank=True, null=True)
    periodo_escolar = models.CharField(max_length=1, blank=True)
    pueblo_etnico_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_centros_eliminados'

class EeCentrosRedesEducativas(models.Model):
    periodo = models.ForeignKey('EePeriodos', blank=True, null=True)
    red = models.ForeignKey('EeRedesEducativas', blank=True, null=True)
    centro = models.ForeignKey(EeCentros, blank=True, null=True)
    es_sede = models.NullBooleanField()
    distancia_sede = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    distancia_proximo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    posee_personeria_juridica = models.NullBooleanField()
    personeria_juridica = models.CharField(max_length=24, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_centros_redes_educativas'

class EeClasesAreas(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion_clase = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_clases_areas'

class EeClasesEspeciales(models.Model):
    ordenamiento_clase = models.IntegerField(blank=True, null=True)
    descripcion_clase = models.CharField(max_length=50, blank=True)
    solo_basica = models.NullBooleanField()
    descripcion_clase_bilingue = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_clases_especiales'

class EeClasesEstadisticas(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion_clase_estadistica = models.CharField(max_length=25, blank=True)
    es_final = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'ee_clases_estadisticas'

class EeContadoresVisitas(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion_reporte = models.CharField(max_length=100, blank=True)
    visitas_externas = models.IntegerField(blank=True, null=True)
    visitas_internas = models.IntegerField(blank=True, null=True)
    descargas_externas = models.IntegerField(blank=True, null=True)
    descargas_internas = models.IntegerField(blank=True, null=True)
    fecha_ultima_visita = models.DateTimeField(blank=True, null=True)
    fecha_ultima_descarga = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_contadores_visitas'

class EeCoordenadasMunicipios(models.Model):
    municipio = models.ForeignKey('EeMunicipios', primary_key=True)
    codigo_departamento = models.CharField(max_length=2)
    codigo_municipio = models.CharField(max_length=2)
    c_x = models.FloatField(blank=True, null=True)
    c_y = models.FloatField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_coordenadas_municipios'

class EeDepartamentos(models.Model):
    codigo_departamento = models.CharField(max_length=2, blank=True)
    descripcion_departamento = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_departamentos'

class EeDireccionesDistritales(models.Model):
    departamento = models.ForeignKey(EeDepartamentos, blank=True, null=True)
    es_municipal = models.NullBooleanField()
    numero_direccion = models.IntegerField(blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_direcciones_distritales'

class EeDirectores(models.Model):
    identidad_director = models.CharField(max_length=13, blank=True)
    nombre_completo_director = models.CharField(max_length=150, blank=True)
    sexo_director = models.CharField(max_length=1, blank=True)
    es_extranjero_director = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'ee_directores'

class EeDirectoresDistritales(models.Model):
    direccion_distrital = models.ForeignKey(EeDireccionesDistritales, blank=True, null=True)
    nombre_completo = models.CharField(max_length=150, blank=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_directores_distritales'

class EeDiscapacidades(models.Model):
    ordenamiento_discapacidad = models.IntegerField(blank=True, null=True)
    descripcion_discapacidad = models.CharField(max_length=40, blank=True)
    es_discapacidad = models.NullBooleanField()
    incluir_prebasica = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'ee_discapacidades'

class EeEdades(models.Model):
    id = models.IntegerField(primary_key=True)
    ordenamiento_edad = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    descripcion_edad = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_edades'

class EeEdadesTiposBoleta(models.Model):
    edad = models.ForeignKey(EeEdades)
    tipo_boleta = models.ForeignKey('EeTiposBoleta')
    aparece_inicial = models.IntegerField()
    aparece_final = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'ee_edades_tipos_boleta'

class EeElementosAula(models.Model):
    descripcion_elemento = models.CharField(max_length=30, blank=True)
    aparece_prebasica = models.NullBooleanField()
    aparece_basica = models.NullBooleanField()
    aparece_media = models.NullBooleanField()
    ordenamiento = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_elementos_aula'

class EeElementosInstalacion(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion_elemento = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_elementos_instalacion'

class EeEstadisticasAulas(models.Model):
    infraestructura = models.ForeignKey('EeInfraestructuras', blank=True, null=True)
    elemento_aula = models.ForeignKey(EeElementosAula, blank=True, null=True)
    grado = models.ForeignKey('EeGrados', blank=True, null=True)
    cantidad_buenas = models.IntegerField(blank=True, null=True)
    cantidad_regulares = models.IntegerField(blank=True, null=True)
    cantidad_malas = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_estadisticas_aulas'

class EeEstadisticasClasesEspeciales(models.Model):
    boleta = models.ForeignKey(EeBoletas, blank=True, null=True)
    profesionalizacion_docente = models.ForeignKey('EeProfesionalizacionDocente', blank=True, null=True)
    clase = models.ForeignKey(EeClasesEspeciales, blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_estadisticas_clases_especiales'

class EeEstadisticasDiscapacitados(models.Model):
    boleta = models.ForeignKey(EeBoletas, blank=True, null=True)
    grado = models.ForeignKey('EeGrados', blank=True, null=True)
    discapacidad = models.ForeignKey(EeDiscapacidades, blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_estadisticas_discapacitados'

class EeEstadisticasDiscapacitadosCcepreb(models.Model):
    boleta = models.ForeignKey(EeBoletasCcepreb, blank=True, null=True)
    edad = models.ForeignKey(EeEdades, blank=True, null=True)
    discapacidad = models.ForeignKey(EeDiscapacidades, blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_estadisticas_discapacitados_ccepreb'

class EeEstadisticasDocentes(models.Model):
    boleta = models.ForeignKey(EeBoletas, blank=True, null=True)
    funcion_docente = models.ForeignKey('EeFuncionesDocentes', blank=True, null=True)
    profesionalizacion_docente = models.ForeignKey('EeProfesionalizacionDocente', blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_estadisticas_docentes'

class EeEstudiantes(models.Model):
    identidad_estudiante = models.CharField(max_length=13, blank=True)
    nombre_completo_estudiante = models.CharField(max_length=100, blank=True)
    sexo_estudiante = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_estudiantes'

class EeFormaServicio(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_forma_servicios = models.CharField(max_length=20, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_forma_servicio'

class EeFuncionesDocentes(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo_boleta = models.ForeignKey('EeTiposBoleta', blank=True, null=True)
    cargo = models.ForeignKey(EeCargos, blank=True, null=True)
    ordenamiento_funcion = models.IntegerField(blank=True, null=True)
    grados_funcion = models.IntegerField(blank=True, null=True)
    descripcion_funcion_docente = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_funciones_docentes'

class EeGrados(models.Model):
    tipo_boleta = models.ForeignKey('EeTiposBoleta', blank=True, null=True)
    codigo_grado = models.IntegerField(blank=True, null=True)
    abreviatura_grado = models.CharField(max_length=5, blank=True)
    descripcion_grado = models.CharField(max_length=20, blank=True)
    ordenamiento_grado = models.IntegerField(blank=True, null=True)
    mg_grados_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_grados'

class EeInfraestructuraInstalaciones(models.Model):
    infraestructura = models.ForeignKey('EeInfraestructuras', blank=True, null=True)
    instalacion = models.ForeignKey('EeInstalaciones', blank=True, null=True)
    cantidad_buenas = models.IntegerField(blank=True, null=True)
    cantidad_regulares = models.IntegerField(blank=True, null=True)
    cantidad_malas = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_infraestructura_instalaciones'

class EeInfraestructuraInstalacionesEspeciales(models.Model):
    infraestructura = models.ForeignKey('EeInfraestructuras', blank=True, null=True)
    instalacion_especial = models.ForeignKey('EeInstalacionesEspeciales', blank=True, null=True)
    elemento_instalacion = models.ForeignKey(EeElementosInstalacion, blank=True, null=True)
    cantidad_buenas = models.IntegerField(blank=True, null=True)
    cantidad_regulares = models.IntegerField(blank=True, null=True)
    cantidad_malas = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_infraestructura_instalaciones_especiales'

class EeInfraestructuras(models.Model):
    material_paredes = models.ForeignKey('EeMateriales', db_column='material_paredes', blank=True, null=True)
    otro_material_paredes = models.CharField(max_length=20, blank=True)
    material_arteson = models.ForeignKey('EeMateriales', db_column='material_arteson', blank=True, null=True)
    material_ventanas = models.ForeignKey('EeMateriales', db_column='material_ventanas', blank=True, null=True)
    tipo_agua = models.ForeignKey('EeTipoAgua', blank=True, null=True)
    otra_fuente_agua = models.CharField(max_length=20, blank=True)
    almacenamiento_agua = models.ForeignKey(EeAlmacenamientoAgua, blank=True, null=True)
    otro_almacenamiento_agua = models.CharField(max_length=20, blank=True)
    suministro_electricidad = models.ForeignKey('EeSuministrosElectricidad', blank=True, null=True)
    otro_suministro_electricidad = models.CharField(max_length=20, blank=True)
    pc_para_alumnos = models.IntegerField(blank=True, null=True)
    pc_para_maestros = models.IntegerField(blank=True, null=True)
    pc_para_personal_administrativo = models.IntegerField(blank=True, null=True)
    tiene_radio = models.NullBooleanField()
    tiene_television = models.NullBooleanField()
    tiene_multimedia = models.NullBooleanField()
    tiene_internet = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'ee_infraestructuras'

class EeInstalaciones(models.Model):
    ordenamiento_instalacion = models.IntegerField(blank=True, null=True)
    descripcion_instalacion = models.CharField(max_length=30, blank=True)
    es_sanitaria = models.NullBooleanField()
    excluir_basica = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'ee_instalaciones'

class EeInstalacionesEspeciales(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion_instalacion = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_instalaciones_especiales'

class EeInstalacionesSanitarias(models.Model):
    infraestructura = models.ForeignKey(EeInfraestructuras, blank=True, null=True)
    instalacion = models.ForeignKey(EeInstalaciones, blank=True, null=True)
    para_docentes = models.CharField(max_length=1, blank=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_instalaciones_sanitarias'

class EeJornadasLaborales(models.Model):
    id = models.IntegerField(primary_key=True)
    ordenamiento_jornada = models.IntegerField(blank=True, null=True)
    descripcion_jornada_laboral = models.CharField(max_length=20, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_jornadas_laborales'

class EeMateriales(models.Model):
    id = models.IntegerField(primary_key=True)
    subtipo_material = models.IntegerField(blank=True, null=True)
    descripcion_material = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_materiales'

class EeMediaDocentesFormaServicio(models.Model):
    boleta = models.ForeignKey(EeBoletasMedia, blank=True, null=True)
    forma_servicio = models.ForeignKey(EeFormaServicio, blank=True, null=True)
    cantidad_femenino = models.IntegerField(blank=True, null=True)
    cantidad_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_media_docentes_forma_servicio'

class EeMediaEstadisticaClases(models.Model):
    boleta = models.ForeignKey(EeBoletasMedia, blank=True, null=True)
    grado = models.ForeignKey(EeGrados, blank=True, null=True)
    clase = models.ForeignKey(EeClasesAreas, blank=True, null=True)
    aprobados_femenino = models.IntegerField(blank=True, null=True)
    aprobados_masculino = models.IntegerField(blank=True, null=True)
    reprobados_femenino = models.IntegerField(blank=True, null=True)
    reprobados_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_media_estadistica_clases'

class EeMediaEstadisticaDocentesJornadas(models.Model):
    boleta = models.ForeignKey(EeBoletasMedia, blank=True, null=True)
    funcion_docente = models.ForeignKey(EeFuncionesDocentes, blank=True, null=True)
    jornada_laboral = models.ForeignKey(EeJornadasLaborales, blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_media_estadistica_docentes_jornadas'

class EeMediaEstadisticaFinal(models.Model):
    seccion = models.ForeignKey('EeMediaSeccionesEstadisticaFinal', blank=True, null=True)
    clase_estadistica = models.ForeignKey(EeClasesEstadisticas, blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_media_estadistica_final'

class EeMediaEstadisticaInicial(models.Model):
    seccion = models.ForeignKey('EeMediaSeccionesEstadisticaInicial', blank=True, null=True)
    edad = models.ForeignKey(EeEdades, blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_media_estadistica_inicial'

class EeMediaEstadisticaInicialTrabajoInfantil(models.Model):
    boleta = models.ForeignKey(EeBoletasMedia, blank=True, null=True)
    jornada = models.CharField(max_length=1, blank=True)
    repitentes = models.CharField(max_length=1, blank=True)
    grado = models.ForeignKey(EeGrados, blank=True, null=True)
    edad = models.ForeignKey(EeEdades, blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_media_estadistica_inicial_trabajo_infantil'

class EeMediaFormasServicio(models.Model):
    boleta = models.ForeignKey(EeBoletasMedia)
    forma_servicio = models.ForeignKey(EeFormaServicio)
    class Meta:
        managed = False
        db_table = 'ee_media_formas_servicio'

class EeMediaSeccionesEstadisticaFinal(models.Model):
    boleta = models.ForeignKey(EeBoletasMedia, blank=True, null=True)
    grado = models.ForeignKey(EeGrados, blank=True, null=True)
    modalidad = models.ForeignKey('EeModalidades', blank=True, null=True)
    forma_servicio = models.ForeignKey(EeFormaServicio, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_media_secciones_estadistica_final'

class EeMediaSeccionesEstadisticaInicial(models.Model):
    boleta = models.ForeignKey(EeBoletasMedia, blank=True, null=True)
    forma_servicio = models.ForeignKey(EeFormaServicio, blank=True, null=True)
    repitentes = models.CharField(max_length=1, blank=True)
    grado = models.ForeignKey(EeGrados, blank=True, null=True)
    modalidad = models.ForeignKey('EeModalidades', blank=True, null=True)
    seccion = models.CharField(max_length=3, blank=True)
    jornada = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_media_secciones_estadistica_inicial'

class EeModalidades(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion_modalidad = models.CharField(max_length=120, blank=True)
    nivel_academico = models.CharField(max_length=1, blank=True)
    duracion = models.IntegerField(blank=True, null=True)
    acuerdo_creacion = models.CharField(max_length=15, blank=True)
    activa = models.NullBooleanField()
    idmodalidad = models.IntegerField(blank=True, null=True)
    eliminado = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_modalidades'

class EeModalidadesBak(models.Model):
    id = models.IntegerField()
    descripcion_modalidad = models.CharField(max_length=120, blank=True)
    nivel_academico = models.CharField(max_length=1, blank=True)
    duracion = models.IntegerField(blank=True, null=True)
    acuerdo_creacion = models.CharField(max_length=15, blank=True)
    activa = models.NullBooleanField()
    idmodalidad = models.IntegerField(blank=True, null=True)
    eliminado = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_modalidades_bak'

class EeModosCargo(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion_modo_cargo = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_modos_cargo'

class EeMunicipios(models.Model):
    departamento = models.ForeignKey(EeDepartamentos)
    codigo_departamento = models.CharField(max_length=2, blank=True)
    codigo_municipio = models.CharField(max_length=2, blank=True)
    descripcion_municipio = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_municipios'

class EeNivelesResumenes(models.Model):
    nivel_educativo = models.IntegerField()
    descripcion = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'ee_niveles_resumenes'

class EeOrganizaciones(models.Model):
    tipo_boleta_id = models.IntegerField(blank=True, null=True)
    codigo_organizacion = models.IntegerField(blank=True, null=True)
    descripcion_organizacion = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_organizaciones'

class EePaisFrontera(models.Model):
    id = models.IntegerField(primary_key=True)
    abreviatura = models.CharField(max_length=1, blank=True)
    pais_frontera = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_pais_frontera'

class EePerfiles(models.Model):
    nombre_perfil = models.CharField(max_length=25, blank=True)
    descripcion_perfil = models.CharField(max_length=255, blank=True)
    oculto = models.NullBooleanField()
    habilitado = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'ee_perfiles'

class EePerfilesUsuario(models.Model):
    perfil = models.ForeignKey(EePerfiles)
    usuario = models.ForeignKey('EeUsuarios')
    class Meta:
        managed = False
        db_table = 'ee_perfiles_usuario'

class EePeriodos(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion_periodo = models.CharField(max_length=30, blank=True)
    bloqueado_ingreso = models.NullBooleanField()
    consultable_inicial = models.NullBooleanField()
    consultable_final = models.NullBooleanField()
    offset_boletas = models.IntegerField(blank=True, null=True)
    previo_requerido = models.NullBooleanField()
    fecha_maximo_normal = models.CharField(max_length=20, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_periodos'

class EePermisos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_permiso = models.CharField(max_length=50, blank=True)
    descripcion_permiso = models.CharField(max_length=255, blank=True)
    oculto = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'ee_permisos'

class EePermisosPerfil(models.Model):
    perfil = models.ForeignKey(EePerfiles)
    permiso = models.ForeignKey(EePermisos)
    class Meta:
        managed = False
        db_table = 'ee_permisos_perfil'

class EePrebasicaEstadisticaFinal(models.Model):
    boleta = models.ForeignKey(EeBoletasPrebasica, blank=True, null=True)
    grado = models.ForeignKey(EeGrados, blank=True, null=True)
    clase_estadistica = models.ForeignKey(EeClasesEstadisticas, blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_prebasica_estadistica_final'

class EePrebasicaEstadisticaInicial(models.Model):
    boleta = models.ForeignKey(EeBoletasPrebasica, blank=True, null=True)
    grado = models.ForeignKey(EeGrados, blank=True, null=True)
    jornada = models.CharField(max_length=1, blank=True)
    edad = models.ForeignKey(EeEdades, blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_prebasica_estadistica_inicial'

class EeProfesionalizacionDocente(models.Model):
    id = models.IntegerField(primary_key=True)
    ordenamiento_profesionalizacion = models.IntegerField(blank=True, null=True)
    con_titulo = models.NullBooleanField()
    nivel_titulo = models.CharField(max_length=100, blank=True)
    descripcion_profesionalizacion = models.CharField(max_length=100, blank=True)
    solo_media = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'ee_profesionalizacion_docente'

class EeProgramas(models.Model):
    tipo_boleta = models.ForeignKey('EeTiposBoleta', blank=True, null=True)
    codigo_programa = models.IntegerField(blank=True, null=True)
    descripcion_programa = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_programas'

class EePueblosEtnicos(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion_pueblo_etnico = models.CharField(max_length=20, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_pueblos_etnicos'

class EeRecursosDiscapacitados(models.Model):
    ordenamiento_recurso = models.IntegerField(blank=True, null=True)
    descripcion_recurso = models.CharField(max_length=80, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_recursos_discapacitados'

class EeRedesEducativas(models.Model):
    municipio = models.ForeignKey(EeMunicipios, blank=True, null=True)
    codigo_red = models.CharField(max_length=8, blank=True)
    nombre_red = models.CharField(max_length=255, blank=True)
    anio_creacion = models.IntegerField(blank=True, null=True)
    posee_personeria_juridica = models.NullBooleanField()
    personeria_juridica = models.CharField(max_length=24, blank=True)
    en_funcionamiento = models.NullBooleanField()
    razon_no_funcionamiento = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_redes_educativas'

class EeResumenClases(models.Model):
    periodo_id = models.IntegerField()
    nivel_educativo = models.IntegerField()
    departamento_id = models.IntegerField()
    municipio_id = models.IntegerField()
    grado_id = models.IntegerField(blank=True, null=True)
    clase_id = models.IntegerField(blank=True, null=True)
    aprobados_femenino = models.IntegerField(blank=True, null=True)
    aprobados_masculino = models.IntegerField(blank=True, null=True)
    reprobados_femenino = models.IntegerField(blank=True, null=True)
    reprobados_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_resumen_clases'

class EeResumenDiscapacitados(models.Model):
    periodo_id = models.IntegerField()
    nivel_educativo = models.IntegerField(blank=True, null=True)
    departamento_id = models.IntegerField()
    municipio_id = models.IntegerField()
    tipo_administracion_id = models.IntegerField(blank=True, null=True)
    fila_id = models.IntegerField(blank=True, null=True)
    discapacidad_id = models.IntegerField(blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_resumen_discapacitados'

class EeResumenDocentes(models.Model):
    periodo_id = models.IntegerField()
    departamento_id = models.IntegerField()
    municipio_id = models.IntegerField()
    centro_id = models.IntegerField()
    nivel_educativo = models.IntegerField(blank=True, null=True)
    tipo_administracion_id = models.IntegerField(blank=True, null=True)
    tipo_zona_id = models.IntegerField(blank=True, null=True)
    boleta_id = models.IntegerField(blank=True, null=True)
    total_f = models.IntegerField(blank=True, null=True)
    total_m = models.IntegerField(blank=True, null=True)
    bloqueada = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'ee_resumen_docentes'

class EeResumenMatriculaBoletas(models.Model):
    periodo_id = models.IntegerField()
    departamento_id = models.IntegerField()
    municipio_id = models.IntegerField()
    centro_id = models.IntegerField()
    nivel_educativo = models.IntegerField(blank=True, null=True)
    tipo_administracion_id = models.IntegerField(blank=True, null=True)
    tipo_zona_id = models.IntegerField(blank=True, null=True)
    boleta_id = models.IntegerField(blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    bloqueada = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'ee_resumen_matricula_boletas'

class EeResumenMatriculaFinal(models.Model):
    periodo_id = models.IntegerField()
    departamento_id = models.IntegerField()
    municipio_id = models.IntegerField()
    centro_id = models.IntegerField()
    tipo_administracion_id = models.IntegerField(blank=True, null=True)
    tipo_zona_id = models.IntegerField(blank=True, null=True)
    boleta_id = models.IntegerField(blank=True, null=True)
    nivel_educativo = models.IntegerField()
    clase_estadistica_id = models.IntegerField(blank=True, null=True)
    grado_id = models.IntegerField(blank=True, null=True)
    edad_id = models.IntegerField(blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_resumen_matricula_final'

class EeResumenMatriculaInicial(models.Model):
    periodo_id = models.IntegerField()
    departamento_id = models.IntegerField()
    municipio_id = models.IntegerField()
    centro_id = models.IntegerField()
    tipo_administracion_id = models.IntegerField(blank=True, null=True)
    tipo_zona_id = models.IntegerField(blank=True, null=True)
    boleta_id = models.IntegerField(blank=True, null=True)
    nivel_educativo = models.IntegerField()
    jornada = models.CharField(max_length=2, blank=True)
    grado_id = models.IntegerField(blank=True, null=True)
    edad_id = models.IntegerField(blank=True, null=True)
    repitentes = models.CharField(max_length=1, blank=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_resumen_matricula_inicial'

class EeResumenMediaInicial(models.Model):
    periodo_id = models.IntegerField()
    departamento_id = models.IntegerField()
    municipio_id = models.IntegerField()
    centro_id = models.IntegerField()
    boleta_id = models.IntegerField(blank=True, null=True)
    forma_servicio_id = models.IntegerField(blank=True, null=True)
    modalidad_id = models.IntegerField(blank=True, null=True)
    grado_id = models.IntegerField(blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_resumen_media_inicial'

class EeResumenNombres(models.Model):
    valor = models.CharField(max_length=50, blank=True)
    f_0 = models.IntegerField(db_column='F_0', blank=True, null=True) # Field name made lowercase.
    m_0 = models.IntegerField(db_column='M_0', blank=True, null=True) # Field name made lowercase.
    f_1 = models.IntegerField(db_column='F_1', blank=True, null=True) # Field name made lowercase.
    m_1 = models.IntegerField(db_column='M_1', blank=True, null=True) # Field name made lowercase.
    total = models.IntegerField(blank=True, null=True)
    p_f_0 = models.DecimalField(db_column='P_F_0', max_digits=18, decimal_places=15, blank=True, null=True) # Field name made lowercase.
    p_m_0 = models.DecimalField(db_column='P_M_0', max_digits=18, decimal_places=15, blank=True, null=True) # Field name made lowercase.
    p_u_1 = models.DecimalField(db_column='P_U_1', max_digits=18, decimal_places=15, blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ee_resumen_nombres'

class EeResumenProbabilidadesValores(models.Model):
    tabla = models.CharField(max_length=32)
    fila_id = models.IntegerField()
    columna_id = models.IntegerField()
    minimo = models.FloatField(blank=True, null=True)
    maximo = models.FloatField(blank=True, null=True)
    promedio = models.FloatField(blank=True, null=True)
    desviacion = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_resumen_probabilidades_valores'

class EeResumenUbicaciones(models.Model):
    valor = models.CharField(max_length=100, blank=True)
    aldeas = models.IntegerField(blank=True, null=True)
    caserios = models.IntegerField(blank=True, null=True)
    barrios = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_resumen_ubicaciones'

class EeSuministrosElectricidad(models.Model):
    descripcion_suministro = models.CharField(max_length=20, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_suministros_electricidad'

class EeTablasResumen(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_resumen = models.CharField(max_length=50, blank=True)
    nombre_tabla = models.CharField(max_length=100, blank=True)
    consulta_generacion = models.CharField(max_length=100, blank=True)
    tiempo_ultima_generacion = models.DateTimeField(blank=True, null=True)
    duracion_minutos = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_tablas_resumen'

class EeTipoAgua(models.Model):
    descripcion_tipo_agua = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_tipo_agua'

class EeTipoDocentes(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion_tipo_docentes = models.CharField(max_length=20, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_tipo_docentes'

class EeTiposAcuerdo(models.Model):
    descripcion_tipo_acuerdo = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_tipos_acuerdo'

class EeTiposAdministracion(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion_tipo_administracion = models.CharField(max_length=25, blank=True)
    sector_cine97 = models.CharField(max_length=15, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_tipos_administracion'

class EeTiposAdministracionTiposBoleta(models.Model):
    tipo_boleta = models.ForeignKey('EeTiposBoleta')
    tipo_administracion = models.ForeignKey(EeTiposAdministracion)
    codigo_tipo_administracion = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_tipos_administracion_tipos_boleta'

class EeTiposBoleta(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo_boleta = models.CharField(max_length=20, blank=True)
    descripcion_boleta = models.CharField(max_length=50, blank=True)
    plantilla_agregar = models.CharField(max_length=50, blank=True)
    plantilla_modificar = models.CharField(max_length=50, blank=True)
    plantilla_mostrar = models.CharField(max_length=50, blank=True)
    plantilla_eliminar = models.CharField(max_length=50, blank=True)
    prefijo = models.CharField(max_length=50, blank=True)
    cuenta_paginas = models.IntegerField(blank=True, null=True)
    tabla_bitacora = models.ForeignKey(EeBitacoraTablas, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_tipos_boleta'

class EeTiposCentro(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion_tipo_centro = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_tipos_centro'

class EeTiposCentroTiposBoleta(models.Model):
    tipo_boleta = models.ForeignKey(EeTiposBoleta)
    tipo_centro = models.ForeignKey(EeTiposCentro)
    codigo_tipo_centro = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_tipos_centro_tipos_boleta'

class EeTiposZona(models.Model):
    tipo_zona = models.CharField(max_length=2, blank=True)
    descripcion_tipo_zona = models.CharField(max_length=15, blank=True)
    class Meta:
        managed = False
        db_table = 'ee_tipos_zona'

class EeUbicacionesUsuarios(models.Model):
    descripcion_ubicacion = models.CharField(max_length=50, blank=True)
    departamento = models.ForeignKey(EeDepartamentos, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_ubicaciones_usuarios'

class EeUsuarios(models.Model):
    usuario = models.CharField(max_length=50)
    nombre_usuario = models.CharField(max_length=200, blank=True)
    password = models.CharField(max_length=40)
    correo_electronico = models.CharField(max_length=255, blank=True)
    ubicacion = models.ForeignKey(EeUbicacionesUsuarios, blank=True, null=True)
    fecha_ultima_sesion = models.DateTimeField(blank=True, null=True)
    tiempo_ultimo_rastreo = models.DateTimeField(blank=True, null=True)
    ultimo_cierre_sesion = models.DateTimeField(blank=True, null=True)
    oculto = models.NullBooleanField()
    habilitado = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'ee_usuarios'

class EeVideos(models.Model):
    titulo = models.CharField(max_length=100, blank=True)
    descripcion = models.CharField(max_length=512, blank=True)
    archivo_calidad_baja = models.CharField(max_length=150, blank=True)
    archivo_calidad_media = models.CharField(max_length=150, blank=True)
    archivo_calidad_alta = models.CharField(max_length=150, blank=True)
    visitas = models.IntegerField(blank=True, null=True)
    fecha_subida = models.DateTimeField(blank=True, null=True)
    prefijo_snapshots = models.CharField(max_length=100, blank=True)
    cuenta_snapshots = models.IntegerField(blank=True, null=True)
    eliminado = models.NullBooleanField()
    fecha_ultima_visita = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_videos'

class EeVideosCalificaciones(models.Model):
    video = models.ForeignKey(EeVideos, blank=True, null=True)
    usuario = models.ForeignKey(EeUsuarios, blank=True, null=True)
    calificacion = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_videos_calificaciones'

class EeVideosComentarios(models.Model):
    usuario = models.ForeignKey(EeUsuarios, blank=True, null=True)
    video = models.ForeignKey(EeVideos, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True)
    fecha = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_videos_comentarios'

class EeVideosVisitas(models.Model):
    usuario = models.ForeignKey(EeUsuarios, blank=True, null=True)
    video = models.ForeignKey(EeVideos, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ee_videos_visitas'

class IntoEstadisticasUpeg2012(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    tipo_boleta = models.CharField(max_length=20, blank=True)
    codigo_centro = models.CharField(max_length=9)
    nombre_centro = models.CharField(max_length=255, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    codigo_departamento = models.CharField(max_length=2, blank=True)
    descripcion_departamento = models.CharField(max_length=25, blank=True)
    codigo_municipio = models.CharField(max_length=2, blank=True)
    descripcion_municipio = models.CharField(max_length=255, blank=True)
    descripcion_tipo_administracion = models.CharField(max_length=25, blank=True)
    descripcion_tipo_zona = models.CharField(max_length=15, blank=True)
    periodo_escolar = models.CharField(max_length=1)
    pais_frontera = models.CharField(max_length=25, blank=True)
    distancia = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descripcion_tipo_docentes = models.CharField(max_length=20)
    descripcion_pueblo_etnico = models.CharField(max_length=20, blank=True)
    descripcion_tipo_centro = models.CharField(max_length=25, blank=True)
    telefono = models.CharField(max_length=12, blank=True)
    correo_electronico = models.CharField(max_length=255)
    en_funcionamiento = models.BooleanField()
    motivo_cierre = models.CharField(max_length=25, blank=True)
    funciona_edificio_propio = models.NullBooleanField()
    inicio_funcionamiento = models.IntegerField(blank=True, null=True)
    comparte_edificio = models.NullBooleanField()
    centros_comparte_edificio = models.CharField(max_length=255, blank=True)
    cambio_nombre = models.BooleanField()
    nombre_anterior = models.CharField(max_length=255, blank=True)
    acuerdo_cambio_nombre = models.CharField(max_length=20, blank=True)
    fecha_cambio_nombre = models.DateTimeField(blank=True, null=True)
    identidad_director = models.CharField(max_length=13, blank=True)
    nombre_completo_director = models.CharField(max_length=150, blank=True)
    sexo_director = models.CharField(max_length=1, blank=True)
    es_extranjero_director = models.NullBooleanField()
    descripcion_modo_cargo = models.CharField(max_length=50, blank=True)
    forma_servicios = models.CharField(max_length=20)
    jornada = models.CharField(max_length=2, blank=True)
    modalidad_id = models.IntegerField(blank=True, null=True)
    descripcion_modalidad = models.CharField(max_length=120)
    codigo_grado = models.IntegerField(blank=True, null=True)
    descripcion_grado = models.CharField(max_length=20, blank=True)
    seccion = models.IntegerField(blank=True, null=True)
    descripcion_edad = models.CharField(max_length=25, blank=True)
    repitentes = models.CharField(max_length=1, blank=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    valor_total = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'into_estadisticas_upeg_2012'

class IntoEstadisticasUpeg2013(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    tipo_boleta = models.CharField(max_length=20, blank=True)
    codigo_centro = models.CharField(max_length=9)
    nombre_centro = models.CharField(max_length=255, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    codigo_departamento = models.CharField(max_length=2, blank=True)
    descripcion_departamento = models.CharField(max_length=25, blank=True)
    codigo_municipio = models.CharField(max_length=2, blank=True)
    descripcion_municipio = models.CharField(max_length=255, blank=True)
    descripcion_tipo_administracion = models.CharField(max_length=25, blank=True)
    descripcion_tipo_zona = models.CharField(max_length=15, blank=True)
    periodo_escolar = models.CharField(max_length=1)
    pais_frontera = models.CharField(max_length=25, blank=True)
    distancia = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descripcion_tipo_docentes = models.CharField(max_length=20)
    descripcion_pueblo_etnico = models.CharField(max_length=20, blank=True)
    descripcion_tipo_centro = models.CharField(max_length=25, blank=True)
    telefono = models.CharField(max_length=12, blank=True)
    correo_electronico = models.CharField(max_length=255)
    en_funcionamiento = models.BooleanField()
    motivo_cierre = models.CharField(max_length=25, blank=True)
    funciona_edificio_propio = models.NullBooleanField()
    inicio_funcionamiento = models.IntegerField(blank=True, null=True)
    comparte_edificio = models.NullBooleanField()
    centros_comparte_edificio = models.CharField(max_length=255, blank=True)
    cambio_nombre = models.BooleanField()
    nombre_anterior = models.CharField(max_length=255, blank=True)
    acuerdo_cambio_nombre = models.CharField(max_length=20, blank=True)
    fecha_cambio_nombre = models.DateTimeField(blank=True, null=True)
    identidad_director = models.CharField(max_length=13, blank=True)
    nombre_completo_director = models.CharField(max_length=150, blank=True)
    sexo_director = models.CharField(max_length=1, blank=True)
    es_extranjero_director = models.NullBooleanField()
    descripcion_modo_cargo = models.CharField(max_length=50, blank=True)
    forma_servicios = models.CharField(max_length=20)
    jornada = models.CharField(max_length=2, blank=True)
    modalidad_id = models.IntegerField(blank=True, null=True)
    descripcion_modalidad = models.CharField(max_length=120)
    codigo_grado = models.IntegerField(blank=True, null=True)
    descripcion_grado = models.CharField(max_length=20, blank=True)
    seccion = models.IntegerField(blank=True, null=True)
    descripcion_edad = models.CharField(max_length=25, blank=True)
    repitentes = models.CharField(max_length=1, blank=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    valor_total = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'into_estadisticas_upeg_2013'

class PmaListaConsultas(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=18, decimal_places=0)
    titulo = models.CharField(max_length=150)
    descripcion_consulta = models.CharField(max_length=150)
    qry_principal = models.CharField(max_length=1600)
    qry_departamento = models.CharField(max_length=2500)
    qry_municipio = models.CharField(max_length=200)
    detalle_centro = models.CharField(max_length=1)
    graficar = models.CharField(max_length=1)
    numerador_denominador = models.CharField(max_length=1)
    orden = models.IntegerField()
    cantidad_fechas_qry = models.IntegerField()
    titulo_numerador = models.CharField(max_length=60, blank=True)
    titulo_denominador = models.CharField(max_length=60, blank=True)
    titulo_resultado = models.CharField(max_length=60, blank=True)
    columnas_consulta = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'pma_lista_consultas'

class PpAldeas(models.Model):
    codigo_departamento = models.CharField(max_length=2)
    codigo_municipio = models.CharField(max_length=2)
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

class PpCaserios(models.Model):
    codigo_departamento = models.CharField(max_length=2)
    codigo_municipio = models.CharField(max_length=2)
    codigo_aldea = models.CharField(max_length=5)
    codigo_caserio = models.CharField(max_length=3)
    descripcion_caserio = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_caserios'

class PpColonias(models.Model):
    codigo_departamento = models.CharField(max_length=2)
    codigo_municipio = models.CharField(max_length=2)
    codigo_aldea = models.CharField(max_length=5)
    codigo_colonia = models.CharField(max_length=3)
    descripcion_colonia = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField()
    usuario_creacion = models.CharField(max_length=25)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'pp_colonias'

class SaehAlimentos(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion_alimento = models.CharField(max_length=50, blank=True)
    aparece_condiciones = models.NullBooleanField()
    aparece_vencimiento = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'saeh_alimentos'

class SaehAlimentosCondiciones(models.Model):
    saeh_boleta = models.ForeignKey('SaehBoletas', blank=True, null=True)
    alimento = models.ForeignKey(SaehAlimentos, blank=True, null=True)
    condicion_buena = models.NullBooleanField()
    observaciones = models.CharField(max_length=150, blank=True)
    class Meta:
        managed = False
        db_table = 'saeh_alimentos_condiciones'

class SaehAlimentosExpiracion(models.Model):
    saeh_boleta = models.ForeignKey('SaehBoletas', blank=True, null=True)
    alimento = models.ForeignKey(SaehAlimentos, blank=True, null=True)
    consumible_antes_vencimiento = models.NullBooleanField()
    observaciones = models.CharField(max_length=150, blank=True)
    class Meta:
        managed = False
        db_table = 'saeh_alimentos_expiracion'

class SaehAlimentosMovilizacion(models.Model):
    saeh_boleta = models.ForeignKey('SaehBoletas', blank=True, null=True)
    alimento = models.ForeignKey(SaehAlimentos, blank=True, null=True)
    alimento_sobra_anterior = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    alimento_ingreso_actual = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    alimento_consumido_actual = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    perdida_alimento_actual = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'saeh_alimentos_movilizacion'

class SaehBoletas(models.Model):
    centro = models.ForeignKey(EeCentros, blank=True, null=True)
    boleta = models.ForeignKey(EeBoletas, blank=True, null=True)
    aldea = models.ForeignKey(EeAldeas, blank=True, null=True)
    caserio = models.ForeignKey(EeCaserios, blank=True, null=True)
    barrio_colonia = models.ForeignKey(EeBarriosColonias, blank=True, null=True)
    ubicacion_x = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    ubicacion_y = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fecha_visita = models.DateTimeField(blank=True, null=True)
    jornada = models.CharField(max_length=1, blank=True)
    dias_sin_alimento = models.IntegerField(blank=True, null=True)
    recipientes_almacenamiento = models.NullBooleanField()
    otros_recipientes = models.CharField(max_length=50, blank=True)
    cantidad_tarimas = models.IntegerField(blank=True, null=True)
    cantidad_silos = models.IntegerField(blank=True, null=True)
    cantidad_barriles = models.IntegerField(blank=True, null=True)
    cantidad_baldes_plasticos = models.IntegerField(blank=True, null=True)
    cantidad_otros_recipientes = models.IntegerField(blank=True, null=True)
    comite_merienda_madres = models.IntegerField(blank=True, null=True)
    comite_merienda_padres = models.IntegerField(blank=True, null=True)
    comite_merienda_maestros = models.IntegerField(blank=True, null=True)
    comite_merienda_otros = models.IntegerField(blank=True, null=True)
    comite_merienda_descripcion_otros = models.CharField(max_length=50, blank=True)
    comite_merienda_directivos_f = models.IntegerField(blank=True, null=True)
    comite_merienda_directivos_m = models.IntegerField(blank=True, null=True)
    otro_tipo_combustible = models.CharField(max_length=50, blank=True)
    otros_aportes = models.CharField(max_length=50, blank=True)
    unidad_salud_cercana = models.CharField(max_length=100, blank=True)
    distancia_unidad_salud = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    recomendaciones = models.CharField(max_length=256, blank=True)
    nombre_director = models.CharField(max_length=150, blank=True)
    telefono_director = models.CharField(max_length=10, blank=True)
    nombre_persona_monitoreo = models.CharField(max_length=150, blank=True)
    institucion_monitoreo = models.ForeignKey('SaehInstitucionesMonitoreo', blank=True, null=True)
    bloqueada = models.NullBooleanField()
    eliminada = models.NullBooleanField()
    advertencias = models.NullBooleanField()
    justificacion_advertencias = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'saeh_boletas'

class SaehCausasAusencias(models.Model):
    saeh_boleta = models.ForeignKey(SaehBoletas, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    descripcion_causa = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'saeh_causas_ausencias'

class SaehClasesEstadisticas(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion_clase_estadistica = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'saeh_clases_estadisticas'

class SaehDesparasitaciones(models.Model):
    saeh_boleta = models.ForeignKey(SaehBoletas, blank=True, null=True)
    numero_entrega = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    tabletas_recibidas = models.IntegerField(blank=True, null=True)
    tabletas_utilizadas = models.IntegerField(blank=True, null=True)
    tipo_desparasitante_mg = models.IntegerField(blank=True, null=True)
    cantidad_beneficiarios = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'saeh_desparasitaciones'

class SaehDiasClases(models.Model):
    saeh_boleta = models.ForeignKey(SaehBoletas, blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    dias_clases = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'saeh_dias_clases'

class SaehEstadisticas(models.Model):
    saeh_boleta = models.ForeignKey(SaehBoletas, blank=True, null=True)
    grado = models.ForeignKey(EeGrados, blank=True, null=True)
    saeh_clase_estadistica = models.ForeignKey(SaehClasesEstadisticas, blank=True, null=True)
    valor_femenino = models.IntegerField(blank=True, null=True)
    valor_masculino = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'saeh_estadisticas'

class SaehGruposRespuestas(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion_grupo = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'saeh_grupos_respuestas'

class SaehInstitucionesMonitoreo(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion_institucion = models.CharField(max_length=200, blank=True)
    class Meta:
        managed = False
        db_table = 'saeh_instituciones_monitoreo'

class SaehPoligonoMunicipio(models.Model):
    poligono_id = models.IntegerField(blank=True, null=True)
    municipio = models.CharField(max_length=4, blank=True)
    punto = models.IntegerField(blank=True, null=True)
    offset = models.IntegerField(blank=True, null=True)
    latitud = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    longitud = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    x = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    y = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    zona = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'saeh_poligono_municipio'

class SaehPosiblesRespuestas(models.Model):
    id = models.IntegerField(primary_key=True)
    grupo_respuestas = models.ForeignKey(SaehGruposRespuestas, blank=True, null=True)
    descripcion_respuesta = models.CharField(max_length=50, blank=True)
    valor_respuesta = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'saeh_posibles_respuestas'

class SaehPreguntas(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=10, blank=True)
    descripcion_pregunta = models.CharField(max_length=256, blank=True)
    grupo_respuestas = models.ForeignKey(SaehGruposRespuestas, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'saeh_preguntas'

class SaehRemesas(models.Model):
    saeh_boleta = models.ForeignKey(SaehBoletas, blank=True, null=True)
    numero_remesa = models.IntegerField(blank=True, null=True)
    fecha_llegada_bodega = models.DateTimeField(blank=True, null=True)
    fecha_salida_bodega = models.DateTimeField(blank=True, null=True)
    dias_alimentos_programados = models.IntegerField(blank=True, null=True)
    dias_alimentos_disponibles = models.IntegerField(blank=True, null=True)
    numero_nota_remision = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'saeh_remesas'

class SaehRespuestas(models.Model):
    saeh_boleta = models.ForeignKey(SaehBoletas)
    pregunta = models.ForeignKey(SaehPreguntas)
    valor = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'saeh_respuestas'

class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sysdiagrams'

class TempoAldeasCentros(models.Model):
    codigo_departamento = models.CharField(max_length=2, blank=True)
    codigo_municipio = models.CharField(max_length=2, blank=True)
    codigo_centro_ee = models.CharField(max_length=9, blank=True)
    codigo_aldea = models.CharField(max_length=5, blank=True)
    descripcion_aldea = models.CharField(max_length=80, blank=True)
    aldea_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tempo_aldeas_centros'

class TempoExtensivoFinal11(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    tipo_boleta = models.CharField(max_length=20, blank=True)
    codigo_centro = models.CharField(max_length=9)
    nombre_centro = models.CharField(max_length=255, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    codigo_departamento = models.CharField(max_length=2, blank=True)
    descripcion_departamento = models.CharField(max_length=25, blank=True)
    codigo_municipio = models.CharField(max_length=2, blank=True)
    descripcion_municipio = models.CharField(max_length=255, blank=True)
    descripcion_tipo_administracion = models.CharField(max_length=25, blank=True)
    descripcion_tipo_zona = models.CharField(max_length=15, blank=True)
    periodo_escolar = models.CharField(max_length=1)
    pais_frontera = models.CharField(max_length=25, blank=True)
    distancia = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descripcion_tipo_docentes = models.CharField(max_length=20)
    descripcion_pueblo_etnico = models.CharField(max_length=20, blank=True)
    descripcion_tipo_centro = models.CharField(max_length=25, blank=True)
    telefono = models.CharField(max_length=12, blank=True)
    correo_electronico = models.CharField(max_length=255)
    en_funcionamiento = models.BooleanField()
    motivo_cierre = models.CharField(max_length=25, blank=True)
    funciona_edificio_propio = models.NullBooleanField()
    inicio_funcionamiento = models.IntegerField(blank=True, null=True)
    comparte_edificio = models.NullBooleanField()
    centros_comparte_edificio = models.CharField(max_length=255, blank=True)
    cambio_nombre = models.BooleanField()
    nombre_anterior = models.CharField(max_length=255, blank=True)
    acuerdo_cambio_nombre = models.CharField(max_length=20, blank=True)
    fecha_cambio_nombre = models.DateTimeField(blank=True, null=True)
    identidad_director = models.CharField(max_length=13, blank=True)
    nombre_completo_director = models.CharField(max_length=150, blank=True)
    sexo_director = models.CharField(max_length=1, blank=True)
    es_extranjero_director = models.NullBooleanField()
    descripcion_modo_cargo = models.CharField(max_length=50, blank=True)
    forma_servicios = models.CharField(max_length=20)
    modalidad_id = models.IntegerField(blank=True, null=True)
    descripcion_modalidad = models.CharField(max_length=120)
    codigo_grado = models.IntegerField(blank=True, null=True)
    descripcion_grado = models.CharField(max_length=20, blank=True)
    consolidada_f = models.IntegerField(blank=True, null=True)
    consolidada_m = models.IntegerField(blank=True, null=True)
    final_f = models.IntegerField(blank=True, null=True)
    final_m = models.IntegerField(blank=True, null=True)
    ingresos_f = models.IntegerField(blank=True, null=True)
    ingresos_m = models.IntegerField(blank=True, null=True)
    desertores_f = models.IntegerField(blank=True, null=True)
    desertores_m = models.IntegerField(blank=True, null=True)
    traslados_f = models.IntegerField(blank=True, null=True)
    traslados_m = models.IntegerField(blank=True, null=True)
    aprobados_f = models.IntegerField(blank=True, null=True)
    aprobados_m = models.IntegerField(blank=True, null=True)
    reprobados_f = models.IntegerField(blank=True, null=True)
    reprobados_m = models.IntegerField(blank=True, null=True)
    graduados_f = models.IntegerField(blank=True, null=True)
    graduados_m = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tempo_extensivo_final_11'

class TempoExtensivoFinal2013(models.Model):
    anio = models.IntegerField(blank=True, null=True)
    tipo_boleta = models.CharField(max_length=20, blank=True)
    codigo_centro = models.CharField(max_length=9)
    nombre_centro = models.CharField(max_length=255, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    codigo_departamento = models.CharField(max_length=2, blank=True)
    descripcion_departamento = models.CharField(max_length=25, blank=True)
    codigo_municipio = models.CharField(max_length=2, blank=True)
    descripcion_municipio = models.CharField(max_length=255, blank=True)
    descripcion_tipo_administracion = models.CharField(max_length=25, blank=True)
    descripcion_tipo_zona = models.CharField(max_length=15, blank=True)
    periodo_escolar = models.CharField(max_length=1)
    pais_frontera = models.CharField(max_length=25, blank=True)
    distancia = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descripcion_tipo_docentes = models.CharField(max_length=20)
    descripcion_pueblo_etnico = models.CharField(max_length=20, blank=True)
    descripcion_tipo_centro = models.CharField(max_length=25, blank=True)
    telefono = models.CharField(max_length=12, blank=True)
    correo_electronico = models.CharField(max_length=255)
    en_funcionamiento = models.BooleanField()
    motivo_cierre = models.CharField(max_length=25, blank=True)
    funciona_edificio_propio = models.NullBooleanField()
    inicio_funcionamiento = models.IntegerField(blank=True, null=True)
    comparte_edificio = models.NullBooleanField()
    centros_comparte_edificio = models.CharField(max_length=255, blank=True)
    cambio_nombre = models.BooleanField()
    nombre_anterior = models.CharField(max_length=255, blank=True)
    acuerdo_cambio_nombre = models.CharField(max_length=20, blank=True)
    fecha_cambio_nombre = models.DateTimeField(blank=True, null=True)
    identidad_director = models.CharField(max_length=13, blank=True)
    nombre_completo_director = models.CharField(max_length=150, blank=True)
    sexo_director = models.CharField(max_length=1, blank=True)
    es_extranjero_director = models.NullBooleanField()
    descripcion_modo_cargo = models.CharField(max_length=50, blank=True)
    forma_servicios = models.CharField(max_length=20)
    modalidad_id = models.IntegerField(blank=True, null=True)
    descripcion_modalidad = models.CharField(max_length=120)
    codigo_grado = models.IntegerField(blank=True, null=True)
    descripcion_grado = models.CharField(max_length=20, blank=True)
    consolidada_f = models.IntegerField(blank=True, null=True)
    consolidada_m = models.IntegerField(blank=True, null=True)
    final_f = models.IntegerField(blank=True, null=True)
    final_m = models.IntegerField(blank=True, null=True)
    ingresos_f = models.IntegerField(blank=True, null=True)
    ingresos_m = models.IntegerField(blank=True, null=True)
    desertores_f = models.IntegerField(blank=True, null=True)
    desertores_m = models.IntegerField(blank=True, null=True)
    traslados_f = models.IntegerField(blank=True, null=True)
    traslados_m = models.IntegerField(blank=True, null=True)
    aprobados_f = models.IntegerField(blank=True, null=True)
    aprobados_m = models.IntegerField(blank=True, null=True)
    reprobados_f = models.IntegerField(blank=True, null=True)
    reprobados_m = models.IntegerField(blank=True, null=True)
    graduados_f = models.IntegerField(blank=True, null=True)
    graduados_m = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tempo_extensivo_final_2013'

class TempoHistoricoPralebah(models.Model):
    codigo_centro = models.CharField(max_length=9)
    class Meta:
        managed = False
        db_table = 'tempo_historico_pralebah'

class TempoMigraCecc2008(models.Model):
    departamento_id = models.IntegerField(blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    tipo_administracion_id = models.IntegerField(blank=True, null=True)
    tipo_zona_id = models.IntegerField(blank=True, null=True)
    mod_indigena = models.CharField(db_column='Mod_Indigena', max_length=2, blank=True) # Field name made lowercase.
    grado_id = models.IntegerField(blank=True, null=True)
    sexo = models.CharField(db_column='Sexo', max_length=9, blank=True) # Field name made lowercase.
    indicadores = models.CharField(db_column='Indicadores', max_length=18, blank=True) # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True) # Field name made lowercase.
    e_0 = models.IntegerField(db_column='E_0', blank=True, null=True) # Field name made lowercase.
    e_1 = models.IntegerField(db_column='E_1', blank=True, null=True) # Field name made lowercase.
    e_2 = models.IntegerField(db_column='E_2', blank=True, null=True) # Field name made lowercase.
    e_3 = models.IntegerField(db_column='E_3', blank=True, null=True) # Field name made lowercase.
    e_4 = models.IntegerField(db_column='E_4', blank=True, null=True) # Field name made lowercase.
    e_5 = models.IntegerField(db_column='E_5', blank=True, null=True) # Field name made lowercase.
    e_6 = models.IntegerField(db_column='E_6', blank=True, null=True) # Field name made lowercase.
    e_7 = models.IntegerField(db_column='E_7', blank=True, null=True) # Field name made lowercase.
    e_8 = models.IntegerField(db_column='E_8', blank=True, null=True) # Field name made lowercase.
    e_9 = models.IntegerField(db_column='E_9', blank=True, null=True) # Field name made lowercase.
    e_10 = models.IntegerField(db_column='E_10', blank=True, null=True) # Field name made lowercase.
    e_11 = models.IntegerField(db_column='E_11', blank=True, null=True) # Field name made lowercase.
    e_12 = models.IntegerField(db_column='E_12', blank=True, null=True) # Field name made lowercase.
    e_13 = models.IntegerField(db_column='E_13', blank=True, null=True) # Field name made lowercase.
    e_14 = models.IntegerField(db_column='E_14', blank=True, null=True) # Field name made lowercase.
    e_15 = models.IntegerField(db_column='E_15', blank=True, null=True) # Field name made lowercase.
    e_16 = models.IntegerField(db_column='E_16', blank=True, null=True) # Field name made lowercase.
    e_17 = models.IntegerField(db_column='E_17', blank=True, null=True) # Field name made lowercase.
    e_18 = models.IntegerField(db_column='E_18', blank=True, null=True) # Field name made lowercase.
    e_19 = models.IntegerField(db_column='E_19', blank=True, null=True) # Field name made lowercase.
    e_20 = models.IntegerField(db_column='E_20', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tempo_migra_cecc_2008'

class TempoMigraCecc2009(models.Model):
    departamento_id = models.IntegerField(blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    tipo_administracion_id = models.IntegerField(blank=True, null=True)
    tipo_zona_id = models.IntegerField(blank=True, null=True)
    mod_indigena = models.CharField(db_column='Mod_Indigena', max_length=2, blank=True) # Field name made lowercase.
    grado_id = models.IntegerField(blank=True, null=True)
    sexo = models.CharField(db_column='Sexo', max_length=9, blank=True) # Field name made lowercase.
    indicadores = models.CharField(db_column='Indicadores', max_length=18, blank=True) # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True) # Field name made lowercase.
    e_0 = models.IntegerField(db_column='E_0', blank=True, null=True) # Field name made lowercase.
    e_1 = models.IntegerField(db_column='E_1', blank=True, null=True) # Field name made lowercase.
    e_2 = models.IntegerField(db_column='E_2', blank=True, null=True) # Field name made lowercase.
    e_3 = models.IntegerField(db_column='E_3', blank=True, null=True) # Field name made lowercase.
    e_4 = models.IntegerField(db_column='E_4', blank=True, null=True) # Field name made lowercase.
    e_5 = models.IntegerField(db_column='E_5', blank=True, null=True) # Field name made lowercase.
    e_6 = models.IntegerField(db_column='E_6', blank=True, null=True) # Field name made lowercase.
    e_7 = models.IntegerField(db_column='E_7', blank=True, null=True) # Field name made lowercase.
    e_8 = models.IntegerField(db_column='E_8', blank=True, null=True) # Field name made lowercase.
    e_9 = models.IntegerField(db_column='E_9', blank=True, null=True) # Field name made lowercase.
    e_10 = models.IntegerField(db_column='E_10', blank=True, null=True) # Field name made lowercase.
    e_11 = models.IntegerField(db_column='E_11', blank=True, null=True) # Field name made lowercase.
    e_12 = models.IntegerField(db_column='E_12', blank=True, null=True) # Field name made lowercase.
    e_13 = models.IntegerField(db_column='E_13', blank=True, null=True) # Field name made lowercase.
    e_14 = models.IntegerField(db_column='E_14', blank=True, null=True) # Field name made lowercase.
    e_15 = models.IntegerField(db_column='E_15', blank=True, null=True) # Field name made lowercase.
    e_16 = models.IntegerField(db_column='E_16', blank=True, null=True) # Field name made lowercase.
    e_17 = models.IntegerField(db_column='E_17', blank=True, null=True) # Field name made lowercase.
    e_18 = models.IntegerField(db_column='E_18', blank=True, null=True) # Field name made lowercase.
    e_19 = models.IntegerField(db_column='E_19', blank=True, null=True) # Field name made lowercase.
    e_20 = models.IntegerField(db_column='E_20', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tempo_migra_cecc_2009'

class TempoRedesEducativas(models.Model):
    codigored = models.CharField(db_column='CodigoRed', max_length=255, blank=True) # Field name made lowercase.
    nombrered = models.CharField(db_column='NombreRed', max_length=255, blank=True) # Field name made lowercase.
    codigodepartamentocentro = models.CharField(db_column='CodigoDepartamentoCentro', max_length=255, blank=True) # Field name made lowercase.
    descripciondepartamento = models.CharField(db_column='DescripcionDepartamento', max_length=255, blank=True) # Field name made lowercase.
    codigomunicipiocentro = models.CharField(db_column='CodigoMunicipioCentro', max_length=255, blank=True) # Field name made lowercase.
    descripcionmunicipio = models.CharField(db_column='DescripcionMunicipio', max_length=255, blank=True) # Field name made lowercase.
    codigocentro = models.CharField(db_column='CodigoCentro', max_length=255, blank=True) # Field name made lowercase.
    nombre_centro = models.CharField(db_column='Nombre_Centro', max_length=255, blank=True) # Field name made lowercase.
    codigo_aldea = models.CharField(db_column='Codigo_Aldea', max_length=255, blank=True) # Field name made lowercase.
    descripcion_aldea = models.CharField(db_column='Descripcion_Aldea', max_length=255, blank=True) # Field name made lowercase.
    direccion_centro = models.CharField(db_column='Direccion_Centro', max_length=255, blank=True) # Field name made lowercase.
    nivel_educativo = models.CharField(db_column='Nivel_Educativo', max_length=255, blank=True) # Field name made lowercase.
    codigotipocentrored = models.CharField(db_column='CodigoTipoCentroRed', max_length=255, blank=True) # Field name made lowercase.
    descripciontipocentrored = models.CharField(db_column='DescripcionTipoCentroRed', max_length=255, blank=True) # Field name made lowercase.
    noresolucion = models.CharField(db_column='NoResolucion', max_length=255, blank=True) # Field name made lowercase.
    tipoorganizacion = models.CharField(db_column='TipoOrganizacion', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tempo_redes_educativas'

class TempoZonasMarginales(models.Model):
    municipio = models.FloatField(db_column='Municipio', blank=True, null=True) # Field name made lowercase.
    barrio = models.CharField(max_length=255, blank=True)
    codigo = models.FloatField(blank=True, null=True)
    marginacion = models.FloatField(blank=True, null=True)
    grado = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'tempo_zonas_marginales'

class UpegEstadisticaFinal2013(models.Model):
    codigo_departamento = models.CharField(max_length=2, blank=True)
    descripcion_departamento = models.CharField(max_length=25, blank=True)
    codigo_municipio = models.CharField(max_length=2, blank=True)
    descripcion_municipio = models.CharField(max_length=255, blank=True)
    tipo_boleta = models.CharField(max_length=20, blank=True)
    codigo_centro = models.CharField(max_length=9)
    nombre_centro = models.CharField(max_length=255, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    tipo_centro = models.CharField(max_length=25)
    tipo_administracion = models.CharField(max_length=25)
    tipo_zona = models.CharField(max_length=15)
    grado = models.CharField(max_length=20)
    consolidada_f = models.IntegerField()
    consolidada_m = models.IntegerField()
    consolidada = models.IntegerField(blank=True, null=True)
    final_f = models.IntegerField()
    final_m = models.IntegerField()
    final = models.IntegerField(blank=True, null=True)
    ingresos_f = models.IntegerField()
    ingresos_m = models.IntegerField()
    ingresos = models.IntegerField(blank=True, null=True)
    desertores_f = models.IntegerField()
    desertores_m = models.IntegerField()
    desertores = models.IntegerField(blank=True, null=True)
    traslados_f = models.IntegerField()
    traslados_m = models.IntegerField()
    traslados = models.IntegerField(blank=True, null=True)
    aprobados_f = models.IntegerField()
    aprobados_m = models.IntegerField()
    aprobados = models.IntegerField(blank=True, null=True)
    reprobados_f = models.IntegerField()
    reprobados_m = models.IntegerField()
    reprobados = models.IntegerField(blank=True, null=True)
    graduados_f = models.IntegerField()
    graduados_m = models.IntegerField()
    graduados = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'upeg_estadistica_final_2013'

