# Borrador — página `trayectoria.html` (solo Markdown propuesta editorial)

Este archivo anticipa contenido reproducible después Ronda 3B. **Sin HTML todavía.**

---

## Metadatos propuesta `<head>`

**title**

`Trayectoria profesional — Miguel Marengo Canales`

**meta name="description"** (neutral técnico, ~157 caracteres)

`Matemáticas aplicadas y optimización logística: OR‑Tools, rutas TMS, desarrollo reproducible y gobierno de datos públicos miguelmarengocanales.com.` *(147 caracteres.)*

*(Versión anterior excedía límite rango deseado; recortada sin perder tecnologías visibles texto index y artículos.)*

**Schema.org extendido tipo `Person` (solo propuesta)**

`knowAbout` debe limitarse tecnologías y conceptos efectivamente aparecidos en artículos o `index`:

`"[\"OR-Tools\", \"heuristic routing\", \"TMS/WMS CRM integration\", \"Cursor IDE\", \"Zed IDE\", \"Google Antigravity\", \"Python\", \"SQL\", \"Docker Compose\", \"FastAPI\", \"Firebase\", \"Firestore\", \"supply chain KPI\", \"data governance\", \"data lineage\"]"`
*(La lista debe filtrarse o acortarse en 3B según política JSON‑LD de duplicidad con página person actual.)*

---

## Cuerpo propuesto página

### H1 Trayectoria profesional

*(Se usará mismo `h1` visible arriba; meta title ya suficientemente paralelo tono institucional sitio persona.)*

### Sección 1 — Síntesis profesional (~90 palabras)

El material público disponible muestra trayectoria en **investigación de operaciones aplicada**, **ingeniería de software** con foco reproducibilidad ante decisiones tácticas (rutas, inventario, KPI) y prácticas prácticamente alineadas a **OR‑Tools** según aparece texto portada mayo 2026. El mismo sitio aloja texto propio técnico (rutas, IDEs aplicados datos operativos, gobierno datos cadena suministro) junto colección institucional **Silodisa**‑origen (**Wix** migrado carpeta **`/publicaciones/wix/`**) que ilustra operaciones día a día empresa logística México sin que este borrador adjudique proyecto personal que no aparece documentado archivo propio Miguel.

### Sección 2 — Áreas de competencia (alineadas a los «cuatro ejes» `index`)

#### H2 Modelado matemático y optimización («Modelado y restricciones», portada index)

Aquí converge lo expuesto públicamente sobre formulaciones con función objetivo, restricciones y sensibilidades negocio‑ingeniería. El texto propio *[uRoutes: rutas excelentes sin pelear con el mapa…]* describe TMS con motor OR‑Tools en mensaje público de Silodisa; *[El algoritmo de la verdad…]* liga definiciones gobernadas con solidez antes de optimizar porque definiciones laxas erosionan el modelo incluso cuando el solver es potente. Enlaces canónicos a esas páginas se insertarán en la plantilla HTML en 3B.

#### H2 Ingeniería de software reproducible («Software reproducible»)

Construcción de código donde entradas, revisiones de código y salidas pueden reconstruirse ante revisión ingeniería. El artículo *[Cursor, Zed y Antigravity]* contrasta tres entornos con ejemplos ERP/WMS, SQL y Docker Compose, y menciona agentes Gemini en el contexto de Antigravity. La biblioteca de vídeo sobre uRoutes cita FastAPI/Firestore en los resúmenes de algunos clips: sirve como ilustración de software operativo de marca sin atribución de autoría de piezas de código individuales a personas concretas en este borrador.

#### H2 Inventarios, rutas y red logística (tercer eje «Inventarios, rutas y red logística», portada index)

Fuera del artículo uRoutes existe el hub visual *[Biblioteca de video uRoutes (Silodisa)]* con módulos WMS, TMS y última milla, y abundan piezas de marca sobre inventario y KPIs (serie *Más allá …* ). [PENDIENTE: el propietario indica nivel de detalle público sobre su papel frente al equipo donde el repositorio no lo diga textualmente en HTML propios.]

#### H2 Datos útiles ante mesa directiva (`Datos útiles ante mesa directiva`, cuarto eje portada index)

Aquí están articulados linaje KPI/OTIF en *[El algoritmo de la verdad…]* y la guía *[Trazabilidad de datos…]*. El texto argumenta cómo ERP/WMS/TMS fragmentados producen «verdades» paralelas ante tableros. [PENDIENTE: añadir ejemplo interno sólo si se publica o autoriza después.]

*(Si tras revisión un eje queda sólo sostenido por blog marca y el titular quiere tono sólo autobiográfico, marcar ese eje como a reforzar con pieza nueva propia antes de publicar `trayectoria.html`.)*

[PENDIENTE genérico: reforzar un eje concreto si en 3B se publican artículos firmados nuevos enlazables.]

---

### Sección 3 — Tecnologías y prácticas (extracto sólo desde artículos o portada revisada)

- Aprendizaje automático mencionado a nivel conceptual de gobernabilidad (sin modelo productivo especificado).
- Cursor, Google Antigravity y Zed (IDE/agentes aplicados según texto dedicado).
- Docker Compose como ejemplo de reproducibilidad en integraciones locales.
- FastAPI · Firebase/Firestore (citados leads biblioteca vídeo uRoutes).
- Gemini (contextual a Antigravity en el mismo artículo).
- KPIs · OTIF · POF como indicadores recorrentes marca y artículos de datos.
- OR‑Tools.
- Python y SQL ejemplificados desarrollo backends logística.
- Synthesia (embeds vídeo marca).
- Heurísticas de rutas · ventanas de tiempo · integración TMS–WMS–CRM descrita públicamente «one map» uRoutes texto propio JSON meta OR‑tools.

No insertar tecnologías (p.ej. GraphQL, ORCID formal, MIP) hasta que una pieza futura HTML las nombre explícitamente si desea párrafo homogéneo con principio información verificada.

---

### Sección 4 — Formación académica

[PENDIENTE: el propietario debe proveer instituciones, grados años o negación exponer públicamente esa sección.]  
*(No aparece párrafo explícito de universidad dentro HTML inventariado.)*

---

### Sección 5 — Experiencia profesional principal

Declaración verificada por schema `Person` página inicio mayo 2026:

```json excerpt concept / not paste entire
"worksFor": { "@id": "...#org-silodisa", "name": "Silodisa" }
```
Texto público página declara ocupación etiqueta profesional («Especialista en sistemas …» contenido campo `jobTitle`). **Sin fechas función, sin cargo formal exacto texto visible index además ese schema — [PENDIENTE: persona confirme título público oficial y periodos.**

Antecedentes empleadores anteriores: **[PENDIENTE: sólo después documentado aquí mismo o consentimiento explícito]**.

---

### Sección 6 — Publicaciones

Enlace navegacional:

[Catálogo completo artículos técnicos publicados](/publicaciones.html)

---

## Pendientes antes convertir Markdown a página final

| Pendiente editorial | Motivo |
|---------------------|--------|
| Formación académica | No aparece en HTML público actual del sitio. |
| Cargo, periodos u otros empleadores | Solo consta organización Silodisa en Schema `worksFor` y texto genérico de `jobTitle` en JSON‑LD sin fechas ni historial más allá del repositorio. |
| Foto cabecera u otro recurso multimedia | Fuera texto existente revisado. |

*(Correcciones reputacionales puntuales siguen canal dedicado `/precisiones-prensa.html`.)*
