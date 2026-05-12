# Reporte 3A — Inventario temático del contenido existente

Alcance: artículos y piezas HTML de contenido sustantivo bajo `/publicaciones/` y `/publicaciones/wix/`; más la página de inicio tratada como **recurso de perfil**, no como artículo. Se excluyen por diseño backups, dumps Wix brutos en raíz (`.wix-blog-p*.html`), verificación de dominio Google y páginas de precisiones/transparencia (no son «material técnico» para este hub).

**Nota canonía:** donde `<title>` y `<h1>` difieren levemente, se prioriza **`<h1>`** como título canónico del contenido visible.

---

## Tabla inventario por artículo

| Archivo | Título canónico (H1) | Fecha (meta / visible) | Tema principal (frase corta) | Tecnologías, frameworks y metodologías mencionadas (en cuerpo o metadatos) | Cliente / proyecto nombrado (con contexto de autoría) | Resumen ejecutivo (1–2 frases) | Área principal | Área secundaria |
|--------|----------------------|-------------------------|------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------|----------------------------------|----------------|------------------|
| `publicaciones/uroutes-heuristica-mejores-rutas.html` | uRoutes: rutas excelentes sin pelear con el mapa (sí, con heurística) | 2026-05-12 | TMS, heurísticas y rutas con restricciones operativas. | OR‑Tools, heurística, ventanas de tiempo, TMS; integración conceptual WMS+TMS+CRM; mención builds (`uRoutes v0.3.15`). | Silodisa como contexto público descrito (divulgación basada en el sitio de Silodisa; nota aclaratoria en el texto). | Explica por qué un motor de rutas combina restricciones reales (tiempo, costo, servicio) y un hilo único de datos frente al plan manual. Enlaza filosofía «one map, full chain» con optimización práctica. | A | D |
| `publicaciones/biblioteca-videos-uroutes-silodisa.html` | Biblioteca de video uRoutes (Silodisa) | Modificación página 2026-05‑12; clips sin fecha por pieza (declarado en meta) | Video‑tutoriales del ecosistema uRoutes (WMS, TMS, rutas, portales). | Textos/leads mencionan Firebase / Firestore, FastAPI, Synthesia (embeds), módulos WMS/TMS/CRM conceptualmente. | Silodisa como origen canónico de la biblioteca (`silodisa.com/es/videos`). | Reproduce 17 clips con iframe y enlaces ancla al sitio de Silodisa; sirve como documentación visual del producto público uRoutes. | A | D |
| `publicaciones/cursor-zed-antigravity-ides-logistica.html` | Cursor, Zed y Antigravity: IDEs para software de logística | 2026-05-12 | Comparativa de IDEs/agentes aplicada a backends logísticos. | Cursor, Zed, Google Antigravity; Python, SQL, Docker Compose, JSON, VS Code‑like; ERP/WMS, webhooks, Gemini (contextual a Antigravity). | Sin cliente comercial nominado como caso; ejemplo genéricos de equipo de desarrollo logístico. | Contrasta tres entornos bajo escenarios típicos (rutas, inventario por ubicación, integraciones) y propone criterios empíricos de elección sin dogmatismo. | B | A |
| `publicaciones/algoritmo-verdad-gobernanza-datos-logistica.html` | El algoritmo de la verdad: por qué la gobernanza de datos es la única salvación en la logística | 2026-05-12 | Gobernanza y consistencia semántica antes de optimizar. | Gobernanza de datos, linaje (data owner), políticas explícitas, silos entre ERP/WMS/TMS, KPI/OTIF, aprendizaje automático en marco conceptual (no código). | Referencia enlazada a otro propio `trazabilidad-datos-decisiones-logistica.html`. | Sostiene que modelos fragilan si las definiciones de «demanda», «servicio», etc., no están gobernadas; propone pasos mínimos (catálogo de definiciones, linaje viable, reglas de calidad versionadas). | C | D |
| `publicaciones/trazabilidad-datos-decisiones-logistica.html` | Trazabilidad de datos en decisiones de cadena de suministro | 2026-05-11 | Trazabilidad del dato hasta la decisión operativa. | Snapshots auditables; cadena fuente→transformaciones→acción sin stack de vendor nombrado. | Sin proyecto externo nominado; marco aplicable genéricamente. | Defiende prácticas de trazabilidad mínimas (fecha, responsable, supuesto, identificador de snapshot) ante decisiones sobre proveedor, lote o ruta. | C | D |
| `publicaciones/wix/optimizando-la-planificacion-de-rutas-con-algoritmos-avanzados.html` | Optimizando la planificación de rutas con algoritmos avanzados | 2023-07-20 | Ruteo con restricciones y datos en tiempo real. | OR‑Tools mencionado explícitamente; restricciones de capacidad y horarios. | Narrativa institucional de Silodisa (pieza corporativa migrada desde Wix). | Describe optimización avanzada de rutas bajo restricciones comerciales y transporte usando datos en tiempo real. | A | — |
| `publicaciones/wix/mas-alla-del-hype-como-la-inteligencia-artificial-y-la-investigacion-de-operaciones-estan-optimizan.html` | Más Allá del Hype: Cómo la Inteligencia Artificial y la Investigación de Operaciones Están Optimizando el Flujo Logístico Hoy | 2025-11-29 | IA aplicada junto con IO al flujo logístico contemporáneo. | Investigación de operaciones e IA mencionadas a alto nivel (sin stack técnico detallado en el archivo). | Posicionamiento de Silodisa en tecnología. | Ensayo de coyuntura sobre papel de IA+IO más allá del marketing; contenido institucional. | A | C |
| `publicaciones/wix/la-revolucion-silenciosa-en-tu-almacen-como-la-ia-y-la-tecnologia-estan-redefiniendo-la-logistica.html` | La Revolución Silenciosa en tu Almacén: … Silodisa es tu Aliado Clave en México | 2025-07-02 | IA/tecnología de almacén y logística México. | Menciona OR‑Tools de Google y «algoritmos propios» en narrativa corporativa. | Silodisa ante prospectos en México. | Artículo de captación tecnológico; incluye referencia OR‑Tools. | D | A |
| `publicaciones/wix/el-papel-de-la-inteligencia-artificial-en-la-optimizacion-de-la-logistica.html` | El papel de la Inteligencia Artificial en la optimización de la logística | 2023-07-20 | IA aplicada conceptualmente en optimización logística. | IA descrita sin stack detallado. | Narrativa institucional. | Panorama de alto nivel de IA en operaciones. | D | — |
| `publicaciones/wix/logistica-en-tiempo-real-por-que-los-promedios-de-30-dias-estan-matando-tu-cadena-de-suministro.html` | Logística en Tiempo Real: Por Qué los Promedios de 30 Días Están Matando tu Cadena de Suministro | 2025-11-22 | Crítica a métricas agregadas en cadena de suministro. | KPI/medición tiempo real, cultura datos en planta. | Narrativa institucional | Argumento operativo‑analítico a favor del dato fresco vs. medias mensuales opacas. | C | D |
| `publicaciones/wix/de-la-medicion-a-la-accion-como-los-kpis-y-la-mejora-continua-definen-nuestra-excelencia-logistica.html` | De la Medición a la Acción: Cómo los KPIs y la Mejora Continua Definen Nuestra Excelencia Logística | 2025-10-25 | KPIs visibles por turnos y mejor continua institucional. | KPI, medición tiempo real, mejora continua. | Narrativa institucional | Ejemplifica cultura de tableros y acción rápida en operaciones. | C | D |
| `publicaciones/wix/mas-alla-del-dato-por-que-la-logistica-de-clase-mundial-exige-medir-la-realidad-en-tiempo-real.html` | Más Allá del Dato: Por Qué la Logística de Clase Mundial Exige Medir la Realidad en Tiempo Real | 2025-11-15 | Medición tiempo real clase mundial. | KPIs visibles equipo operativo, referencia MIT cualitativa en estilo texto original. | Narrativa institucional | Vincula transparencia de métricas con cultura competitiva. | C | D |
| `publicaciones/wix/mas-alla-del-esfuerzo-la-ciencia-de-la-medicion-logistica-en-tiempo-real.html` | Más Allá del Esfuerzo: La Ciencia de la Medición Logística en Tiempo Real | 2025-11-08 | Narrativa institucional de medición tiempo real. | KPIs tiempo real. | Narrativa institucional | Refuerzo del mensaje anterior en serie contenido institucional. | C | D |
| `publicaciones/wix/mas-alla-del-echale-ganas-por-que-la-cultura-de-datos.html` | Más Allá del "Echale Ganas": Por Qué la Cultura de Datos | 2025-11-01 | Cultura de datos vs sólo voluntad institucional. | Cultura de datos, KPIs mencionados concretamente en la línea típica de serie blog. | Narrativa institucional | Conecta entusiasmo con disciplina métrica. | C | E |
| `publicaciones/wix/datos-lo-que-diferencia-a-silodisa.html` | DATOS, LO QUE DIFERENCIA A SILODISA | 2025-07-07 | Valor institucional de datos operativos. | Datos, precisión métricas en estilo institucional. | Silodisa | Posicionamiento de datos como diferenciador. | C | D |
| `publicaciones/wix/en-silodisa-cada-dato-cuenta-la-clave-de-nuestra-excelencia-operativa.html` | El Superpoder de Silodisa: Datos, Precisión y la Entrega Perfecta (POF) | 2025-08-09 | Métricas POF/excelencia. | POF (Perfect Order Fulfillment mencionado en título y cuerpo). | Silodisa | Une datos y cumplimiento de pedido institucional. | D | C |
| `publicaciones/wix/importancia-del-cumplimiento-perfecto-del-pedido-pof.html` | Importancia del Cumplimiento Perfecto del Pedido (POF). | 2023-07-20 | Indicadores de cumplimiento de pedidos. | POF/service logístico institucional. | Institucional | Educativo operativo‑comercial típico de blog marca. | D | C |
| `publicaciones/wix/la-importancia-de-las-evidencias-en-la-logistica-garantizando-una-entrega-perfecta.html` | La importancia de las evidencias en la logística… | 2023-07-20 | Evidencias y entrega institucional | Evidencias de entrega institucional | Institucional | Educativo en control de última milla institucional | D | C |
| `publicaciones/wix/optimizando-el-diseno-del-almacen-para-mejorar-la-eficiencia.html` | Optimizando el diseño del almacén para mejorar la eficiencia | 2023-07-20 | Diseño almacén/eficiencia | Diseño físico proceso almacén (alto nivel) | Institucional | Contenido de diseño‑operativo almacenes | D | — |
| `publicaciones/wix/la-importancia-de-un-almacen-caotico-y-sus-beneficios.html` | La importancia de un almacén caótico y sus beneficios | 2023-07-20 | Modelo conceptual almacén "caótico" | Métodos almacenes comerciales (alto nivel) | Institucional | Divulgación de conceptos de diseño. | D | — |
| `publicaciones/wix/el-doble-motor-de-nuestro-exito-precision-en-el-inventario-y-pasion-en-nuestra-gente.html` | El Doble Motor de Nuestro Éxito: Precisión en el Inventario y Pasión… | 2025-09-27 | Cultura equipo + inventario preciso | KPI/medición tiempo real institucional (texto menciona tableros en tono empresa). | Narrativa marca | Arte cultura empresa + KPI inventario. | D | E |
| `publicaciones/wix/la-filosofia-del-cero-error-por-que-en-silodisa-la-precision-del-inventario-es-una-obsesion.html` | La Filosofía del "Cero Error": … inventario … | 2025-10-18 | Precisión inventario institucional | Control inventario institucional | Silodisa | Narrativa institucional de excelencia en inventario. | D | C |
| `publicaciones/wix/el-nearshoring-esta-aqui-tu-socio-logistico-esta-realmente-preparado.html` | El Nearshoring está Aquí: ¿Tu Socio Logístico…? | 2025-09-13 | Nearshoring y preparación socio logístico | Tendencias cadena México (alto nivel) | Prospectos + Silodisa institucional | Artículo tendencia macro + servicio socio. | D | E |
| `publicaciones/wix/detras-de-cada-botella-de-electrolit-la-mision-esencial-de-silodisa.html` | Detrás de Cada Botella de Electrolit: … SILODISA | 2025-08-16 | Caso institucional Electrolit | Distribución / misión marca mencionadas en estilo institucional | Electrolit como caso narrado en pieza marca | Ejemplo público marca consumo pharma/logística México. | D | — |
| `publicaciones/wix/de-tlaloc-a-la-nube-como-la-sabiduria-ancestral-inspira-la-logistica-sostenible-de-silodisa-mx.html` | De Tláloc a la Nube: … Silodisa.mx | 2025-08-23 | Sostenibilidad narrativa marca | Sostenibilidad cultura marca (alto nivel) | Silodisa.mx institucional | Relato cultural + posicionamiento sostenibilidad marca. | E | D |
| `publicaciones/wix/logistica-innovadora.html` | Logística Innovadora | 2023-07-20 | Panorama institucional innovación. | Conceptos tecnológicos alto nivel marca | Institucional | Genéricos innovación marca. | D | E |
| `publicaciones/wix/las-tendencias-mas-innovadoras-en-la-logistica-actual-2023.html` | Las tendencias más innovadoras en la logística actual 2023 | 2023-07-20 | Tendencias 2023 alto nivel. | Trends industria texto genéricos | Institucional | Lista tendencias coyuntura 2023. | D | E |
| `publicaciones/wix/el-futuro-de-la-logistica-tendencias-e-innovaciones.html` | El futuro de la logística: Tendencias e innovaciones | 2023-07-20 | Futuro tecnológico alto nivel institucional | IA / trends genéricos | Institucional | Outlook futuro marca. | D | E |
| `publicaciones/wix/innovacion-cumplimiento-y-bienestar-asi-construimos-juntos-el-futuro-en-silodisa.html` | Innovación, Cumplimiento y Bienestar: … Silodisa | 2025-08-02 | RH / cultura + innovación marca | Bienestar empleados mencionados estilo empresa | Silodisa | Artículo cultura organizacional. | E | D |
| `publicaciones/wix/el-poder-del-asombro-impulsando-la-motivacion-en-silodisa-para-2025.html` | El Poder del Asombro: … Silodisa … 2025 | 2025-09-20 | Motivación / cultura 2025 | Sin stack técnico enfoque personas | Silodisa | Artículo cultura motivacional. | E | — |
| `publicaciones/wix/mas-que-una-empresa-una-comunidad-el-ingrediente-secreto-de-silodisa.html` | Más que una Empresa, una Comunidad: … Silodisa | 2025-09-06 | Cultura empresa‑comunidad | Sin tecnología código | Silodisa | Relato marca comunidad. | E | — |
| `publicaciones/wix/blog-silodisa-la-alineacion-nuestro-motor-para-resultados-extraordinarios.html` | Blog Silodisa: La Alineación, Nuestro Motor … | 2025-10-13 | Cultura misión empresa | Alineación cultura equipo texto genéricos | Silodisa | Discurso alineación resultados empresa. | E | D |
| `publicaciones/wix/en-silodisa-la-tecnologia-tiene-un-proposito-tu-familia.html` | En Silodisa, la Tecnología Tiene un Propósito: Tu Familia | 2025-07-19 | Propósito marca / familia empleados | Sin tecnología profunda código | Silodisa | Relato marca‑personas institucional. | E | — |
| `publicaciones/wix/mas-que-agua-el-gesto-que-muestra-el-corazon-de-silodisa.html` | Más que Agua, el Gesto que Muestra el Corazón de Silodisa | 2025-07-26 | Gesto social empresa | — | Silodisa, donación agua (texto original) | RSE / cultura. | E | — |
| `publicaciones/wix/cansado-del-caos-usa-los-secretos-de-la-logistica-para-organizar-tu-vida-y-alcanzar-tus-metas.html` | ¿Cansado del caos? Usa los secretos de la logística… vida personal | 2025-07-12 | Analogía vida personal‑logística | Metáforas productividad personales. | Narrativa marca + lector persona popular. | Ensayo vida personal inspirado disciplina logística. | E | — |
| `publicaciones/wix/hackea-tu-felicidad-y-productividad-el-plan-definitivo-de-las-mejores-universidades-del-mundo-para.html` | ¡Hackea tu Felicidad y Productividad! … | 2025-07-05 | Felicidad y productividad personales alto nivel. | Conceptos desarrollo persona / universidades (texto institucional pop.) | — | Inspiracional generalista. | E | — |

\*Textos migrados desde Wix: la **autoría voz marca** aparece institucional; no se puede inferir contribución persona sin fuente fuera del archivo.

---

## Recurso de perfil sin fila tabla

| Archivo | Función para hub |
|---------|-------------------|
| `index.html` | Portada profesional: investigación de operaciones y OR‑Tools en hero; cuatro ejes (modelado, software reproducible, inventarios‑rutas‑red logística, datos ante mesa directiva). Organization **Silodisa** aparece sólo como `worksFor` en Schema.org en el HTML actual (`#org-silodisa`). |

---

## Clasificación resumida por área (conteos según área *principal*, 36 piezas inventariadas)

| Código área | Nombre corto | Nº principal |
|:------------:|---------------|:------------:|
| A | Rutas, motores y hub uRoutes (incluye biblioteca de vídeo como pieza única agregadora) | 4 |
| B | Herramientas de desarrollo (IDEs/agentes aplicados a logística) | 1 |
| C | Datos, gobernanza, KPI y medición en tiempo real | 8 |
| D | Inventario, última milla, tendencias cadena suministro, piezas marca operativas | 14 |
| E | Cultura empresa, marca, contenido institucional o divulgación no técnica | 9 |

*Comprobación: 4 + 1 + 8 + 14 + 9 = 36.*

---

## Ajuste a la taxonomía A–E

Las cinco categorías funcionan porque la mayoría del volumen público viene de contenido marca **Silodisa** (**D**/ **E**) y convive con piezas de firma (**A–C**) en la carpeta `publicaciones/` propia del titular personal.

Opción editorial plausible en Ronda 3B:

- Agrupar en `proyectos.html` las piezas **`mas-alla-*`** y **KPI** en una sublista tipo «Serie KPI y lectura tiempo real», para no cansar repetición de títulos.

---

¿Contenido sensible dentro de `/publicaciones/` según política precisiones‑prensa? **No aparecieron strings reputacionales** listados por el propietario en `index`, `publicaciones`, `publicaciones/wix`; siguen contenidos sólo donde corresponde (precisiones‑prensa, transparencia legado).
