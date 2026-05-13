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

`"[\"OR-Tools\", \"heuristic routing\", \"TMS/WMS CRM integration\", \"Cursor IDE\", \"Zed IDE\", \"Google Antigravity\", \"Python\", \"SQL\", \"Google Cloud\", \"Docker Compose\", \"FastAPI\", \"Firebase\", \"Firestore\", \"supply chain KPI\", \"data governance\", \"data lineage\"]"`
*(Filtrar o acortar en 3B según política JSON‑LD; el cuerpo actual nombra además inglés/avanzado y alemán — idiomas típicamente fuera `knowAbout`.)*

---

## Cuerpo propuesto página

**H1 en HTML:** Trayectoria profesional  
*(Debajo cada `###` será **h2** en la plantilla salvo donde se indiquen niveles más profundos.)*

*(Declaración página inicio mayo 2026: schema `Person` con `worksFor` Silodisa y `jobTitle` genérico. En **3B** conviene alinear visibles/metadata JSON‑LD con cargos, periodos Areté/Silodisa y ocupación textual del cuerpo.)*

### Síntesis profesional

Mi trabajo se concentra en la intersección de matemáticas aplicadas, ingeniería de software y operaciones logísticas. Desde 1989 dirijo Areté Software, empresa dedicada al desarrollo de sistemas para logística y cadena de suministro. Desde 2009 opero Silodisa, organización de almacenamiento y distribución con flota refrigerada especializada en medicamentos y electrolitos. Mi formación combina ingeniería técnica, dirección empresarial e innovación organizacional, con énfasis en sistemas auditables, optimización de rutas e inventarios, y gobernanza de datos para decisiones operativas defendibles ante revisión ejecutiva.

### Áreas de competencia técnica

#### Modelado matemático y optimización

Formulación de problemas operativos con función objetivo y restricciones explícitas; aplicación de OR‑Tools y heurísticas de ruteo a problemas reales de cadena de suministro; análisis de sensibilidad y escenarios de estrés. La [página de proyectos](/proyectos.html) enlazará al trabajo publicado sobre uRoutes y motores de ruteo para TMS (disponible en **3B** cuando exista ese HTML).

#### Ingeniería de software sobre datos trazables

Desarrollo de sistemas reproducibles con linaje de datos, control de versiones y pruebas. Trabajo cotidiano con Python, SQL, Google Cloud, FastAPI y entornos de desarrollo asistidos por agentes (Cursor, Zed, Google Antigravity). Énfasis en arquitecturas auditables y trazables ante revisión técnica y de cumplimiento.

#### Optimización de rutas, inventarios y red logística

Aplicación operativa de modelos sobre redes de distribución reales: ventanas de tiempo, integración TMS‑WMS‑CRM, KPIs de servicio (OTIF, POF) e inventarios bajo restricciones de servicio y costo. Contexto operativo: distribución farmacéutica con cadena de frío en Silodisa.

#### Gobernanza y calidad de datos

Diseño de prácticas de linaje, validación y reconciliación entre sistemas (ERP/WMS/TMS) para que los tableros directivos respondan a una sola fuente de verdad. Documentación de supuestos, criterios de aceptación y bitácora de cambios.

### Formación académica

**Ingeniero Mecánico Electricista**, Universidad Nacional Autónoma de México (UNAM). Titulado en 1986, con cédula profesional emitida por la Dirección General de Profesiones de la Secretaría de Educación Pública.

**Estudios completos de Maestría en Administración**, Universidad Veracruzana (1994). Programa concluido con reconocimiento al mejor desempeño académico de la generación; pendiente disertación de grado.

**Programa AD‑2 de Innovación y Continuidad**, IPADE Business School, Universidad Panamericana (2012).

**Stanford Executive Program**, Stanford Graduate School of Business (2013).

### Experiencia profesional

**Fundador y director general — Areté Software** (1989 – presente)  
Empresa dedicada al desarrollo de software para logística y cadena de suministro.

**Fundador y director general — Silodisa** (2009 – presente)  
Operación logística de almacenamiento y distribución con flota refrigerada, especializada en medicamentos y electrolitos.

**Encargado de programación de encuestas de expectativas empresariales — Instituto Nacional de Estadística, Geografía e Informática (INEGI)**  
Diseño y desarrollo de sistemas para el levantamiento y procesamiento de encuestas económicas dirigidas al sector empresarial.

**Director de Cómputo — Cámara de Diputados, H. Congreso de la Unión** (1985 – 1986)  
Responsable de la infraestructura de cómputo y sistemas de información de la Cámara de Diputados.

### Reconocimientos profesionales

**Premio Estatal de la Calidad — Gobierno del Estado de Hidalgo**  
Otorgado a Areté Software por la implementación del Sistema Integral de Licencias de Conducir del Estado de Hidalgo, operando en todo el territorio estatal. Reconocimiento entregado entre finales de los noventa y principios de los dos mil.

**Certificación Great Place to Work — Areté Software**  
Reconocimiento internacional otorgado por Great Place to Work Institute a empresas con culturas organizacionales destacadas. Obtenido entre 2010 y 2015.

### Idiomas

Español (lengua materna) · Inglés (nivel avanzado) · Alemán (intermedio activo, con tres años de residencia en país de habla alemana)

### Publicaciones técnicas

Catálogo completo de artículos técnicos publicados disponible en [Publicaciones](/publicaciones.html).

---

## Pendientes antes convertir Markdown a página final

| Pendiente editorial | Motivo |
|---------------------|--------|
| **Premio Estatal de la Calidad (Hidalgo)** — fechas exactas o documento público cotizable. | Narrativa provisional «finales noventa / principios dos mil» antes publicación oficial. |
| Alinear `index`/JSON‑LD (`jobTitle`, `worksFor`, opcional segunda org Areté) con cuerpo trayectoria. | Portada aún muestra ocupación corta únicamente y `worksFor` Silodisa. |
| Foto cabecera u otro recurso multimedia | Fuera texto existente revisado. |

*(Enlace [/proyectos.html](/proyectos.html) en modelo y optimización: destino válido sólo después **3B** cuando exista el HTML proyectos.)*

*(Correcciones reputacionales puntuales siguen canal dedicado `/precisiones-prensa.html`.)*
