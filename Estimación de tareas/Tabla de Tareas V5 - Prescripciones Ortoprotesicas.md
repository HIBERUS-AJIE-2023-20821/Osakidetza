# Tabla de Tareas — Prescripciones Ortoprotésicas Osakidetza

## V5 — 05/03/2026

Documento generado a partir del Enfoque PM/BA V5 y cruzado con el Excel de estimación existente (T-001 a T-058).

**Convenciones**:
- **Ref. Excel**: ID de la tarea en el Excel original (vacío = tarea nueva no presente en el Excel).
- **Horas**: columna vacía para estimación.
- **Comentario**: notas sobre redundancia, revisión o eliminación potencial.

---

| # | Módulo | Submódulo | Caso de uso | Tarea | Front/Back | Ref. Excel | Horas | Comentario |
|---|---|---|---|---|---|---|---|---|
| 1 | AUTH | Login Osabide Global | Autenticación | Login a través de Osabide Global pasando token: recepción de token, validación de contexto profesional, carga de permisos | Front | T-004 | | |
| 2 | AUTH | Login Osabide Global | Autenticación | Validación de token de Osabide Global: verificación del contexto (centro, ámbito, servicio, paciente) en back | Back | — | | Nueva. T-004 solo cubre front; falta el back de validación del token |
| 3 | AUTH | Login externo | Autenticación | Pantalla de login externo con credenciales LDAP/AD | Front | T-005 | | |
| 4 | AUTH | Login externo | Autenticación | Sistema de login externo: autenticación contra LDAP/AD | Back | T-006 | | |
| 5 | AUTH | Roles y permisos | Gestión de roles | Pantalla de gestión de roles y permisos de facultativos | Front | — | | Nueva. Sujeta a resolución de P-01 (puede que Osabide Global ya proporcione lo necesario) |
| 6 | AUTH | Roles y permisos | Gestión de roles | APIs CRUD de gestión de roles y permisos | Back | — | | Nueva. Sujeta a resolución de P-01 |
| 7 | AUTH | Roles y permisos | Cambio de rol | Cambio de rol activo en sesión si el usuario tiene varios roles | Front | — | | Nueva. No existe en el Excel |
| 8 | AUTH | Roles y permisos | Cambio de rol | Lógica de cambio de rol activo: recarga de permisos y contexto | Back | — | | Nueva. No existe en el Excel |
| 9 | AUTH | Modo acceso | Modo con/sin paciente | Lógica para admitir acceso con paciente asociado (cita activa) y sin paciente (gestión propia del facultativo) | Back | — | | Nueva. El sistema debe diferenciar ambos modos y adaptar el listado de prescripciones en consecuencia |
| 10 | AUTH | Modo acceso | Modo con/sin paciente | Adaptación de interfaz según modo de acceso (con paciente: preselecciona paciente; sin paciente: muestra todas las prescripciones del facultativo) | Front | — | | Nueva |
| 11 | CATÁLOGO | BBDD | Diseño BBDD | Diseño de base de datos del catálogo: campos del nomenclátor del Departamento + campos propios de Osakidetza | Back | T-007 | | |
| 12 | CATÁLOGO | BBDD | Diseño BBDD | Creación y pruebas de base de datos del catálogo | Back | T-008 | | |
| 13 | CATÁLOGO | BBDD | Gobierno de edición | Definición y desarrollo de campos propios de Osakidetza (activo sí/no, favoritos por facultativo, campos de caracterización de producto, campos adicionales para reglas de indicación) | Back | — | | Nueva. Ampliada: incluye campos de caracterización de productos (decisión cliente 11/03/2026) |
| 14 | CATÁLOGO | Sincronización | Carga masiva por ficheros | Proceso de importación periódica de ficheros del nomenclátor del Departamento (~1.000 productos): lectura, parseo, validación de formato/contenido, carga en BBDD, gestión de errores (duplicados, campos faltantes, formatos incorrectos), log de auditoría de cada carga. NO se usa replicación BBDD (Golden Gate descartado por coste) | Back | T-009 | | Actualizada: la carga es por importación de ficheros (CSV/XML/otro), no por sincronización genérica de BBDD |
| 15 | CATÁLOGO | Sincronización | Carga bajo demanda por ficheros | Ejecución manual del mismo proceso de importación de ficheros fuera de ciclo. Incluye subida manual del fichero por parte del administrador | Back | T-010 | | Actualizada: misma lógica de ficheros que #14 pero ejecución manual |
| 16 | CATÁLOGO | Sincronización | Gestión de ficheros y failover | Mecanismo de recepción de ficheros del Departamento (SFTP, carpeta compartida o API de descarga), validación previa al procesamiento, gestión de reintentos si la importación falla, y garantía de disponibilidad 24x7 del catálogo local | Back | — | | Actualizada: pasa de réplica BBDD a gestión de ficheros + failover local |
| 17 | CATÁLOGO | Gestión catálogo | Pantalla gestión | Pantalla de gestión/administración del catálogo: listado con filtros, ficha de producto editable (campos Osakidetza + campos de caracterización), activar/desactivar productos | Front | T-011 | | Ampliada: incluye campos de caracterización de producto (decisión cliente 11/03/2026) |
| 18 | CATÁLOGO | Gestión catálogo | APIs catálogo | APIs CRUD de gestión del catálogo incluyendo campos de caracterización | Back | T-012 | | Ampliada: incluye persistencia de caracterización |
| 19 | CATÁLOGO | Búsqueda | Pantalla búsqueda | Pantalla/diálogo de búsqueda de catálogo de productos, con filtros y acceso al detalle | Front | T-013 | | |
| 20 | CATÁLOGO | Búsqueda | Filtro por tipo | Filtro de productos por tipo | Back | T-014 | | |
| 21 | CATÁLOGO | Búsqueda | Filtro por familia | Filtro de producto por familia (grupo > subgrupo > categoría) | Back | T-015 | | |
| 22 | CATÁLOGO | Búsqueda | Filtro por código | Filtro de producto por código | Back | T-016 | | |
| 23 | CATÁLOGO | Búsqueda | Filtro por descripción | Filtro de producto por descripción (texto libre) | Back | — | | Nueva. Los filtros del Excel no incluyen búsqueda por descripción |
| 24 | CATÁLOGO | Selección | Pantalla selección | Pantalla de selección de productos dentro de la prescripción: favoritos primero + productos similares | Front | T-017 | | |
| 25 | CATÁLOGO | Selección | Productos no disponibles | Mostrar todos los productos del catálogo, incluso los que el facultativo no puede prescribir (aparecen como no disponibles para que pueda solicitar permisos) | Front | — | | Nueva. RN-13: productos sin permiso visibles pero marcados como no disponibles |
| 26 | CATÁLOGO | Selección | Productos no disponibles | Validación back: marcar productos como no disponibles según permisos del facultativo | Back | — | | Nueva. Complemento back de #25 |
| 27 | CATÁLOGO | Favoritos | Pantalla favoritos | Pantalla de gestión de favoritos del facultativo | Front | T-018 | | |
| 28 | CATÁLOGO | Favoritos | Sistema favoritos | Sistema de gestión de favoritos: almacenamiento en BBDD de Osakidetza, marcado por el facultativo desde la prescripción | Back | T-019 | | |
| 29 | PRESCRIPCIÓN | BBDD | Diseño BBDD | Diseño de base de datos de prescripciones (prescripción, materiales, estados, histórico, adjuntos) | Back | T-020 | | |
| 30 | PRESCRIPCIÓN | BBDD | Diseño BBDD | Creación y pruebas de BD de prescripciones | Back | T-021 | | |
| 31 | PRESCRIPCIÓN | Listado | Pantalla listado | Pantalla de consulta/listado de prescripciones con filtros (por paciente, por facultativo, por estado, por fecha, por OSI, por tipo producto) | Front | T-022 | | |
| 32 | PRESCRIPCIÓN | Listado | APIs búsqueda | APIs de búsqueda/consulta de prescripciones con filtros | Back | T-023 | | |
| 33 | PRESCRIPCIÓN | Listado | Indicador visual | Indicador visual de estado de dispensación en el listado (icono/color + columna de estado textual) | Front | — | | Nueva. Sin ella el prescriptor no identifica visualmente el estado |
| 34 | PRESCRIPCIÓN | Detalle | API detalle | API consulta detalles de una prescripción | Back | T-024 | | |
| 35 | PRESCRIPCIÓN | Detalle | Pantalla detalle | Pantalla de consulta de detalle de prescripción (modo lectura, datos completos, estado de cada material) | Front | T-025 | | |
| 36 | PRESCRIPCIÓN | Detalle | Histórico | Pantalla de histórico de la prescripción: acciones realizadas, cambios de estado, fechas | Front | — | | Nueva. No existe en el Excel |
| 37 | PRESCRIPCIÓN | Detalle | Histórico | API/servicio de histórico/auditoría de la prescripción | Back | — | | Nueva. No existe en el Excel |
| 38 | PRESCRIPCIÓN | Detalle | Documentos adjuntos | Visualización y descarga de documentos adjuntos (informe clínico, CSV firmado) | Front | — | | Nueva. Implícita pero no tiene tarea propia |
| 39 | PRESCRIPCIÓN | Creación | Pantalla creación | Pantalla de creación de prescripción con cabecera precargada (datos paciente + datos facultativo) | Front | T-026 | | |
| 40 | PRESCRIPCIÓN | Creación | Recuperar info facultativo | Recuperar información del facultativo desde contexto Osabide Global o directorio corporativo (nº colegiado, especialidad, centro, servicio) | Back | T-027 | | Revisar: no especifica si es API a SAP, BBDD directa o ambas |
| 41 | PRESCRIPCIÓN | Creación | Recuperar info paciente | Recuperar información del paciente desde Osategi vía CIC (TIS, CIP, nombre, sexo, nacimiento, domicilio) | Back | T-028 | | Revisar: no especifica si es servicio web Osategi o BBDD directa |
| 42 | PRESCRIPCIÓN | Creación | Añadir materiales | Añadir materiales/productos a la prescripción desde el buscador de catálogo | Front | T-029 | | |
| 43 | PRESCRIPCIÓN | Creación | Visado obligar informe | Si el producto requiere visado, obligar a adjuntar informe clínico (RN-02) | Front | T-030 | | |
| 44 | PRESCRIPCIÓN | Creación | Catálogo indicadores | Considerar catálogo de indicadores por producto (visado, protocolo, campos adicionales) | Front | T-031 | | Revisar: ¿solapamiento con #43 y #45? Valorar si es tarea independiente o parte de la pantalla de creación |
| 45 | PRESCRIPCIÓN | Creación | Protocolo campos adicionales | Si el producto tiene protocolo, mostrar campos adicionales del protocolo en el formulario | Front | — | | Nueva. Derivada de §3.2 del enfoque |
| 46 | PRESCRIPCIÓN | Creación | Protocolo campos adicionales | Lógica back para gestionar campos de protocolo por producto | Back | — | | Nueva |
| 47 | PRESCRIPCIÓN | Edición | Pantalla edición | Pantalla de edición de prescripción existente (si el estado lo permite) | Front | — | | Nueva como tarea front independiente. T-034 cubre solo la API back |
| 48 | PRESCRIPCIÓN | Creación | Guardar borrador | Guardar prescripción como borrador (sin firmar) | Front | — | | Nueva. Implícita en T-033 pero no tiene tarea front propia |
| 49 | PRESCRIPCIÓN | Firma | Firmar prescripción | Firmar y autorizar prescripción desde interfaz (integración Giltza/Izenpe) | Front | T-032 | | Revisar: 10h puede ser insuficiente para la integración con Giltza/Izenpe |
| 50 | PRESCRIPCIÓN | Firma | Firmar y generar | Firmar y generar prescripción en back: firma digital, generación de CSV/documento firmado | Back | T-040 | | Es el par back de T-032; no es redundante sino complementario |
| 51 | PRESCRIPCIÓN | APIs CRUD | API creación | API de creación de prescripción | Back | T-033 | | |
| 52 | PRESCRIPCIÓN | APIs CRUD | API edición | API de edición de prescripción | Back | T-034 | | |
| 53 | PRESCRIPCIÓN | APIs CRUD | API eliminación | API de eliminación de prescripción (solo borrador/pendiente de firma) | Back | T-035 | | |
| 54 | PRESCRIPCIÓN | Listado | Acción eliminar | Acción de eliminar prescripción desde el listado (front) | Front | — | | Nueva. T-035 cubre la API back pero falta la acción en front |
| 55 | PRESCRIPCIÓN | APIs CRUD | API clonar | API de clonar/copiar prescripción (elimina materiales no válidos para la especialidad) | Back | T-036 | | |
| 56 | PRESCRIPCIÓN | Listado | Acción copiar | Acción de copiar/duplicar prescripción desde el listado (front) | Front | — | | Nueva. T-036 cubre la API back pero falta la acción en front |
| 57 | PRESCRIPCIÓN | APIs CRUD | API anular | API de anular prescripción (si no dispensada ni anulada) | Back | T-037 | | |
| 58 | PRESCRIPCIÓN | Listado | Acción anular | Acción de anular prescripción desde el listado (front) | Front | — | | Nueva. T-037 cubre la API back |
| 59 | PRESCRIPCIÓN | APIs CRUD | API renovar | API de renovar prescripción (crea prescripción de renovación) | Back | T-038 | | |
| 60 | PRESCRIPCIÓN | Listado | Acción renovar | Acción de renovar prescripción desde el listado (front): si es temprana, solicitar justificación clínica | Front | — | | Nueva. T-038 cubre la API back; falta el front |
| 61 | PRESCRIPCIÓN | Validación | Validar prescripción | Validar prescripción: aplicar reglas de negocio (unidad clínica, visado, motivo, estados) | Back | T-039 | | |
| 62 | PRESCRIPCIÓN | Validación | Validar unidad clínica | Validar que el prescriptor solo puede prescribir productos de su unidad clínica/especialidad (RN-01) | Back | — | | Nueva. T-039 es genérica; esta regla necesita implementación específica |
| 63 | PRESCRIPCIÓN | Validación | Validar motivo especial | Validar motivo accidente de trabajo / enfermedad profesional: intervención adicional, comunicación al sistema de visado (RN-04) | Back | — | | Nueva. No existe en el Excel |
| 64 | PRESCRIPCIÓN | Validación | Validar rechazada no reabrir | Validar que prescripción rechazada por inspección no se puede reabrir (RN-05) | Back | — | | Nueva. No existe en el Excel |
| 65 | PRESCRIPCIÓN | Impresión | Imprimir prescripción | Imprimir prescripción desde interfaz (genera PDF oficial para entrega al paciente) | Front | T-041 | | |
| 66 | PRESCRIPCIÓN | Impresión | Imprimir prescripción | Generación de PDF de prescripción (back): plantilla oficial Osakidetza | Back | T-042 | | |
| 67 | PRESCRIPCIÓN | Impresión | Descargar informe | Descargar informe/CSV de la prescripción firmada | Back | T-043 | | |
| 68 | PRESCRIPCIÓN | Exportación | Exportar Excel | Exportar listado filtrado de prescripciones a Excel | Back | T-044 | | |
| 69 | PRESCRIPCIÓN | Renovación | Prescripción recurrente | Renovación de prescripción: considerar renovación a tiempo y renovación temprana (exige justificación clínica escrita, RN-07) | Back | T-045 | | Revisar: 20h puede ser insuficiente si incluye toda la lógica de justificación de renovación temprana. ¿Solapamiento con #59 (API renovar)? Valorar si T-045 es redundante con T-038 o si son complementarias |
| 70 | PRESCRIPCIÓN | Máquina estados | Estados prescripción | Implementación de la máquina de estados de la prescripción (8 estados, transiciones definidas en §3.4) | Back | — | | Nueva. Crítica. No existe como tarea independiente en el Excel |
| 71 | PRESCRIPCIÓN | Máquina estados | Estados material | Implementación de la máquina de estados del material (10 estados, transiciones definidas en §3.5) | Back | — | | Nueva. Crítica. No existe como tarea independiente en el Excel |
| 72 | PRESCRIPCIÓN | Caducidad | Proceso caducidad | Proceso automático de caducidad: job/scheduler que marca como "No vigente" las prescripciones no dispensadas en plazo (configurable, propuesta 6 meses, RN-10) | Back | — | | Nueva. No existe en el Excel |
| 73 | PRESCRIPCIÓN | Nº Expediente | Generación expediente | Generación del nº de expediente de la prescripción (pendiente definir origen — P-02) | Back | — | | Nueva. Sujeta a resolución de P-02 |
| 74 | DISPENSACIÓN | APIs interop. | Consulta dispensables | API de consulta de prescripciones dispensables por paciente (TIS) | Back | T-050 | | |
| 75 | DISPENSACIÓN | APIs interop. | Bloquear material | API para bloquear material (reservado por un establecimiento; RN-09) | Back | T-051 | | Revisar: el Excel dice "Bloquear prescripción" pero el enfoque es por material, no por prescripción |
| 76 | DISPENSACIÓN | APIs interop. | Desbloquear material | API para desbloquear material | Back | T-052 | | Revisar: mismo comentario que #75, es por material |
| 77 | DISPENSACIÓN | APIs interop. | Recibir dispensación | Recibir información de dispensación (API/evento): actualizar estado del material a Dispensado, registrar fecha, establecimiento | Back | T-053 | | |
| 78 | DISPENSACIÓN | Visado | Enviar solicitud visado | Enviar solicitud de visado al Departamento al firmar prescripción con material que requiere visado | Back | — | | Nueva. T-054 mezcla envío y recepción; deberían ser 2 tareas separadas |
| 79 | DISPENSACIÓN | Visado | Recibir estado visado | Servicio receptor de estado de visado (push inmediato del Departamento): actualizar estado de prescripción | Back | T-054 | | Revisar: T-054 no diferencia solicitud (ida) de recepción (vuelta). La estimación de 60h debería repartirse entre #78 y #79 |
| 80 | DISPENSACIÓN | Validación post-disp. | Validación prescriptor | Pantalla/acción para que el prescriptor valide o rechace un material dispensado que requiere validación clínica | Front | — | | Nueva. No existe en el Excel |
| 81 | DISPENSACIÓN | Validación post-disp. | Validación prescriptor | Lógica back de validación post-dispensación: cambiar estado material según decisión del prescriptor | Back | — | | Nueva. No existe en el Excel |
| 82 | DISPENSACIÓN | Dispensación parcial | Visualización parcial | Visualización del estado material a material en prescripciones con dispensación parcial (front) | Front | — | | Nueva. Sujeta a definición UX (P-08) |
| 83 | DISPENSACIÓN | Dispensación parcial | Lógica parcial | Lógica de dispensación parcial: gestionar estados independientes por material dentro de una prescripción (RN-16) | Back | — | | Nueva |
| 84 | TAREAS | Tarea visado | Crear tarea | Crear tarea pendiente cuando la prescripción pasa a "Pendiente inspección" (requiere visado) | Back | T-046 | | |
| 85 | TAREAS | Tarea visado | Actualizar tarea | Actualizar tarea cuando cambia el estado de visado (aprobado/rechazado/solicitud modificación) | Back | T-047 | | |
| 86 | TAREAS | Tarea validación | Tarea validación | Crear tarea pendiente cuando un material dispensado requiere validación del prescriptor | Back | — | | Nueva. No existe en el Excel |
| 87 | TAREAS | Tarea dispensación | Tarea dispensación | Crear aviso cuando todos los materiales de una prescripción se dispensan (cierre de ciclo) | Back | — | | Nueva. No existe en el Excel |
| 88 | TAREAS | Pantalla tareas | Pantalla tareas | Pantalla de visualización de tareas pendientes: visados pendientes, rechazados, modificaciones solicitadas, dispensaciones pendientes de validación | Front | T-048 | | |
| 89 | TAREAS | APIs tareas | APIs tareas | APIs de gestión de tareas pendientes (listado, marcar como vista, histórico) | Back | T-049 | | |
| 90 | TAREAS | Dashboard | Avisos al entrar | Dashboard/pantalla de avisos al entrar al módulo: resumen de pendientes antes de acceder al listado | Front | — | | Nueva. No existe en el Excel |
| 91 | TAREAS | Dashboard | Avisos al entrar | API de resumen de pendientes para el dashboard de entrada | Back | — | | Nueva |
| 92 | MANTENIMIENTO | Establecimientos | Pantalla establecimientos | Pantalla de gestión de establecimientos (listado, alta, edición, baja) | Front | — | | Nueva. No existe en el Excel |
| 93 | MANTENIMIENTO | Establecimientos | APIs establecimientos | APIs CRUD de gestión de establecimientos | Back | — | | Nueva. No existe en el Excel |
| 94 | MANTENIMIENTO | Configuraciones | Pantalla configuraciones | Pantalla de configuración del sistema (plazos de caducidad, sincronización, parámetros operativos) | Front | — | | Nueva como front. T-003 solo cubre back |
| 95 | MANTENIMIENTO | Configuraciones | API configuraciones | API de gestión de configuraciones del sistema | Back | T-003 | | Revisar: T-003 mezcla configuraciones + roles en una sola tarea; valorar separar |
| 96 | TRANSVERSAL | Multi-idioma | Multi-idioma front | Internacionalización del front: euskera / castellano | Front | T-001 | | Revisar: 60h. ¿El framework ya soporta i18n? Si sí, la estimación podría reducirse |
| 97 | TRANSVERSAL | Multi-idioma | Multi-idioma back | Internacionalización del back: mensajes, validaciones, errores en euskera / castellano | Back | T-002 | | Revisar: 60h. Mismo comentario que #96 |
| 98 | TRANSVERSAL | Unificación pacientes | Unificación pacientes | Modificar el proceso de unificación de pacientes existente en Osakidetza para incluir prescripciones ortoprotésicas | Back | — | | Nueva. Solo aparece mencionada fuera de la tabla principal del Excel |
| 99 | TRANSVERSAL | Módulo SOA | Servicio terceros | Creación de módulo/servicio para exponer datos de prescripciones a otros sistemas de Osakidetza (servicio de consulta para terceros) | Back | T-055 | | |
| 100 | TRANSVERSAL | QA | QA front | Pruebas y tests unitarios: front (plan de pruebas de casos de uso) | Front | T-056 | | Revisar: 120h (~10% del desarrollo); con la complejidad de la máquina de estados podría quedarse corto |
| 101 | TRANSVERSAL | QA | QA back | Pruebas y tests unitarios: back | Back | T-057 | | Revisar: 120h; mismo comentario que #100 |
| 102 | TRANSVERSAL | ETL Reporting | ETL datos reporting | ETL de extracción de datos de prescripciones y carga en BBDD de reporting | Back | T-058 | | ELIMINADA DEL ALCANCE. Reporting/ETL fue excluido del proyecto; esta tarea debería desaparecer |
| 103 | MANTENIMIENTO | Reglas indicación | Modelo de datos reglas | Diseño e implementación del modelo de datos para reglas de indicación por producto: tipos de regla (especialidad, edad, sexo, diagnóstico, límite renovación, requisito documental, etc.), condiciones, acciones, vigencia | Back | — | | Nueva (decisión cliente 11/03/2026). Crítica: sin modelo de reglas no se puede implementar la validación |
| 104 | MANTENIMIENTO | Reglas indicación | Pantalla admin reglas | Pantalla de administración de reglas de indicación: crear, editar, desactivar reglas por producto o grupo de productos. Incluye vista de reglas vigentes y histórico | Front | — | | Nueva (decisión cliente 11/03/2026) |
| 105 | MANTENIMIENTO | Reglas indicación | APIs CRUD reglas | APIs CRUD para gestión de reglas de indicación (crear, editar, desactivar, consultar por producto) | Back | — | | Nueva (decisión cliente 11/03/2026) |
| 106 | MANTENIMIENTO | Reglas indicación | Motor validación reglas | Motor/servicio de validación que aplica las reglas de indicación configuradas cuando un facultativo prescribe un producto. Devuelve errores/advertencias si no se cumplen condiciones. Consumido por el Módulo 3 (Prescripción) | Back | — | | Nueva (decisión cliente 11/03/2026). Crítica: conecta mantenimiento con prescripción |
| 107 | PRESCRIPCIÓN | Validación | Integrar reglas indicación | Integrar en el flujo de prescripción la llamada al motor de validación de reglas de indicación: al añadir producto, mostrar errores/advertencias basados en reglas configuradas | Front | — | | Nueva (decisión cliente 11/03/2026). Complemento front del motor de validación |
| 108 | CATÁLOGO | Sincronización | Log importación ficheros | Pantalla de consulta del log/histórico de importaciones de ficheros: fecha, fichero procesado, registros cargados, errores detectados, estado de la carga | Front | — | | Nueva. Necesaria para trazabilidad de las cargas por fichero |

---

## Resumen

| Concepto | Cantidad |
|---|---|
| Tareas totales | 108 |
| Tareas del Excel original conservadas | 48 |
| Tareas nuevas (no estaban en el Excel) | 60 |
| Tareas marcadas para revisión | 12 |
| Tareas marcadas como potencialmente redundantes | 3 |
| Tareas eliminadas del alcance | 1 (T-058 ETL) |
| Tareas añadidas por decisiones cliente 11/03/2026 | 6 (#103–#108) |

### Tareas con comentarios de redundancia o eliminación

| # | Tarea | Comentario |
|---|---|---|
| 44 | Catálogo indicadores (T-031) | Posible solapamiento con #43 (visado) y #45 (protocolo). Valorar si es independiente o se absorbe |
| 69 | Prescripción recurrente (T-045) | Posible redundancia con #59 (API renovar, T-038). Ambas tratan renovación; valorar si se unifican |
| 102 | ETL datos reporting (T-058) | ELIMINADA DEL ALCANCE. Debería desaparecer |

### Tareas con revisión de estimación

| # | Tarea | Ref. Excel | Horas Excel | Observación |
|---|---|---|---|---|
| 49 | Firmar prescripción front | T-032 | 10h | Posiblemente subestimado para integración Giltza/Izenpe |
| 69 | Prescripción recurrente | T-045 | 20h | Puede ser insuficiente si incluye lógica de justificación |
| 79 | Recibir estado visado | T-054 | 60h | No diferencia envío de recepción; repartir entre #78 y #79 |
| 95 | API configuraciones | T-003 | 40h | Mezcla configuraciones y roles; separar |
| 96-97 | Multi-idioma | T-001/002 | 120h | Verificar si el framework ya soporta i18n |
| 100-101 | QA | T-056/057 | 240h | ~10% del desarrollo; podría ser insuficiente |
