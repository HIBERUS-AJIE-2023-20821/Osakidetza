# Comentarios del cliente — 11/03/2026

## Origen

Comunicación escrita del cliente (Osakidetza) recibida el 11 de marzo de 2026.

## Contenido literal

> Tenía pendiente informaros del enfoque con el catálogo de Productos Ortoprotésicos.
>
> La integración se plantea a través de ficheros o alguna otra solución. NO se propone usar herramientas de replicación tipo Oracle Golden Gate, por los costes que implica para algo manejable con otras soluciones.
>
> Por otro lado, consideramos que es preferible incorporar un módulo de mantenimiento de Productos Ortoprotésicos en Osakidetza que permita caracterizar los productos y reglas que se necesiten para la indicación, por lo que en la estimación, considerad esta necesidad.

## Interpretación y decisiones derivadas

### Decisión 1 — Mecanismo de integración del catálogo: ficheros

- La sincronización del nomenclátor del Departamento con la BBDD propia de Osakidetza se realizará **mediante ficheros** (CSV, XML u otro formato plano acordado).
- Se descarta expresamente el uso de herramientas de replicación de base de datos (Oracle Golden Gate o similares) por motivos de coste.
- Esto afecta a las tareas de **carga masiva (batch)** y **carga bajo demanda**: ambas pasan de ser un proceso genérico de "sincronización" a un proceso concreto de **importación/parseo de ficheros**.
- Implica desarrollo de:
  - Proceso de lectura, parseo y validación de ficheros recibidos del Departamento.
  - Gestión de errores de importación (registros duplicados, formatos incorrectos, campos faltantes).
  - Mecanismo de recepción de ficheros (ubicación, protocolo y periodicidad por definir).
  - Log/auditoría de cargas realizadas.

### Decisión 2 — Módulo de mantenimiento de productos ampliado (caracterización y reglas de indicación)

- El cliente solicita un **módulo de mantenimiento de productos ortoprotésicos propio de Osakidetza** que vaya más allá de la simple activación/desactivación de productos.
- Este módulo debe permitir:
  - **Caracterizar productos**: añadir atributos propios de Osakidetza que complementen los datos del Departamento (más allá de activo/inactivo y favoritos).
  - **Definir reglas de indicación**: configurar qué condiciones, restricciones o requisitos aplican a cada producto para su prescripción (por ejemplo: qué especialidad puede prescribirlo, si requiere justificación adicional, si tiene restricciones de edad/sexo, límites de renovación, etc.).
- Esto amplía significativamente el alcance del Módulo 5 (Mantenimiento) y del Módulo 2 (Catálogo), y tiene impacto directo en el Módulo 3 (Prescripción), que debe consumir estas reglas para validar la prescripción.
- Implica desarrollo de:
  - Modelo de datos para reglas de indicación por producto.
  - Pantalla de administración para definir/editar reglas de indicación.
  - Motor de validación que aplique las reglas al prescribir.
  - APIs back para CRUD de reglas y consulta de reglas aplicables.

## Impacto en documentación

- **Enfoque PM/BA V5**: Actualizar Módulo 2 (mecanismo de sincronización) y Módulo 5 (ampliar mantenimiento con caracterización y reglas). Actualizar DEP-05 y reglas de negocio.
- **Tabla de Tareas V5**: Actualizar tareas #14, #15, #16 (carga), #13 (gobierno de edición), #17/#18 (gestión catálogo). Añadir tareas nuevas para reglas de indicación y procesamiento de ficheros.
