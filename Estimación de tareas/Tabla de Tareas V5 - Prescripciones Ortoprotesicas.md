# Tabla de Tareas — Prescripciones Ortoprotésicas Osakidetza

## V7 — 11/03/2026

Documento generado a partir del Enfoque PM/BA V5, cruzado con el Excel de estimación existente (T-001 a T-058) y actualizado con las decisiones del cliente del 11/03/2026 (integración por ficheros + módulo de reglas de indicación). V7: revisión de horas (recorte de margen excesivo), incorporación de JP y UX al equipo, fase previa de diseño UX+análisis funcional, y compresión del cronograma de desarrollo.

**Convenciones**:
- **Ref. Excel**: ID de la tarea en el Excel original (vacío / — = tarea nueva no presente en el Excel).
- **Horas**: estimación en horas de desarrollo efectivo por tarea (incluyen margen moderado; no incluyen gestión ni coordinación).
- **Comentario**: notas sobre redundancia, revisión o eliminación potencial.

**Fases del cronograma** (referenciadas en la planificación §9):
- **FP** — Fase previa: diseño UX + análisis funcional (antes del desarrollo)
- **F0** — Fundamentos (arquitectura, BBDD, autenticación)
- **F1** — Catálogo y sincronización por ficheros
- **F2** — Prescripción core (CRUD, estados, validaciones)
- **F3** — Firma digital y visado
- **F4** — Dispensación, tareas y cierre de ciclo
- **F5** — Mantenimiento, reglas de indicación, roles
- **F6** — Transversales (i18n, SOA, QA final)

---

| # | Módulo | Submódulo | Caso de uso | Tarea | Front/Back | Ref. Excel | Horas | Comentario |
|---|---|---|---|---|---|---|---|---|
| 1 | AUTH | Login Osabide Global | Autenticación | Login a través de Osabide Global pasando token: recepción de token, validación de contexto profesional, carga de permisos | Front | T-004 | 40 | |
| 2 | AUTH | Login Osabide Global | Autenticación | Validación de token de Osabide Global: verificación del contexto (centro, ámbito, servicio, paciente) en back | Back | — | 24 | Nueva. T-004 solo cubre front; falta el back de validación del token |
| 3 | AUTH | Login externo | Autenticación | Pantalla de login externo con credenciales LDAP/AD | Front | T-005 | 24 | |
| 4 | AUTH | Login externo | Autenticación | Sistema de login externo: autenticación contra LDAP/AD | Back | T-006 | 32 | |
| 5 | AUTH | Roles y permisos | Gestión de roles | Pantalla de gestión de roles y permisos de facultativos | Front | — | 40 | Nueva. Sujeta a resolución de P-01 (puede que Osabide Global ya proporcione lo necesario) |
| 6 | AUTH | Roles y permisos | Gestión de roles | APIs CRUD de gestión de roles y permisos | Back | — | 48 | Nueva. Sujeta a resolución de P-01 |
| 7 | AUTH | Roles y permisos | Cambio de rol | Cambio de rol activo en sesión si el usuario tiene varios roles | Front | — | 16 | Nueva. No existe en el Excel. **Revisión Igor**: según arquitecto, el usuario logueado tendrá X roles asignados y no debería haber cambio de rol en mitad de sesión. Valorar eliminación si se confirma que Osabide Global resuelve el contexto de roles al autenticarse (ver P-01). Se mantiene por precaución hasta respuesta del cliente |
| 8 | AUTH | Roles y permisos | Cambio de rol | Lógica de cambio de rol activo: recarga de permisos y contexto | Back | — | 16 | Nueva. No existe en el Excel. **Revisión Igor**: misma observación que #7. Si no aplica cambio de rol en sesión, esta tarea se eliminaría junto con #7 (-32h). Condicionada a P-01 |
| 9 | AUTH | Modo acceso | Modo con/sin paciente | Lógica para admitir acceso con paciente asociado (cita activa) y sin paciente (gestión propia del facultativo) | Back | — | 24 | Nueva. El sistema debe diferenciar ambos modos y adaptar el listado de prescripciones en consecuencia |
| 10 | AUTH | Modo acceso | Modo con/sin paciente | Adaptación de interfaz según modo de acceso (con paciente: preselecciona paciente; sin paciente: muestra todas las prescripciones del facultativo) | Front | — | 16 | Nueva |
| 11 | CATÁLOGO | BBDD | Diseño BBDD | Diseño de base de datos del catálogo: campos del nomenclátor del Departamento + campos propios de Osakidetza | Back | T-007 | 40 | |
| 12 | CATÁLOGO | BBDD | Diseño BBDD | Creación y pruebas de base de datos del catálogo | Back | T-008 | 32 | |
| 13 | CATÁLOGO | BBDD | Gobierno de edición | Definición y desarrollo de campos propios de Osakidetza (activo sí/no, favoritos por facultativo, campos de caracterización de producto, campos adicionales para reglas de indicación) | Back | — | 48 | Nueva. Ampliada: incluye campos de caracterización de productos (decisión cliente 11/03/2026). **Revisión Igor**: opina que la definición de campos propios va incluida en T-007 (#11). Parcialmente cierto para campos simples (activo sí/no), pero la ampliación con campos de caracterización y reglas de indicación (decisión cliente 11/03) no estaba en el alcance original de T-007. Se mantiene como tarea separada por ese motivo; podría reducirse a ~32h si se absorbe la parte más básica en #11 |
| 14 | CATÁLOGO | Sincronización | Carga masiva por ficheros | Proceso de importación periódica de ficheros del nomenclátor del Departamento (~1.000 productos): lectura, parseo, validación de formato/contenido, carga en BBDD, gestión de errores (duplicados, campos faltantes, formatos incorrectos), log de auditoría de cada carga. NO se usa replicación BBDD (Golden Gate descartado por coste) | Back | T-009 | 60 | Actualizada: la carga es por importación de ficheros (CSV/XML/otro), no por sincronización genérica de BBDD |
| 15 | CATÁLOGO | Sincronización | Carga bajo demanda por ficheros | Ejecución manual del mismo proceso de importación de ficheros fuera de ciclo. Incluye subida manual del fichero por parte del administrador | Back | T-010 | 16 | Actualizada: misma lógica de ficheros que #14 pero ejecución manual |
| 16 | CATÁLOGO | Sincronización | Gestión de ficheros y failover | Mecanismo de recepción de ficheros del Departamento (SFTP, carpeta compartida o API de descarga), validación previa al procesamiento, gestión de reintentos si la importación falla, y garantía de disponibilidad 24x7 del catálogo local | Back | — | 40 | Actualizada: pasa de réplica BBDD a gestión de ficheros + failover local |
| 17 | CATÁLOGO | Gestión catálogo | Pantalla gestión | Pantalla de gestión/administración del catálogo: listado con filtros, ficha de producto editable (campos Osakidetza + campos de caracterización), activar/desactivar productos | Front | T-011 | 48 | Ampliada: incluye campos de caracterización de producto (decisión cliente 11/03/2026) |
| 18 | CATÁLOGO | Gestión catálogo | APIs catálogo | APIs CRUD de gestión del catálogo incluyendo campos de caracterización | Back | T-012 | 40 | Ampliada: incluye persistencia de caracterización |
| 19 | CATÁLOGO | Búsqueda | Pantalla búsqueda | Pantalla/diálogo de búsqueda de catálogo de productos, con filtros y acceso al detalle | Front | T-013 | 32 | |
| 20 | CATÁLOGO | Búsqueda | Filtro por tipo | Filtro de productos por tipo | Back | T-014 | 8 | |
| 21 | CATÁLOGO | Búsqueda | Filtro por familia | Filtro de producto por familia (grupo > subgrupo > categoría) | Back | T-015 | 16 | |
| 22 | CATÁLOGO | Búsqueda | Filtro por código | Filtro de producto por código | Back | T-016 | 8 | |
| 23 | CATÁLOGO | Búsqueda | Filtro por descripción | Filtro de producto por descripción (texto libre) | Back | — | 8 | Nueva. Los filtros del Excel no incluyen búsqueda por descripción |
| 24 | CATÁLOGO | Selección | Pantalla selección | Pantalla de selección de productos dentro de la prescripción: favoritos primero + productos similares | Front | T-017 | 40 | |
| 25 | CATÁLOGO | Selección | Productos no disponibles | Mostrar todos los productos del catálogo, incluso los que el facultativo no puede prescribir (aparecen como no disponibles para que pueda solicitar permisos) | Front | — | 16 | Nueva. RN-13: productos sin permiso visibles pero marcados como no disponibles |
| 26 | CATÁLOGO | Selección | Productos no disponibles | Validación back: marcar productos como no disponibles según permisos del facultativo | Back | — | 16 | Nueva. Complemento back de #25 |
| 27 | CATÁLOGO | Favoritos | Pantalla favoritos | Pantalla de gestión de favoritos del facultativo | Front | T-018 | 24 | |
| 28 | CATÁLOGO | Favoritos | Sistema favoritos | Sistema de gestión de favoritos: almacenamiento en BBDD de Osakidetza, marcado por el facultativo desde la prescripción | Back | T-019 | 16 | |
| 29 | PRESCRIPCIÓN | BBDD | Diseño BBDD | Diseño de base de datos de prescripciones (prescripción, materiales, estados, histórico, adjuntos) | Back | T-020 | 48 | |
| 30 | PRESCRIPCIÓN | BBDD | Diseño BBDD | Creación y pruebas de BD de prescripciones | Back | T-021 | 32 | |
| 31 | PRESCRIPCIÓN | Listado | Pantalla listado | Pantalla de consulta/listado de prescripciones con filtros (por paciente, por facultativo, por estado, por fecha, por OSI, por tipo producto) | Front | T-022 | 48 | |
| 32 | PRESCRIPCIÓN | Listado | APIs búsqueda | APIs de búsqueda/consulta de prescripciones con filtros | Back | T-023 | 40 | |
| 33 | PRESCRIPCIÓN | Listado | Indicador visual | Indicador visual de estado de dispensación en el listado (icono/color + columna de estado textual) | Front | — | 8 | Nueva. Sin ella el prescriptor no identifica visualmente el estado |
| 34 | PRESCRIPCIÓN | Detalle | API detalle | API consulta detalles de una prescripción | Back | T-024 | 24 | |
| 35 | PRESCRIPCIÓN | Detalle | Pantalla detalle | Pantalla de consulta de detalle de prescripción (modo lectura, datos completos, estado de cada material) | Front | T-025 | 40 | |
| 36 | PRESCRIPCIÓN | Detalle | Histórico | Pantalla de histórico de la prescripción: acciones realizadas, cambios de estado, fechas | Front | — | 24 | Nueva. No existe en el Excel |
| 37 | PRESCRIPCIÓN | Detalle | Histórico | API/servicio de histórico/auditoría de la prescripción | Back | — | 24 | Nueva. No existe en el Excel |
| 38 | PRESCRIPCIÓN | Detalle | Documentos adjuntos | Visualización y descarga de documentos adjuntos (informe clínico, CSV firmado) | Front | — | 16 | Nueva. Implícita pero no tiene tarea propia |
| 39 | PRESCRIPCIÓN | Creación | Pantalla creación | Pantalla de creación de prescripción con cabecera precargada (datos paciente + datos facultativo) | Front | T-026 | 60 | |
| 40 | PRESCRIPCIÓN | Creación | Recuperar info facultativo | Recuperar información del facultativo desde contexto Osabide Global o directorio corporativo (nº colegiado, especialidad, centro, servicio) | Back | T-027 | 40 | Revisar: no especifica si es API a SAP, BBDD directa o ambas |
| 41 | PRESCRIPCIÓN | Creación | Recuperar info paciente | Recuperar información del paciente desde Osategi vía CIC (TIS, CIP, nombre, sexo, nacimiento, domicilio) | Back | T-028 | 40 | Revisar: no especifica si es servicio web Osategi o BBDD directa |
| 42 | PRESCRIPCIÓN | Creación | Añadir materiales | Añadir materiales/productos a la prescripción desde el buscador de catálogo | Front | T-029 | 24 | |
| 43 | PRESCRIPCIÓN | Creación | Visado obligar informe | Si el producto requiere visado, obligar a adjuntar informe clínico (RN-02) | Front | T-030 | 16 | |
| 44 | PRESCRIPCIÓN | Creación | Catálogo indicadores | Considerar catálogo de indicadores por producto (visado, protocolo, campos adicionales) | Front | T-031 | 16 | Revisar: ¿solapamiento con #43 y #45? Valorar si es tarea independiente o parte de la pantalla de creación |
| 45 | PRESCRIPCIÓN | Creación | Protocolo campos adicionales | Si el producto tiene protocolo, mostrar campos adicionales del protocolo en el formulario | Front | — | 20 | Nueva. Derivada de §3.2 del enfoque |
| 46 | PRESCRIPCIÓN | Creación | Protocolo campos adicionales | Lógica back para gestionar campos de protocolo por producto | Back | — | 24 | Nueva |
| 47 | PRESCRIPCIÓN | Edición | Pantalla edición | Pantalla de edición de prescripción existente (si el estado lo permite) | Front | — | 32 | Nueva como tarea front independiente. T-034 cubre solo la API back |
| 48 | PRESCRIPCIÓN | Creación | Guardar borrador | Guardar prescripción como borrador (sin firmar) | Front | — | 8 | Nueva. Implícita en T-033 pero no tiene tarea front propia |
| 49 | PRESCRIPCIÓN | Firma | Firmar prescripción | Firmar y autorizar prescripción desde interfaz (integración Giltza/Izenpe) | Front | T-032 | 24 | Revisar: 10h puede ser insuficiente para la integración con Giltza/Izenpe |
| 50 | PRESCRIPCIÓN | Firma | Firmar y generar | Firmar y generar prescripción en back: firma digital, generación de CSV/documento firmado | Back | T-040 | 40 | Es el par back de T-032; no es redundante sino complementario |
| 51 | PRESCRIPCIÓN | APIs CRUD | API creación | API de creación de prescripción | Back | T-033 | 40 | |
| 52 | PRESCRIPCIÓN | APIs CRUD | API edición | API de edición de prescripción | Back | T-034 | 32 | |
| 53 | PRESCRIPCIÓN | APIs CRUD | API eliminación | API de eliminación de prescripción (solo borrador/pendiente de firma) | Back | T-035 | 16 | |
| 54 | PRESCRIPCIÓN | Listado | Acción eliminar | Acción de eliminar prescripción desde el listado (front) | Front | — | 8 | Nueva. T-035 cubre la API back pero falta la acción en front |
| 55 | PRESCRIPCIÓN | APIs CRUD | API clonar | API de clonar/copiar prescripción (elimina materiales no válidos para la especialidad) | Back | T-036 | 32 | |
| 56 | PRESCRIPCIÓN | Listado | Acción copiar | Acción de copiar/duplicar prescripción desde el listado (front) | Front | — | 8 | Nueva. T-036 cubre la API back pero falta la acción en front |
| 57 | PRESCRIPCIÓN | APIs CRUD | API anular | API de anular prescripción (si no dispensada ni anulada) | Back | T-037 | 20 | |
| 58 | PRESCRIPCIÓN | Listado | Acción anular | Acción de anular prescripción desde el listado (front) | Front | — | 8 | Nueva. T-037 cubre la API back |
| 59 | PRESCRIPCIÓN | APIs CRUD | API renovar | API de renovar prescripción (crea prescripción de renovación) | Back | T-038 | 32 | |
| 60 | PRESCRIPCIÓN | Listado | Acción renovar | Acción de renovar prescripción desde el listado (front): si es temprana, solicitar justificación clínica | Front | — | 16 | Nueva. T-038 cubre la API back; falta el front |
| 61 | PRESCRIPCIÓN | Validación | Validar prescripción | Validar prescripción: aplicar reglas de negocio (unidad clínica, visado, motivo, estados) | Back | T-039 | 40 | |
| 62 | PRESCRIPCIÓN | Validación | Validar unidad clínica | Validar que el prescriptor solo puede prescribir productos de su unidad clínica/especialidad (RN-01) | Back | — | 20 | Nueva. T-039 es genérica; esta regla necesita implementación específica |
| 63 | PRESCRIPCIÓN | Validación | Validar motivo especial | Validar motivo accidente de trabajo / enfermedad profesional: intervención adicional, comunicación al sistema de visado (RN-04) | Back | — | 16 | Nueva. No existe en el Excel |
| 64 | PRESCRIPCIÓN | Validación | Validar rechazada no reabrir | Validar que prescripción rechazada por inspección no se puede reabrir (RN-05) | Back | — | 8 | Nueva. No existe en el Excel |
| 65 | PRESCRIPCIÓN | Impresión | Imprimir prescripción | Imprimir prescripción desde interfaz (genera PDF oficial para entrega al paciente) | Front | T-041 | 12 | |
| 66 | PRESCRIPCIÓN | Impresión | Imprimir prescripción | Generación de PDF de prescripción (back): plantilla oficial Osakidetza | Back | T-042 | 40 | |
| 67 | PRESCRIPCIÓN | Impresión | Descargar informe | Descargar informe/CSV de la prescripción firmada | Back | T-043 | 16 | |
| 68 | PRESCRIPCIÓN | Exportación | Exportar Excel | Exportar listado filtrado de prescripciones a Excel | Back | T-044 | 24 | |
| 69 | PRESCRIPCIÓN | Renovación | Prescripción recurrente | Renovación de prescripción: considerar renovación a tiempo y renovación temprana (exige justificación clínica escrita, RN-07) | Back | T-045 | 24 | Revisar: 20h puede ser insuficiente si incluye toda la lógica de justificación de renovación temprana. ¿Solapamiento con #59 (API renovar)? Valorar si T-045 es redundante con T-038 o si son complementarias |
| 70 | PRESCRIPCIÓN | Máquina estados | Estados prescripción | Implementación de la lógica de transiciones de estado de la prescripción (8 estados, transiciones definidas en §3.4). No requiere framework formal de state machine; se trata de codificar las transiciones permitidas, validaciones de cambio de estado y eventos asociados como lógica de negocio | Back | — | 48 | Nueva. Crítica. No existe como tarea independiente en el Excel. **Revisión Igor**: desaconseja usar un patrón de máquina de estados formal y sugiere manejar estados sin ese patrón. De acuerdo: no se propone un framework (Spring Statemachine o similar), sino la implementación de las reglas de transición como lógica de negocio. La tarea sigue siendo necesaria porque los 8 estados con sus transiciones deben codificarse y testearse independientemente de cómo se implementen |
| 71 | PRESCRIPCIÓN | Máquina estados | Estados material | Implementación de la lógica de transiciones de estado del material (10 estados, transiciones definidas en §3.5). No requiere framework formal de state machine; misma aproximación que #70 aplicada a los estados del material | Back | — | 48 | Nueva. Crítica. No existe como tarea independiente en el Excel. **Revisión Igor**: misma observación que #70. Se clarifica que no implica framework de máquina de estados |
| 72 | PRESCRIPCIÓN | Caducidad | Proceso caducidad | Proceso automático de caducidad: job/scheduler que marca como "No vigente" las prescripciones no dispensadas en plazo (configurable, propuesta 6 meses, RN-10) | Back | — | 20 | Nueva. No existe en el Excel |
| 73 | PRESCRIPCIÓN | Nº Expediente | Generación expediente | Generación del nº de expediente de la prescripción (pendiente definir origen — P-02) | Back | — | 12 | Nueva. Sujeta a resolución de P-02 |
| 74 | DISPENSACIÓN | APIs interop. | Consulta dispensables | API de consulta de prescripciones dispensables por paciente (TIS) | Back | T-050 | 32 | |
| 75 | DISPENSACIÓN | APIs interop. | Bloquear material | API para bloquear material (reservado por un establecimiento; RN-09) | Back | T-051 | 24 | Revisar: el Excel dice "Bloquear prescripción" pero el enfoque es por material, no por prescripción. **Revisión Igor**: indica que el requerimiento original era bloquear la prescripción completa, no por material. Discrepancia crítica: si la dispensación es parcial (material a material), el bloqueo debería ser por material; si es por prescripción completa, cambia la arquitectura de dispensación. **Requiere resolución urgente — ver P-11** |
| 76 | DISPENSACIÓN | APIs interop. | Desbloquear material | API para desbloquear material | Back | T-052 | 16 | Revisar: mismo comentario que #75, es por material |
| 77 | DISPENSACIÓN | APIs interop. | Recibir dispensación | Recibir información de dispensación (API/evento): actualizar estado del material a Dispensado, registrar fecha, establecimiento | Back | T-053 | 40 | |
| 78 | DISPENSACIÓN | Visado | Enviar solicitud visado | Enviar solicitud de visado al Departamento al firmar prescripción con material que requiere visado | Back | — | 24 | Nueva. T-054 mezcla envío y recepción; deberían ser 2 tareas separadas. **Revisión Igor**: indica que actualmente NO existe canal electrónico para enviar la solicitud al Departamento; el proceso es con papel que el propio paciente lleva. Si se confirma, esta tarea debería transformarse en "generar documento de solicitud de visado para impresión" (podría absorberse en #66, generación de PDF). **Requiere resolución — ver P-12** |
| 79 | DISPENSACIÓN | Visado | Recibir estado visado | Servicio receptor de estado de visado (push inmediato del Departamento): actualizar estado de prescripción | Back | T-054 | 40 | Revisar: T-054 no diferencia solicitud (ida) de recepción (vuelta). La estimación de 60h debería repartirse entre #78 y #79 |
| 80 | DISPENSACIÓN | Validación post-disp. | Validación prescriptor | Pantalla/acción para que el prescriptor valide o rechace un material dispensado que requiere validación clínica | Front | — | 16 | Nueva. Derivada del modelo de estados del material (§3.5). **Revisión Igor**: cuestiona si es requerimiento nuevo. Es funcionalidad derivada de la lógica de estados (no invención), pero es un flujo secundario. Prioridad F5 (no critical path); si al llegar a esa fase el cliente no la necesita, se puede eliminar sin impacto |
| 81 | DISPENSACIÓN | Validación post-disp. | Validación prescriptor | Lógica back de validación post-dispensación: cambiar estado material según decisión del prescriptor | Back | — | 16 | Nueva. Derivada del modelo de estados del material. **Revisión Igor**: misma observación que #80. Prioridad F5; eliminable si el cliente no la necesita |
| 82 | DISPENSACIÓN | Dispensación parcial | Visualización parcial | Visualización del estado material a material en prescripciones con dispensación parcial (front) | Front | — | 16 | Nueva. Sujeta a definición UX (P-08) |
| 83 | DISPENSACIÓN | Dispensación parcial | Lógica parcial | Lógica de dispensación parcial: gestionar estados independientes por material dentro de una prescripción (RN-16) | Back | — | 24 | Nueva |
| 84 | TAREAS | Tarea visado | Crear tarea | Crear tarea pendiente cuando la prescripción pasa a "Pendiente inspección" (requiere visado) | Back | T-046 | 16 | |
| 85 | TAREAS | Tarea visado | Actualizar tarea | Actualizar tarea cuando cambia el estado de visado (aprobado/rechazado/solicitud modificación) | Back | T-047 | 16 | |
| 86 | TAREAS | Tarea validación | Tarea validación | Crear tarea pendiente cuando un material dispensado requiere validación del prescriptor | Back | — | 16 | Nueva. Derivada del flujo de validación post-dispensación (#80/#81). **Revisión Igor**: misma observación — vinculada a #80/#81. Si la validación post-dispensación no se implementa, esta tarea también se elimina. Prioridad F5 |
| 87 | TAREAS | Tarea dispensación | Tarea dispensación | Crear aviso cuando todos los materiales de una prescripción se dispensan (cierre de ciclo) | Back | — | 12 | Nueva. No existe en el Excel |
| 88 | TAREAS | Pantalla tareas | Pantalla tareas | Pantalla de visualización de tareas pendientes: visados pendientes, rechazados, modificaciones solicitadas, dispensaciones pendientes de validación | Front | T-048 | 40 | |
| 89 | TAREAS | APIs tareas | APIs tareas | APIs de gestión de tareas pendientes (listado, marcar como vista, histórico) | Back | T-049 | 32 | |
| 90 | TAREAS | Dashboard | Avisos al entrar | Dashboard/pantalla de avisos al entrar al módulo: resumen de pendientes antes de acceder al listado | Front | — | 24 | Nueva. No existe en el Excel |
| 91 | TAREAS | Dashboard | Avisos al entrar | API de resumen de pendientes para el dashboard de entrada | Back | — | 20 | Nueva |
| 92 | MANTENIMIENTO | Establecimientos | Pantalla establecimientos | Pantalla de gestión de establecimientos (listado, alta, edición, baja) | Front | — | 24 | Nueva. **Revisión Igor**: cuestiona si la gestión de establecimientos (ortopedias) es competencia de Osakidetza o del Departamento. Si el catálogo de establecimientos lo mantiene el Departamento y llega como dato maestro (similar al nomenclátor), Osakidetza no necesita CRUD propio y esta tarea se eliminaría. **Requiere resolución — ver P-13** |
| 93 | MANTENIMIENTO | Establecimientos | APIs establecimientos | APIs CRUD de gestión de establecimientos | Back | — | 16 | Nueva. **Revisión Igor**: misma observación que #92. Condicionada a P-13 |
| 94 | MANTENIMIENTO | Configuraciones | Pantalla configuraciones | Pantalla de configuración del sistema (plazos de caducidad, sincronización, parámetros operativos) | Front | — | 24 | Nueva como front. T-003 solo cubre back |
| 95 | MANTENIMIENTO | Configuraciones | API configuraciones | API de gestión de configuraciones del sistema | Back | T-003 | 24 | T-003 cubre configuraciones del sistema (no incluye roles, que van en #5/#6). **Revisión Igor**: confirma que T-003 siempre fue solo configuraciones, no roles |
| 96 | TRANSVERSAL | Multi-idioma | Multi-idioma front | Internacionalización del front: euskera / castellano | Front | T-001 | 48 | Revisar: 60h. ¿El framework ya soporta i18n? Si sí, la estimación podría reducirse |
| 97 | TRANSVERSAL | Multi-idioma | Multi-idioma back | Internacionalización del back: mensajes, validaciones, errores en euskera / castellano | Back | T-002 | 40 | Revisar: 60h. Mismo comentario que #96 |
| 98 | TRANSVERSAL | Unificación pacientes | Unificación pacientes | Modificar el proceso de unificación de pacientes existente en Osakidetza para incluir prescripciones ortoprotésicas | Back | — | 24 | Nueva. **Revisión Igor**: indica que se decidió no tocar este proceso por ahora, ya que requiere cambiar el proceso globalmente para Departamento, Osakidetza y establecimientos. Si se confirma, esta tarea se eliminaría del alcance (-24h) y quedaría como requisito futuro. **Requiere resolución — ver P-14** |
| 99 | TRANSVERSAL | Módulo SOA | Servicio terceros | Creación de módulo/servicio para exponer datos de prescripciones a otros sistemas de Osakidetza (servicio de consulta para terceros) | Back | T-055 | 40 | |
| 100 | TRANSVERSAL | QA | QA front | Pruebas y tests unitarios: front (plan de pruebas de casos de uso) | Front | T-056 | 120 | Revisar: 120h (~10% del desarrollo); con la complejidad de la máquina de estados podría quedarse corto |
| 101 | TRANSVERSAL | QA | QA back | Pruebas y tests unitarios: back | Back | T-057 | 120 | Revisar: 120h; mismo comentario que #100 |
| 102 | TRANSVERSAL | ETL Reporting | ETL datos reporting | ETL de extracción de datos de prescripciones y carga en BBDD de reporting | Back | T-058 | 0 (ELIMINADA) | ELIMINADA DEL ALCANCE. Reporting/ETL fue excluido del proyecto; esta tarea debería desaparecer |
| 103 | MANTENIMIENTO | Reglas indicación | Modelo de datos reglas | Diseño e implementación del modelo de datos para reglas de indicación por producto: tipos de regla (especialidad, edad, sexo, diagnóstico, límite renovación, requisito documental, etc.), condiciones, acciones, vigencia | Back | — | 48 | Nueva (decisión cliente 11/03/2026). Crítica: sin modelo de reglas no se puede implementar la validación |
| 104 | MANTENIMIENTO | Reglas indicación | Pantalla admin reglas | Pantalla de administración de reglas de indicación: crear, editar, desactivar reglas por producto o grupo de productos. Incluye vista de reglas vigentes y histórico | Front | — | 48 | Nueva (decisión cliente 11/03/2026) |
| 105 | MANTENIMIENTO | Reglas indicación | APIs CRUD reglas | APIs CRUD para gestión de reglas de indicación (crear, editar, desactivar, consultar por producto) | Back | — | 32 | Nueva (decisión cliente 11/03/2026) |
| 106 | MANTENIMIENTO | Reglas indicación | Motor validación reglas | Motor/servicio de validación que aplica las reglas de indicación configuradas cuando un facultativo prescribe un producto. Devuelve errores/advertencias si no se cumplen condiciones. Consumido por el Módulo 3 (Prescripción) | Back | — | 48 | Nueva (decisión cliente 11/03/2026). Crítica: conecta mantenimiento con prescripción |
| 107 | PRESCRIPCIÓN | Validación | Integrar reglas indicación | Integrar en el flujo de prescripción la llamada al motor de validación de reglas de indicación: al añadir producto, mostrar errores/advertencias basados en reglas configuradas | Front | — | 24 | Nueva (decisión cliente 11/03/2026). Complemento front del motor de validación |
| 108 | CATÁLOGO | Sincronización | Log importación ficheros | Pantalla de consulta del log/histórico de importaciones de ficheros: fecha, fichero procesado, registros cargados, errores detectados, estado de la carga | Front | — | 24 | Nueva. Necesaria para trazabilidad de las cargas por fichero |

---

## 8. Resumen de estimación

### 8.1 Resumen general

| Concepto | Cantidad |
|---|---|
| Tareas totales (activas) | 107 |
| Tareas del Excel original conservadas | 48 |
| Tareas nuevas (no estaban en el Excel) | 59 |
| Tareas eliminadas del alcance | 1 (T-058 ETL, #102) |
| Tareas añadidas por decisiones cliente 11/03/2026 | 6 (#103–#108) |

### 8.2 Horas por módulo

| Módulo | Tareas | Horas Front | Horas Back | Total horas |
|---|---|---|---|---|
| AUTH (Autenticación) | #1–#10 | 136 | 144 | **280** |
| CATÁLOGO (Nomenclátor) | #11–#28, #108 | 184 | 348 | **532** |
| PRESCRIPCIÓN (Núcleo) | #29–#73, #107 | 432 | 760 | **1.192** |
| DISPENSACIÓN | #74–#83 | 32 | 216 | **248** |
| TAREAS (Avisos) | #84–#91 | 64 | 112 | **176** |
| MANTENIMIENTO | #92–#95, #103–#106 | 96 | 168 | **264** |
| TRANSVERSAL | #96–#101 | 168 | 224 | **392** |
| **TOTAL** | **107 activas** | **1.112** | **1.972** | **3.084** |

### 8.3 Comparativa con Excel original

| Concepto | Excel original | V7 estimación | Delta |
|---|---|---|---|
| Horas Back | 1.630 | 1.972 | +342 (+21,0%) |
| Horas Front | 650 | 1.112 | +462 (+71,1%) |
| **Total** | **2.280** | **3.084** | **+804 (+35,3%)** |

**Justificación del incremento (+35%)**:

El Excel original contenía 58 tareas. Se han identificado 59 tareas nuevas que no existían (aumento del 85% en el número de tareas). El incremento de horas (+35%) es proporcionalmente inferior al de tareas porque las nuevas son de menor alcance promedio:

- **Tareas originales conservadas** (48): media de ~46h/tarea (sin cambios sustanciales).
- **Tareas nuevas** (59): media de ~14h/tarea (acciones front faltantes, validaciones específicas, máquinas de estados, avisos, configuración).

Desglose del incremento:
- 37 acciones front que faltaban para APIs back existentes (+244h): pantalla edición, acciones eliminar/copiar/anular/renovar, indicadores visuales, histórico, adjuntos, dashboard, configuraciones, establecimientos, dispensación parcial, reglas indicación.
- 2 máquinas de estados (prescripción + material) que el Excel no contemplaba como tarea independiente (+96h): RN críticas del sistema.
- 6 tareas de decisión del cliente 11/03/2026 (+224h): reglas de indicación + log importación ficheros.
- 14 tareas de validaciones, lógica y procesos complementarios (+240h): protocolo, caducidad, unificación pacientes, gobierno de datos catálogo.
- QA se mantiene en 240h (estimación original, no incrementada).
- Firma digital front ajustada de 10h a 24h por integración Giltza (+14h).
- Visado separado en envío + recepción (+12h neto).
- Eliminación de ETL Reporting (-60h).

**Nota sobre el margen**: Se ha recortado relleno excesivo en 12 tareas que en V6 tenían estimaciones generosas. Total recortado: -116h. Las estimaciones actuales incluyen un margen moderado (~10-15%) sobre el esfuerzo base.

### 8.4 Tareas con ajustes respecto a V6

| # | Tarea | V6 | V7 | Δ | Motivo del ajuste |
|---|---|---|---|---|---|
| 2 | Validación token back | 32h | 24h | -8h | Alcance acotado: parsing de token + consulta contexto |
| 33 | Indicador visual estado | 12h | 8h | -4h | Componente UI sencillo (icono + color) |
| 37 | Histórico API | 32h | 24h | -8h | Log de auditoría con framework estándar |
| 78 | Enviar solicitud visado | 32h | 24h | -8h | Composición y envío de mensaje a API conocida |
| 80 | Validación prescriptor front | 24h | 16h | -8h | Diálogo simple aprobar/rechazar |
| 81 | Validación prescriptor back | 24h | 16h | -8h | Cambio de estado puntual, lógica definida |
| 83 | Dispensación parcial back | 32h | 24h | -8h | Lógica de estados independientes, bien acotada |
| 92 | Establecimienots pantalla | 32h | 24h | -8h | CRUD estándar, sin lógica compleja |
| 93 | Establecimientos APIs | 24h | 16h | -8h | APIs CRUD básicas |
| 98 | Unificación pacientes | 32h | 24h | -8h | Modificación de proceso existente, no nuevo |
| 100 | QA front | 140h | 120h | -20h | Se mantiene estimación original (T-056), suficiente con plan de pruebas estructurado |
| 101 | QA back | 140h | 120h | -20h | Se mantiene estimación original (T-057), ídem |
| | | | **Total recorte** | **-116h** | |

### 8.5 Tareas con notas de revisión pendiente

| # | Tarea | Ref. Excel | Horas Excel | Horas V7 | Observación |
|---|---|---|---|---|---|
| 44 | Catálogo indicadores | T-031 | 20h | 16h | Posible solapamiento con #43 y #45; valorar unificar |
| 49 | Firmar prescripción front | T-032 | 10h | 24h | Ajustada al alza por integración Giltza/Izenpe |
| 69 | Prescripción recurrente | T-045 | 20h | 24h | Posible redundancia con #59 (API renovar); valorar unificar |
| 79 | Recibir estado visado | T-054 | 60h | 40h | Split: #78 (envío, 24h) + #79 (recepción, 40h) = 64h total |
| 95 | API configuraciones | T-003 | 40h | 24h | Roles separados a tareas #5/#6; esta solo cubre configuraciones |
| 96–97 | Multi-idioma | T-001/002 | 120h | 88h | Reducida asumiendo que el framework soporta i18n base |
| 100–101 | QA | T-056/057 | 240h | 240h | Se mantiene estimación original; suficiente con plan estructurado |
| 102 | ETL Reporting | T-058 | 60h | 0h | **ELIMINADA** del alcance |

---

## 9. Planificación: equipo, fases y cronograma

### 9.1 Composición del equipo propuesto

| Rol | Perfil | Dedicación | Fases activo | Responsabilidad principal |
|---|---|---|---|---|
| **Jefe de Proyecto (JP)** | PM senior, experiencia en Administración Pública | 100% | FP–F6 | Planificación, seguimiento, gestión de riesgos, interlocución con cliente, coordinación de equipos |
| **Analista Funcional (BA)** | Analista funcional senior, conocimiento dominio sanitario | 100% FP; 50% F0–F6 | FP–F6 | Especificación funcional, validación con usuarios, criterios de aceptación, soporte a desarrollo |
| **UX Designer** | Diseñador UX/UI senior | 100% FP; 25% F0–F2 | FP–F2 | Investigación usuarios, wireframes, prototipos, guía de estilo, validación usabilidad |
| **Tech Lead / Arquitecto** | Desarrollador senior back | 100% | F0–F6 | Arquitectura, diseño BBDD, máquina de estados, revisión de código |
| **Backend Dev 1** | Desarrollador back mid-senior | 100% | F0–F6 | APIs CRUD, validaciones, lógica de negocio |
| **Backend Dev 2** | Desarrollador back mid | 100% | F1–F5 | Sincronización ficheros, dispensación, tareas, mantenimiento |
| **Frontend Dev 1** | Desarrollador front senior | 100% | F0–F6 | Pantallas principales (prescripción, catálogo, dashboard) |
| **Frontend Dev 2** | Desarrollador front mid | 100% | F2–F5 | Pantallas secundarias (tareas, mantenimiento, reglas, edición) |
| **Esp. Integración** | Desarrollador back con experiencia en integraciones | 60% | F0–F4 | Osabide Global, Osategi, SAP, Giltza, visado, dispensación |
| **QA / Tester** | Tester funcional + automatización | 100% | F2–F6 | Plan de pruebas, tests unitarios, regresión, validación estados |

**Capacidad por fase**:
- **FP (previa)**: JP + BA + UX = 3 personas (no consume horas de desarrollo).
- **F0–F2**: ~5,5 FTE desarrollo + JP (100%) + BA (50%) + UX (25%) = equipo completo.
- **F3–F6**: ~5,5 FTE desarrollo + JP (100%) + BA (50%). UX disponible bajo demanda.

### 9.2 Cronograma por fases

| Fase | Nombre | Duración | Semanas | Horas dev | Equipo activo |
|---|---|---|---|---|---|
| **FP** | Fase previa: UX + análisis funcional | 6 semanas | S-6 a S-1 | — (no dev) | JP, BA, UX |
| **F0** | Fundamentos | 3 semanas | S1 a S3 | ~328h | Tech Lead, Back1, Front1, Integ |
| **F1** | Catálogo y ficheros | 3 semanas | S4 a S6 | ~420h | Tech Lead, Back1, Back2, Front1, Integ |
| **F2** | Prescripción core | 4 semanas | S7 a S10 | ~936h | Todos (6 devs + QA) |
| **F3** | Firma y visado | 2 semanas | S11 a S12 | ~244h | Tech Lead, Back1, Front1, Integ, QA |
| **F4** | Dispensación y tareas | 3 semanas | S13 a S15 | ~368h | Todos (6 devs + QA) |
| **F5** | Mantenimiento y reglas | 3 semanas | S16 a S18 | ~396h | Tech Lead, Back1, Back2, Front1, Front2, QA |
| **F6** | Transversales y cierre | 3 semanas | S19 a S21 | ~392h | Back1, Front1, QA |
| | **TOTAL DESARROLLO** | **21 semanas** | | **~3.084h** | |
| | **TOTAL PROYECTO** | **27 semanas** | | | |

**Duración total estimada: 6 sem. fase previa + 21 sem. desarrollo = 27 semanas (~6,5 meses)**.

(*) Las semanas de desarrollo (S1–S21) comienzan después de la fase previa. Las fechas concretas dependen de la fecha de arranque.

### 9.3 Fase Previa (FP) — Diseño UX y análisis funcional (6 semanas)

Objetivo: producir la especificación funcional completa, wireframes validados y prototipos navegables antes de iniciar el desarrollo.

| Semana | Actividad principal | Entregable |
|---|---|---|
| S-6 a S-5 | Investigación de usuarios y flujos: entrevistas con facultativos, observación en consulta, revisión de GELPO Aragón como referencia | Mapa de flujos de usuario, personas, pain points |
| S-4 a S-3 | Wireframes de todas las pantallas del sistema (listado, creación/edición, detalle, catálogo, tareas, mantenimiento, configuración) | Wireframes lo-fi completos, validados con BA |
| S-3 a S-2 | Prototipos navegables de los flujos principales (prescripción completa, firma, dispensación parcial, dashboard avisos) | Prototipo hi-fi clickable |
| S-2 a S-1 | Validación con usuarios reales (1–2 sesiones con facultativos de Osakidetza) + ajustes | Informe de usabilidad, wireframes finales, guía de estilo UI |
| Transversal | BA: especificaciones funcionales detalladas, criterios de aceptación por historia, resolución de preguntas abiertas | Documento funcional completo, backlog priorizado |
| Transversal | JP: plan de proyecto detallado, kick-off con equipo técnico, gestión de dependencias externas | Plan de proyecto, actas, registro de riesgos |

**Entregables clave de FP**:
- Wireframes y prototipos validados → input directo para Frontend Dev 1 y 2.
- Especificación funcional con criterios de aceptación → input para todos los desarrolladores.
- Resolución de preguntas abiertas P-01 a P-10 (o escalamiento formal si el cliente no responde).
- Solicitud formal de documentación a dependencias externas (Giltza, Osategi, formato ficheros).

### 9.4 Asignación de tareas por fase de desarrollo

#### F0 — Fundamentos (semanas S1–S3)

Objetivo: arquitectura base, diseño de BBDD, autenticación y acceso operativos.

| Tareas | Módulo | Horas |
|---|---|---|
| #1, #2, #3, #4, #9, #10 | AUTH (login + modo acceso) | 160 |
| #11 | CATÁLOGO (diseño BBDD) | 40 |
| #29 | PRESCRIPCIÓN (diseño BBDD) | 48 |
| Arquitectura, entornos, CI/CD | Infraestructura | ~80 (no tarea explícita) |
| **Subtotal F0** | | **~328h** |

Dependencias críticas: Especificación del token de Osabide Global (DEP-01), acceso a LDAP corporativo (DEP-02). Deben estar resueltas en FP.

#### F1 — Catálogo y sincronización por ficheros (semanas S4–S6)

Objetivo: catálogo operativo con carga desde ficheros del Departamento.

| Tareas | Módulo | Horas |
|---|---|---|
| #12, #13, #14, #15, #16 | CATÁLOGO (BBDD + sincronización) | 196 |
| #17, #18 | CATÁLOGO (gestión) | 88 |
| #19, #20, #21, #22, #23 | CATÁLOGO (búsqueda) | 72 |
| #27, #28 | CATÁLOGO (favoritos) | 40 |
| #108 | CATÁLOGO (log importación) | 24 |
| **Subtotal F1** | | **~420h** |

Dependencias críticas: Formato y protocolo del fichero del Departamento (P-09), definición de campos de caracterización (P-10). Deben avanzarse en FP.

#### F2 — Prescripción core (semanas S7–S10)

Objetivo: CRUD completo de prescripciones, máquina de estados, validaciones de negocio.

| Tareas | Módulo | Horas |
|---|---|---|
| #24, #25, #26 | CATÁLOGO (selección en prescripción) | 72 |
| #30–#48, #51–#62, #64, #68–#73 | PRESCRIPCIÓN (core completo) | ~864 |
| **Subtotal F2** | | **~936h** |

Dependencias críticas: Servicio Osategi operativo (DEP-03), datos SAP RRHH accesibles (DEP-04).

#### F3 — Firma digital y visado (semanas S11–S12)

Objetivo: firma Giltza/Izenpe integrada, circuito de visado completo.

| Tareas | Módulo | Horas |
|---|---|---|
| #49, #50 | PRESCRIPCIÓN (firma) | 64 |
| #63 | PRESCRIPCIÓN (validación motivo especial) | 16 |
| #65, #66, #67 | PRESCRIPCIÓN (PDF e impresión) | 68 |
| #78, #79 | DISPENSACIÓN (visado ida/vuelta) | 64 |
| #84, #85 | TAREAS (tareas de visado) | 32 |
| **Subtotal F3** | | **~244h** |

Dependencias críticas: Documentación API Giltza (DEP-06), contrato de visado con Departamento (DEP-07).

#### F4 — Dispensación, tareas y cierre de ciclo (semanas S13–S15)

Objetivo: APIs de dispensación integradas, tareas/avisos operativos, cierre del ciclo asistencial.

| Tareas | Módulo | Horas |
|---|---|---|
| #74, #75, #76, #77 | DISPENSACIÓN (APIs interop.) | 112 |
| #80, #81, #82, #83 | DISPENSACIÓN (validación post + parcial) | 72 |
| #72 | PRESCRIPCIÓN (caducidad automática) | 20 |
| #86, #87, #88, #89, #90, #91 | TAREAS (avisos + pantallas) | 164 |
| **Subtotal F4** | | **~368h** |

Dependencias críticas: Contrato API dispensación con ortopedias (DEP-08, P-07).

#### F5 — Mantenimiento, reglas de indicación y roles (semanas S16–S18)

Objetivo: módulo de mantenimiento completo, reglas de indicación operativas, gestión de roles.

| Tareas | Módulo | Horas |
|---|---|---|
| #92, #93 | MANTENIMIENTO (establecimientos) | 40 |
| #94, #95 | MANTENIMIENTO (configuraciones) | 48 |
| #103, #104, #105, #106 | MANTENIMIENTO (reglas indicación) | 176 |
| #107 | PRESCRIPCIÓN (integrar reglas en front) | 24 |
| #5, #6, #7, #8 | AUTH (roles — condicional a P-01) | 120 |
| **Subtotal F5** | | **~408h** |

Dependencias: Resolución de P-01 (roles), definición de catálogo de reglas (P-10).

#### F6 — Transversales y cierre (semanas S19–S21)

Objetivo: multi-idioma, servicio SOA, pruebas finales de integración, regresión completa.

| Tareas | Módulo | Horas |
|---|---|---|
| #96, #97 | TRANSVERSAL (multi-idioma) | 88 |
| #98 | TRANSVERSAL (unificación pacientes) | 24 |
| #99 | TRANSVERSAL (servicio terceros SOA) | 40 |
| #100, #101 | TRANSVERSAL (QA final, regresión) | 240 |
| **Subtotal F6** | | **~392h** |

Nota: las horas de QA (#100, #101) se ejecutan progresivamente desde F2, con la fase de regresión y validación final concentrada en F6.

### 9.5 Diagrama de Gantt simplificado

```
          FASE PREVIA                 DESARROLLO
          S-6--------S-1   S1--S3  S4--S6  S7------S10  S11-S12  S13----S15  S16---S18  S19--S21
          FP                F0      F1        F2          F3        F4          F5         F6

JP        [██████████████] [████] [████] [████████] [████] [██████] [█████] [████]
BA        [██████████████] [--50%------------------------------------------50%----------]
UX        [██████████████] [25%] [25%] [25%]
Tech Lead                  [████] [████] [████████] [████] [██████] [█████] [████]
Back 1                     [████] [████] [████████] [████] [██████] [█████] [████]
Back 2                            [████] [████████] [████] [██████] [█████]
Front 1                    [████] [████] [████████] [████] [██████] [█████] [████]
Front 2                                  [████████] [████] [██████] [█████]
Integ                      [████] [████] [████████] [████] [██████]
QA                                       [████████] [████] [██████] [█████] [████]
```

### 9.6 Hitos clave

| Hito | Fase | Semana | Entregable |
|---|---|---|---|
| H0 — Diseño UX validado | FP | S-1 | Wireframes finales, prototipos validados, especificación funcional, backlog priorizado |
| H1 — Entorno operativo | F0 | S3 | Arquitectura desplegada, login funcional, BBDD creadas |
| H2 — Catálogo cargado | F1 | S6 | Catálogo importado por ficheros, búsqueda y gestión operativos |
| H3 — Prescripción funcional | F2 | S10 | CRUD completo, máquina de estados, validaciones básicas |
| H4 — Firma y visado | F3 | S12 | Firma digital con Giltza, circuito de visado integrado |
| H5 — Ciclo asistencial cerrado | F4 | S15 | Dispensación integrada, tareas/avisos, ciclo completo |
| H6 — Sistema completo | F5 | S18 | Reglas de indicación, mantenimiento, roles |
| H7 — Release candidate | F6 | S21 | Multi-idioma, SOA, QA final aprobado, listo para UAT |

### 9.7 Riesgos de planificación

| Riesgo | Impacto en calendario | Mitigación |
|---|---|---|
| Retraso en especificación API Giltza (DEP-06) | F3 se retrasa, cascada en F4–F6 | Solicitar documentación en FP; desarrollar con mock hasta disponer de entorno |
| Retraso en formato de fichero nomenclátor (P-09) | F1 se retrasa | Definir formato provisional en FP (CSV genérico) y adaptar al recibir especificación real |
| Preguntas abiertas P-01 (roles) sin resolver | F5 se retrasa o se entrega parcial | Resolver en FP; si no se resuelve, asumir gestión de roles propia y ajustar después |
| APIs de visado del Departamento no disponibles | F3 parcialmente bloqueada | Desarrollar con mocks; el servicio receptor ya es nuestro |
| Alcance de reglas de indicación (P-10) sin definir | F5 puede sobrepasar estimación | Taller funcional en FP para cerrar catálogo de tipos de regla |
| Fase previa insuficiente para resolver dependencias | Desarrollo arranca con incertidumbre | JP debe escalar bloqueos en semana S-3 como máximo; no arrancar desarrollo sin H0 cerrado |
| Diseños UX rechazados por usuarios finales | Retrabajo en desarrollo | Validar prototipos con usuarios reales en FP (semana S-2) antes de construir |

### 9.8 Supuestos de la planificación

1. Las horas estimadas son horas de **desarrollo efectivo** (no incluyen reuniones, gestión ni coordinación del JP/BA).
2. La fase previa (FP) produce wireframes validados y especificación funcional completa; el desarrollo NO arranca sin el hito H0.
3. El framework tecnológico se decide en FP. Las estimaciones asumen un stack moderno con soporte básico de i18n.
4. Las tareas de QA (#100, #101) se ejecutan de forma continua desde F2, no solo en F6.
5. La tarea #102 (ETL Reporting) está **eliminada** del alcance y no consume horas.
6. Las tareas #5–#8 (roles y permisos) están **condicionadas** a la resolución de P-01. Si Osabide Global provee suficiente información, estas 120h podrían reducirse o eliminarse.
7. El Especialista en Integración trabaja al 60% de dedicación porque compagina con otros proyectos de EJIE; su carga se concentra en las fases con integraciones externas.
8. Se asume disponibilidad de entornos de integración (Osabide Global dev, Osategi test, Giltza sandbox) a partir de F2.
9. UX participa al 25% durante F0–F2 para dar soporte a los desarrolladores front y resolver dudas de diseño en tiempo real. A partir de F3 está disponible bajo demanda.
10. JP está al 100% durante todo el proyecto. En proyectos de Administración Pública, la gestión, coordinación con cliente y seguimiento formal requieren dedicación completa.
