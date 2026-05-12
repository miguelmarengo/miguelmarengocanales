# Reporte — Prioridad 3A (extracción y propuesta sólo Markdown)

Ejecución al **2026‑05‑11** contexto proyecto `miguel-marengo-canales-pagina-web`.

---

## 1. Resumen inventario temático

| Métrica | Valor verificado |
|---------|-------------------|
| Artículos HTML recopilados carpeta persona `publicaciones/*.html` | **5** |
| Piezas migra Wix republicadas carpeta **`publicaciones/wix/*.html`** | **31** |
| Total filas tabla inventario | **36** |
| Inventario archivo | `reporte-3a-inventario.md` |

Distribución áreas ***primarias*** (véase segunda tabla ese archivo también):

| Código área | Conteo principal |
|:-------------:|:----------:|
| A | **4** |
| B | **1** |
| C | **8** |
| D | **14** |
| E | **9** |
| Σ | **36** ✓ |

Nota método: clasificación sólo usando lectura contenido público archivo; etiqueta marca **«Narrativa institucional Silodisa»** en piezas migradas porque voz empresa sin distinción explícita autor humano dentro HTML.

---

## 2. Áreas temáticas finales elegidas motivo corto

A–**E** se mantuvo original briefing después ver volumen porque:

- Serie **Mas allá …** KPI / cultura (**C**) coexisten con piezas marca solo operativo (**D**) y no convenía colapsar sólo tres rubros porque perderían separación práctica proyecto hub página.
- **E** permite aislar contenido marca cultura‑personas sin confundirlos navegaciones técnicos que buscan algoritmos/motores.
- Solo alternativa plausible era fusionar **D+E** institucional; se desaconsejó por mezcla tono ejecutivo KPI vs historia motivacional equipo.

Referencia tabla detalle `reporte-3a-inventario.md § Clasificación resumida`.

---

## 3. Archivos `.md` generados entrega 3A

| Archivo | Propósito |
|---------|-----------|
| `reporte-3a-inventario.md` | Tabla archivo‑a‑archivo clasificación tecnologías fecha resumen cliente |
| `borrador-proyectos.md` | Estructura propuesta página `proyectos.html` hub navegacional |
| `borrador-trayectoria.md` | Narrativa competencias tecnologías knowAbout schema propuesta persona |
| `borrador-contacto.md` | Mínimos canales + precisiones‑prensa cruce |
| `reporte-prioridad-3a.md` *(este archivo)* | Consistencia proceso + validaciones técn |

No se modificó HTML/JSON configuración servidor (cumplimiento prohibición briefing).

---

## 4. Resultados validaciones complementarias breve (**TAREA 6**)

### 6.1 `vercel.json`

Redirects primeras entradas explícitas `source` rutas antes reglas `:path*` wildcard `has`:

```json
{ "source": "/transparencia.html", ... }
{ "source": "/transparencia", ... }
```

Las reglas `has` sólo ejecutan ante host mismatch (subdominio / apex sin www); **desconocido conflicto orden** fuera ese documento porque **primer match gana típico deployments Vercel** y rutas específicas preceden comodín path – evaluación lógica: **aparentemente válido sintactic JSON** mayo 2026.

*[No se alteró archivo – observación sólo lectura.]*

### 6.2 Estado `transparencia.html` legado

Permanece página completa pre‑**precisiones** reputacional con meta keywords/descripciones **ISSSTE / Reforma 250 / Índice Político**. **Beneficio mantener física archivo** hasta que search engines completen procesamiento nuevo redirect 308/301 porque copia HTML auto‑canonical evita inconsistencia crawler si CDN cache transitorio. **Stub mínimo** HTML cliente (**meta refresh**/JS) podría añadirse **redundancia** ante fallas improbables servidor – **opcional recomendado sólo después** verificar política crawler duplica contenidos (*soft duplicate*). Eliminar físico archivo **prematuro** mientras existe documentación paralela nueva `precisiones-prensa.html` y backlinks externos potenciales; redireccionamiento servidor ya suficiente arquitectónico.

### 6.3 Términos sensibles dispersión fuera `precisiones-prensa.html`

Búsqueda acotada `index.html`, `publicaciones/`, Archivo **`publicaciones.html`**: **cero ocurrencias** cadenas: `Índice Político`, `Álvarez Puga`, `Reforma 250`, `ISSSTE`, `Gordillo`, `Yunes`.

Hallazgos adicionales (propietario decidir tratamiento infra vs contenido público navegable):

| Archivo residual | Observación reputacional breve |
|------------------|---------------------------------|
| `precisiones-prensa.html` | Destino reputacional esperado ✅ |
| `transparencia.html` | Legacy duplicidad semántico / SEO – mitigación redirect ✅ |
| `backup-prioridad-* / wix dumps raíz (*.wix-blog...) ` | No están enlazadas navegación sitio público habitual; igual podrían servir texto largo crawler si servidor los expone público – **valorar exclusion `robots.txt` o mover fuera artefactos publicación.** |

*Ningún artículo técnico repositorio mezcla esas etiquetas reputacionales hoy ✅.*

---

## 5. Lista campos marca **[PENDIENTE]** próximos antes Ronda 3B (public HTML)

Combinación deduplicada principal:

| Categoría | Pendiente ejemplo |
|-----------|-------------------|
| Académica | Institución(s), año(s), público/ocultar sección trayectoría |
| Profesión empleadores | Roles fechas empresa distinta Silodisa |
| Corporativa Silodisa | ¿Mostrar mismo email equipo? ¿Cargo formal firma público página persona?|
| Canal contacto extras | Correo público github orcid scholarly |
| Curaduría proyecto hub | Comprimir sublistas marca vs textos Miguel |
| Recursos multimedia | ¿Foto / iconografía extra páginas nuevas|

---

## 6. Decisiones tomadas modelo sin instrucción explícita (revisión humana)

| Decisión | Justificación ejecutada |
|-----------|---------------------------|
| Excluí precisiones‑prensa del inventario “artículo técnico” para hub proyectos porque propósito reputacional‑legal diferente colección rutas/dat |
| Inventariadas **todas** 31 piezas wix porque siguen dentro patrimonio textual servidor aun tonalidad empresa |
| Inventario prioriza **`h1`** título cuando title largo sufijo marca |
| Serie KPI **clasificada Área C principal** incluso algunas párrafos hablan última milla – prioridad contenido medição |
| `borrador-proyectos.md` permite enlace opcional pieza clasificada D para coherencia lector rutas/OR cross-link |
| `knowAbout` propuesto JSON sólo tecnologías leídas; varios inglés porque producto software internacional marca |

Si algún principio debe revertirse (p.ej. separar proyecto hub sólo escritos primera persona Miguel) ajustable 3B.

---

## 7. Tiempo revisión estimado humano siguiente fase (**Ronda 3B**)

| Paso estimado tiempo | Ventana personas familiarizadas contenido previo Silodisa |
|----------------------|------------------------------------------------------------|
| Revisión tablas categorías + anclas links | ~45 min‑70 min |
| Completar bloques Pendiente biográficos | ~30 min (si datos listos externos) hasta **bloque abierto horas si investigación instituciones** previas |
| Alineación tonal portada nueva vs proyecto/trayectoria | ~35 min copy |
| QA cross-enlaces + nuevo `nav` cuando exista | ~35 min dev |

**Ventana combinada práctica orden magnitud medio día trabajo fraccionado** sin contar desarrollo HTML/CSS efectivo después aprobaciones.

---

## Cierre proceso 3A

Entregables sólo Markdown; **NINGÚN archivo producción tocado.** Listo siguiente iteración tras feedback propietario.
