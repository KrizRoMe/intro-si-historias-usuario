# Repositorio de Historias de Usuario

Plantilla interactiva de GitHub Issue Form para que los estudiantes del curso **Introducción a los Sistemas de Información** registren sus Historias de Usuario (HU).

## ¿Cómo usar la plantilla?

1. Abre la URL directa del formulario:
   ```
   https://github.com/KrizRoMe/intro-si-historias-usuario/issues/new?template=historia_de_usuario.yml
   ```
2. Completa los campos del formulario.
3. Al enviar, se crea una Issue con la etiqueta `user-story` aplicada automáticamente.

## Estructura del formulario

| Campo | Descripción |
|---|---|
| Identificador de la HU | Ej. `HU-01` |
| Título corto | Resumen en una línea |
| Rol | Quién se beneficia (dropdown) |
| Sistema o módulo | Componente del SI donde aplica |
| Quiero | Acción / funcionalidad |
| Para | Beneficio / valor de negocio |
| Criterios de aceptación | Checklist (5 opciones) |
| Prioridad (MoSCoW) | Must / Should / Could / Won't |
| Estimación | Tamaño relativo (S/M/L) |
| Sprint sugerido | Sprint 1 al 4 o Backlog |
| Dependencias | HU(s) relacionadas |
| Prototipo | Imagen del mockup en Excalidraw |
| Captura del contexto | Foto del problema actual |
| Notas adicionales | Supuestos, links, etc. |

## Directrices para una buena HU

- **Como** un [rol específico],
- **Quiero** [acción / funcionalidad concreta],
- **Para** [beneficio medible para el usuario o la organización].

### Criterios INVEST

- **I**ndependiente: la HU puede desarrollarse sola.
- **N**egociable: el alcance se puede discutir.
- **V**aliosa: aporta valor al usuario o al negocio.
- **E**stimable: se puede estimar tamaño.
- **S**mall: cabe en un sprint.
- **T**esteable: se puede verificar.

## Reglas del repositorio

- No se permiten issues en blanco (la opción "Open a blank issue" está deshabilitada vía `.github/ISSUE_TEMPLATE/config.yml`).
- Cada HU debe ser trazable a un requerimiento del proyecto integrador del curso.
- Las HU aceptadas se mueven a la columna "In Progress" del Project board del equipo.
