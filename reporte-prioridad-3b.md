# Reporte de ejecución — Ronda 3B

Fecha de trabajo: **2026-05-12** (lastmod coherentes).

---

## 1. Respaldos creados

Carpeta: **`/Users/miguelmarengo/PROGRAMAS/miguel-marengo-canales-pagina-web/backup-prioridad-3b-2026-05-12/`**

| Archivo respaldado | Ruta absoluta dentro del workspace |
|--------------------|------------------------------------|
| `sitemap.xml` (estado anterior) | `backup-prioridad-3b-2026-05-12/sitemap.xml` |
| `index.html` (estado anterior) | `backup-prioridad-3b-2026-05-12/index.html` |

**Nota:** `site.css` se amplió con reglas locales para páginas 3B (`.page-trayectoria` / `.page-proyectos` / `.page-contacto` y lista de proyectos). No se guardó snapshot previo de `site.css` en esta carpeta; el estado anterior queda reproducible mediante control de versión (`git`) si ya estabas commiteando.

---

## 2. Archivos HTML creados

| Archivo | Secciones (H1 único + H2 mayor) | Palabras texto aprox.¹ | Schema JSON‑LD principal |
|---------|--------------------------------|------------------------|---------------------------|
| `trayectoria.html` | H1 Trayectoria; H2 ×7 (Síntesis, Competencia técnica con H3 ×4 dentro, Formación, Experiencia, Reconocimientos, Idiomas, Publicaciones) | **~608** | `@graph`: `WebPage` + `Person` (`#person`) con `hasOccupation`, `alumniOf`, `knowsLanguage`, `knowsAbout`, `award`, `sameAs`, `worksFor` |
| `proyectos.html` | H1 Proyectos; intro; H2 Área 1–3 (+ H3 material / aplicación según borrador); H2 Catálogo completo | **~483** | `CollectionPage` con `about` (tres ejes), `creator` `#person`, `mainEntity` `ItemList` de 9 ítems `Article` enlazadas por URL absoluta |
| `contacto.html` | H1 Contacto; H2 ×3 (Canales, Idiomas, Precisiones reputacionales según borrador) | **~102** | `ContactPage` con `mainEntity` `#person` |

¹ Conteo tras eliminar etiquetas/`script`; orientativo para densidad SERP vs HTML bruto (~1188 / ~1094 / ~371 tokens con `wc -w` del archivo).

**Validación de enlaces desde `borrador-proyectos.md`:** todas las rutas objetivo fueron confirmadas contra el filesystem del repo antes de cerrar marcado.

**Decisión de implementación revisable:**

- **`trayectoria.html`**: el nodo `@id …#person` se repite también en esta página para enriquecer con `hasOccupation`, `alumniOf`, etc. Mantener **`index.html`** como origen habitual del grafo; los buscadores suelen fusionar nodos mismo `@id` entre páginas, pero puede haber sutilezas en herramientas de validación. Si prefieres un solo archivo “fuente de verdad” para `Person`, en **ronda siguiente** puede reducirse a `mentions`/`WebPage.about` sólo desde trayectoría.
- **`knowsAbout`**: se derivaron competencias sólo desde el **borrador-trayectoria** (sin añadir p. ej. *Docker*, que aparece en **proyectos** pero no en trayectoría).
- **Texto modelo y proyectos**: se respeta textualmente «**enlazará** … cuando exista ese HTML» aun cuando **esta misma ronda** ya creó **`/proyectos.html`** (evita contenido nuevo no autorizado por el borrador).

---

## 3. Cambios en `index.html`

- **Menú (`site-nav`)**: enlaces a `/trayectoria.html`, `/proyectos.html`, `/contacto.html`; rutas también normalizadas a **root-relative** para Inicio (`/index.html`) y Publicaciones (`/publicaciones.html`).
- **CTA (“Material público técnico”)**: novedad **«Conocer trayectoria ampliada»** → `/trayectoria.html`; botón principal de publicaciones apunta a `/publicaciones.html`.
- **Pie de página**: enlaces a Trayectoría, Proyectos, Contacto y Publicaciones (todas rutas desde raíz); `precisiones-prensa` → `/precisiones-prensa.html`.

---

## 4. Diff `sitemap.xml` — antes vs. después (fragmento alto nivel)

### Antes (copia backup, cabeceras de URL)

Primera entrada seguía así (sin las tres páginas nuevas hasta `precisiones`):

```xml
  <url>
    <loc>https://www.miguelmarengocanales.com/</loc>
    <lastmod>2026-05-12</lastmod>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://www.miguelmarengocanales.com/precisiones-prensa.html</loc>
```

### Después (producción en repo tras 3B)

Tras `/` se insertan **tres URLs** antes de precisiones‑prensa:

```xml
  <url>
    <loc>https://www.miguelmarengocanales.com/trayectoria.html</loc>
    <lastmod>2026-05-12</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.miguelmarengocanales.com/proyectos.html</loc>
    <lastmod>2026-05-12</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://www.miguelmarengocanales.com/contacto.html</loc>
    <lastmod>2026-05-12</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.6</priority>
  </url>
```

El resto del sitemap (**home 1.0**, **precisiones 0.3**, artículos) quedó igual que en el backup correspondiente salvo estos bloques añadidos.

---

## 5. Verificaciones recomendadas post‑deploy

1. **`curl`** (respuesta **HTTP/2 200** esperada tras despliegue estático típico en Vercel):

   ```bash
   curl -sI https://www.miguelmarengocanales.com/trayectoria.html
   curl -sI https://www.miguelmarengocanales.com/proyectos.html
   curl -sI https://www.miguelmarengocanales.com/contacto.html
   ```

2. **Google Search Console**: inspección de URL por cada nueva ruta → «Solicitar indexación» cuando el deploy esté estable.
3. **Schema**: [validator.schema.org](https://validator.schema.org/) contra HTML publicado (`trayectoria`, `proyectos`, `contacto`).
4. **Open Graph / Twitter**: comprobar vistas previas ([opengraph.xyz](https://opengraph.xyz/) u herramienta equivalente).

---

## 6. Pendientes sugeridos — Ronda 4 (editorial / plantillas)

En línea con la orden de trabajo:

- Definir **6–12 temas** técnicos mensuales (calendario editorial).
- Consolidar una **plantilla HTML** reusada para nuevos artículos bajo `/publicaciones/`.
- Formalizar cadencia de **publicación y revisión** (owner + SLA editorial).

Opcional relacionado técnico: decidir si **solo `index`** declara grafo Person completo y las páginas 3B referencian vía `@id` sin repetir todas las propiedades.

---

## 7. Archivos modificados incidentalmente fuera del listado inicial de respaldo explícito

| Archivo | Motivo breve |
|---------|----------------|
| `site.css` | Estilos mínimos H3 subtítulos y listas de material (`page-proyectos`, etc.). |

No se modificaron **`precisiones-prensa.html`**, **`transparencia.html`**, **`vercel.json`**, **`robots.txt`** ni contenidos bajo **`/publicaciones/`**, conforme a prohibiciones explicitadas.
