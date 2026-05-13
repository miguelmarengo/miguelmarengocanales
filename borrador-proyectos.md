# Borrador — página `proyectos.html` (solo Markdown)

Este archivo anticipa contenido reproducible después de la Ronda 3B. **Sin HTML todavía.**

---

## Metadatos propuestos para `<head>`

**title**

`Proyectos y áreas de trabajo — Miguel Marengo Canales`

**meta name="description"** (~151 caracteres)

`Áreas técnicas de trabajo: optimización con OR‑Tools, ingeniería de software para logística y gobernanza de datos para decisiones operativas.`

**Schema.org (propuesta 3B)**

`CollectionPage` con `about` apuntando a las tres áreas técnicas; `author` o `creator` vinculado al `@id` `Person` ya declarado en `index.html`.

---

## Cuerpo de la página

**H1 en HTML:** Proyectos y áreas de trabajo

Esta página agrupa por área temática el trabajo técnico publicado en este sitio. Cada bloque enlaza a documentación detallada en la sección de publicaciones. No es un listado de proyectos cerrados ni un portafolio comercial: es un mapa conceptual sobre material técnico verificable. Para el catálogo completo de artículos ordenado por fecha, consulta la sección [Publicaciones](/publicaciones.html).

---

### Área 1 — Optimización matemática y ruteo

Aplicación de investigación de operaciones a problemas reales de red logística: ventanas horarias, capacidad vehicular, costos operativos y restricciones de servicio. Trabajo cotidiano con OR‑Tools, heurísticas de ruteo y modelos de programación matemática sobre datos operativos reales de distribución farmacéutica con cadena de frío.

#### Material técnico publicado

**[uRoutes: rutas excelentes sin pelear con el mapa](/publicaciones/uroutes-heuristica-mejores-rutas.html)**  
Heurísticas de ruteo y motor OR‑Tools aplicado a operación de TMS. Mayo 2026.

**[Más allá del hype: inteligencia artificial e investigación de operaciones en logística](/publicaciones/wix/mas-alla-del-hype-como-la-inteligencia-artificial-y-la-investigacion-de-operaciones-estan-optimizan.html)**  
Distinción entre soluciones de aprendizaje automático y problemas genuinamente combinatorios donde IO sigue siendo el instrumento correcto. Noviembre 2025.

**[Biblioteca de video — uRoutes](/publicaciones/biblioteca-videos-uroutes-silodisa.html)**  
Recursos visuales sobre el ecosistema operativo: módulos de WMS, TMS, ruteo y aplicación de chofer.

---

### Área 2 — Ingeniería de software para logística

Diseño y construcción de sistemas reproducibles con trazabilidad de datos, control de versiones y pruebas. Integración entre ERP, WMS, TMS y CRM con APIs auditables. Stack habitual: Python, SQL, Google Cloud, FastAPI, Docker, entornos de desarrollo asistidos por agentes (Cursor, Zed, Google Antigravity).

#### Material técnico publicado

**[Cursor, Zed y Antigravity: IDEs para software de logística](/publicaciones/cursor-zed-antigravity-ides-logistica.html)**  
Análisis comparativo de tres entornos de desarrollo asistido por IA aplicados a problemas reales de software para cadena de suministro. Mayo 2026.

---

### Área 3 — Gobernanza y trazabilidad de datos

Diseño de prácticas de linaje, validación y reconciliación entre sistemas para que los tableros directivos respondan a una sola fuente de verdad. Documentación de supuestos, criterios de aceptación y reconstrucción de cadenas de decisión hasta el dato original.

#### Material técnico publicado

**[El algoritmo de la verdad: gobernanza de datos en logística](/publicaciones/algoritmo-verdad-gobernanza-datos-logistica.html)**  
Cuando las definiciones operativas están fragmentadas entre sistemas, los modelos más sofisticados producen verdades paralelas. Mayo 2026.

**[Trazabilidad de datos en cadena de suministro](/publicaciones/trazabilidad-datos-decisiones-logistica.html)**  
Snapshots mínimos y reconstrucción de la cadena de un dato hasta la decisión que lo originó. Mayo 2026.

#### Aplicación operativa documentada

**[Logística en tiempo real frente a promedios de 30 días](/publicaciones/wix/logistica-en-tiempo-real-por-que-los-promedios-de-30-dias-estan-matando-tu-cadena-de-suministro.html)**  
KPIs operativos contra mediciones rezagadas en distribución farmacéutica. Noviembre 2025.

**[De la medición a la mejora continua: KPIs operativos](/publicaciones/wix/de-la-medicion-a-la-accion-como-los-kpis-y-la-mejora-continua-definen-nuestra-excelencia-logistica.html)**  
Octubre 2025.

**[Importancia de las evidencias en la logística: garantizando una entrega perfecta](/publicaciones/wix/la-importancia-de-las-evidencias-en-la-logistica-garantizando-una-entrega-perfecta.html)**  
Soporte documental sobre la métrica POF (Perfect Order Fulfillment) en operación real.

---

### Catálogo completo

Para acceder al inventario completo de publicaciones, ordenado por fecha, usa [Publicaciones](/publicaciones.html).

---

## Pendientes antes convertir Markdown a página final

| Pendiente editorial | Motivo |
|---------------------|--------|
| JSON‑LD `CollectionPage` (`about`/tres ejes temáticos, `creator`/`author` ligado `#person`). | Pendiente markup en HTML 3B. |
| Orden dentro de cada bloque ¿cronología inversa? ¿`<details>` en sublistas largas futuras? | Decisión UX y accesibilidad al maquetar. |

*(Enlaces internos siguen rutas relativas desde raíz; absolutas sólo donde defina política canonical/OG/schema.)*
