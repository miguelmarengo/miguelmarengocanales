# Reporte consolidado — Ronda 3A.1

Fecha ejecución (Cursor / red): **2026-05-12** (cabeceras `curl` contra producción UTC).

---

## A — Validación redirect 301/308 `/transparencia`

### Comandos ejecutados

```bash
curl -sI https://www.miguelmarengocanales.com/transparencia.html | head -20
curl -sI https://www.miguelmarengocanales.com/transparencia | head -20
curl -sI https://miguelmarengocanales.com/transparencia.html | head -25
```

### Resultado obtenido

| Solicitud | Código HTTP | `Location` / notas |
|-----------|-------------|-------------------|
| `https://www.miguelmarengocanales.com/transparencia.html` | **200** | Sin header `Location`. Se sirve el HTML como recurso estático (`content-disposition: inline; filename="transparencia.html"`). |
| `https://www.miguelmarengocanales.com/transparencia` | **404** (`x-vercel-error: NOT_FOUND`) | Sin `Location` hacia `/precisiones-prensa.html`. |
| `https://miguelmarengocanales.com/transparencia.html` (apex) | **308** | `Location: https://www.miguelmarengocanales.com/transparencia.html` (solo canonicalización **host** hacia www; no fuerza `/precisiones-prensa`). |

### Diagnóstico

En el repositorio, `vercel.json` define redirecciones permanentes coherentes desde `/transparencia.html` y `/transparencia` hacia `/precisiones-prensa.html` (sin modificarse en esta ronda, según especificación):

```json
{ "source": "/transparencia.html", "destination": "/precisiones-prensa.html", "permanent": true }
```

El comportamiento en **www** (200 en `.html`, 404 en ruta sin extensión) **no coincide** con esas reglas. Causas plausibles a revisar en el dashboard de Vercel (esta ronda solo informa):

- Despliegue de producción generado desde un commit antiguo o rama sin el `vercel.json` actual.
- Proyecto en Vercel vinculado a otro directorio raíz o build que omite esa configuración.
- Promoción a producción desactualizada frente al último push (hay que revisar el deployment vigente).

**Estado marca en este reporte:** la validación **`transparencia` → `precisiones-prensa` en producción = NO OK** hasta que las respuestas sean **301/308** con `Location: /precisiones-prensa.html` (o URL absoluta equivalente).

*(Tras implementar el stub en este repo y desplegar, conviene repetir los mismos `curl -I`; el objetivo SEO sigue siendo intercepción en edge; el stub actúa como red de seguridad si el recurso llega como 200.)*

---

## B — Stub blindado `transparencia.html`

### Respaldo

- Copia legado: **`/backup-prioridad-3a1-2026-05-11/transparencia-legado.html`**  
  *(ruta absoluta en repo:* `…/backup-prioridad-3a1-2026-05-11/transparencia-legado.html`)*

### Archivo nuevo

- **`/transparencia.html`** sustituido por el stub mínimo acordado: `canonical` → `/precisiones-prensa.html`, `noindex, follow`, `meta refresh`, enlace navegable y `window.location.replace('/precisiones-prensa.html')`.

### Validaciones post-deploy recomendadas (propietario)

1. Tras próximo deploy: repetir **`curl -I`** de la sección A y confirmar redirect de servidor cuando proceda.
2. Navegador privado: abrir `/transparencia.html` y comprobar aterrizaje en **`/precisiones-prensa.html`** y etiqueta **`noindex`** en HTML servido (`Ver código fuente`).
3. Google Search Console (opcional): inspeccionar URL antigua cuando el redirect ya responda 301/308.

---

## C — Auditoría `.wix` en repositorio

### C.1 Inventario y método

- **Búsqueda por nombre**: archivos que contienen `.wix` en el nombre del fichero (**6 HTML** raíz / backup).
- **Carpeta Wix migrada**: **`/publicaciones/wix/`** — **31** artículos HTML (nombre sin `.wix`; contenido editorial migrado con plantilla del sitio).
- **Scripts** (referencia técnica, no página servida):  
  `/scripts/probe_wix_dates.py`, `/scripts/generate_wix_posts.py`.

Para los tres dumps de blog en raíz y sus copias bajo backup, `<title>` aparece dentro del HTML voluminoso típico de export Wix (**one-post:** «Logística Innovadora»; **p2/p3:** página blog Silodisa con paginación Wix legacy).

### C.2 Tabla de clasificación y acciones

| Ruta dentro del repo (absoluto workspace) | ~palabras¹ | `<title>` útil | `<meta robots>` antes → después² | ¿Enlazado en sitio?³ | Editorial | Cat | Acción |
|----------|:-:|:--|:--|:--|:--|:--|:---|
| `publicaciones/wix/*.html` (×31 migrados; ej. `…/logistica-innovadora.html` ~383w; ejemplo largo `…/mas-alla-del-hype-…html` ~1148w) | ~400–1150 típico | Sí (`index,follow`) | `index,follow` | Sí (`publicaciones.html`, navegación; **sitemap**) | Migración editorial legítima | **A** | Ninguna; **mantener en sitemap** |
| `.wix-one-post.html` | ~13.9k | Sí | `noindex,nofollow` (íntegro); **+<link canonical>** hacia **`/publicaciones/wix/logistica-innovadora.html`** | No | Dump duplica artículo canónico | **D** | Canonical + robots ya Cubierto robots.txt |
| `backup-prioridad-1-2026-05-12/wix-orphan/.wix-one-post.html` | ~igual copia | Sí | faltaban control temprano → **`noindex,nofollow` + canonical `logistica-innovadora.html`** | No | Duplicado | **D** | Aplicado meta + canonical; carpeta **`Disallow` robots** |
| `.wix-blog-p2.html` | ~17.5k | Sí (`Blog \| Silodisa`) | `noindex,nofollow`; **+<link canonical `publicaciones.html`** | No | Scaffolding lista Wix legacy | **C** | Canonical refuerzo; robots.txt ya negaba archivo |
| `.wix-blog-p3.html` | ~17.4k | Ídem p2 | ídem | No | Ídem | **C** | Ídem |
| `backup…/wix-orphan/.wix-blog-p2.html` | ~igual | Sí | faltaban → **`noindex,nofollow` + canonical hub** | No | Ídem | **C** | Ídem |
| `backup…/wix-orphan/.wix-blog-p3.html` | ~igual | Sí | faltaban → **`noindex,nofollow` + canonical hub** | No | Ídem | **C** | Ídem |
| `scripts/probe_wix_dates.py`, `scripts/generate_wix_posts.py` | N/A código | — | — | No | Herramienta generación interna | *(n/a)* | No requiere `robots` de página |

¹ `wc -w` sobre muestras representativas.

² El orden en el dumps Wix también conserva enlaces `<link rel="canonical" href="https://miguelmarengo1.wixsite.com/…">` profundos en el archivo; los **primeros `<link rel="canonical">`** en orden DOM suelen tener precedencia al añadir en `<head>` al inicio; no se saneó todo el scaffolding JSON Wix innecesario.

³ Grep enlaces `href` → `.wix-*.html` en HTML del sitio: **sin coincidencias** (los dumps no están enlazados desde navegación).

### C.3 Categoría B (huérfanos editoriales **con valor** pero sin enlace desde el sitio)

**Ningún candidato.** Los artículos con valor están bajo **`/publicaciones/wix/`** y ya están listados desde **`publicaciones.html`** y el **sitemap**.

### C.4 `robots.txt` — antes vs. después

**Antes:**

```txt
User-agent: *
Disallow: /.wix-one-post.html
Disallow: /.wix-blog-p2.html
Disallow: /.wix-blog-p3.html
Allow: /

Sitemap: https://www.miguelmarengocanales.com/sitemap.xml
```

**Después:**

```txt
User-agent: *
Allow: /
Disallow: /.wix-one-post.html
Disallow: /.wix-blog-p2.html
Disallow: /.wix-blog-p3.html
Disallow: /backup-prioridad-*/

Sitemap: https://www.miguelmarengocanales.com/sitemap.xml
```

- **`Disallow: /backup-prioridad-*/`** cubre copias dentro de **`backup-prioridad-…`** (incl. `…/wix-orphan/`) ante despliegue accidental de carpetas backup.
- Se reordenó `Allow: /` arriba según formato recomendado en la orden de ronda.

### C.5 `sitemap.xml`

**Sin cambios en esta ronda.** No listaba rutas **`/.wix-*`** ni carpetas **`backup`**; solo entradas canónicas (incluso **`publicaciones/wix/*`**, categoría **A**). Eliminaciones de URLs categoría **C/D** **no aplican** porque esas rutas ya no aparecían en el sitemap.

---

## D — Normalización de rutas en borradores `.md`

| Archivo | Cambios realizados |
|---------|---------------------|
| `borrador-trayectoria.md` | **Ninguno.** El enlace Markdown interno `[…](/publicaciones.html)` ya cumple política root-relative. |
| `borrador-proyectos.md` | **Ninguno.** Todos los destinos revisados están como `/publicaciones/…`. |
| `borrador-contacto.md` | **Ninguno.** La ruta **`/precisiones-prensa.html`** ya aparece como root-relative dentro del párrafo de precisiones reputacionales. |

**Enlaces externos** (ej. perfil LinkedIn en `contacto`): **sin alteración**, permanecen con URL absoluta `https://…`.

---

## E — Estado general del sitio (según inventario repo + producción antes del próximo deploy)

| Concepto | Detalle breve |
|----------|----------------|
| URLs declaradas como indexables fuertes (sitemap) | **39** entradas en `sitemap.xml`: home, `precisiones-prensa`, `publicaciones`, 5 autorales bajo `/publicaciones/`, 31 bajo **`/publicaciones/wix/`**. |
| Meta `robots index` páginas públicas típicas | `index.html`, `publicaciones.html`, `precisiones-prensa.html`, artículos bajo **`/publicaciones/`** y **`/publicaciones/wix/`**. |
| `noindex` (intención) | Dumps **`/.wix-*`** (`noindex,nofollow`); nuevo **`transparencia.html`** stub (`noindex, follow`). Tras deploy, cualquier recurso dentro **`/backup-prioridad-*/`** queda desaconsejado vía **`robots.txt`**. |
| Redirects conocidos **`vercel.json`** | Apex `miguelmarengocanales.com` → **www**; `*.vercel.app` → www; **intentado** `/transparencia(.html)` → **`/precisiones-prensa.html`** (⚠ persisten discrepancias en www según §A hasta validar deployment). |
| `sitemap.xml` | Íntegro; bloque marcado **`WIX-SITEMAP-START`/`END`**; **sin `transparencia.html`**. |

---

## F — Pendientes Ronda **3A.2** (revisión humana)

### Campos `[PENDIENTE]` en borradores

Detalle en tablas texto original; resumen ejecutivo:

- **`borrador-trayectoria.md`:** nivel público papel frente a equipo/inventarios; ejemplo interno datos; si reforzar eje tras nuevos HTML; bloque **formación académica** completo o negativa pública; **título/oficial y periodos** vs. schema `jobTitle`; **historial otros empleadores** solo si se documenta o consiente.
- **`borrador-proyectos.md`:** decisiones curatoriales orden/bloques UI (`details`, títulos cortos, etc.).
- **`borrador-contacto.md`:** email público u otras opciones; enlaces opcionales (GitHub/ORCID/Scholar); política eventual formulario y datos personales México/EU.

### Decisiones humanas relacionadas auditoría `.wix`

- Ningún huérfano editorial **Categoría B** detectado para desanclar/decidir.
- Si en el futuro se **elimina físicamente** los dumps **`/.wix-*.html`**, pueden retirarse entradas concretas de `Disallow`; mientras tanto se mantienen como capas de control.

---

## G — Pendientes Ronda **3B** (publicación)

Tras cierre editorial de borradores, típicamente se **crearán** (esta ronda **no los generó**) las páginas:

| Archivo | Metadatos (desde borradores propuestos) |
|---------|----------------------------------------|
| **`trayectoria.html`** | `title`: *Trayectoria profesional — Miguel Marengo Canales*; meta description textual ~147 chars; probable JSON-LD `Person` refinado desde borrador §metadatos. |
| **`proyectos.html`** | `title`: *Proyectos y áreas de trabajo — Miguel Marengo Canales*; meta description ~147 chars; cuerpo hub por áreas con enlaces existentes **`/publicaciones/…`** y **`/publicaciones/wix/…`**. |
| **`contacto.html`** | `title`: *Contacto profesional — Miguel Marengo Canales*; meta description revisada cuando existan otros canales públicos (`[PENDIENTE]` borrador); contenido centrado canal LinkedIn inicial. |

Enlaces internos nuevos páginas: seguir política **`/` root-relative**; absolutas solo donde corresponda (canonical, OG, JSON-LD, sitemap).

---

*Fin reporte Ronda 3A.1.*
