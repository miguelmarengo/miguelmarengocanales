# Reporte Prioridad 1 — Archivos `.wix-*.html`

Fecha del informe: 2026-05-12.

## Archivos tratados como *scaffolding* (sin valor editorial autónomo)

Los tres únicos prefijos `.wix-*.html` detectados en el repositorio son volcados de **Wix.com Website Builder** (generador declarado en el propio `<head>`), marcado masivo tipo runtime de la plataforma, sin `<title>` útil ni URL canónica propia comparable a las páginas del sitio.

| Archivo | Contenido aparente | Recomendación aplicada |
|--------|--------------------|-------------------------|
| `.wix-one-post.html` | SPA/plantilla de post Wix (~14k líneas de JS/CSS/embed) | `noindex, nofollow` en meta + `Disallow` en `robots.txt` |
| `.wix-blog-p2.html` | Listado/markup repetido página de blog paginación 2 | Idem |
| `.wix-blog-p3.html` | Listado/markup repetido página de blog paginación 3 | Idem |

Los **textos editoriales vigentes para visitantes** están en `publicaciones.html` y en `publicaciones/wix/*.html`, que son HTML estático legible fuera del volcado Wix. No se detectó contenido sustantivo adicional sólo visible en estos archivos huérfanos que amerite mantenerlos indexables.

Si en algún momento se localizara contenido editorial exclusivo dentro de estos dumps, convendría **extraer fragmento editorial → artículo en `publicaciones/`** con URL canónica y `BlogPosting`; hasta entonces mantener **`noindex` + bloque `Disallow`** evita gasto de rastreo y señales duplicadas (criterios alineados a Google Search Essentials sobre contenido útil y control de crawling).
