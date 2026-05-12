# Reporte Prioridad 2 — Migración a `precisiones-prensa.html`

## Inventario de cambios

- **Página nueva:** `precisiones-prensa.html` — documento de precisiones sobre menciones en prensa (JSON-LD `Article`, canonical/OG coherentes con `2026-05-11`; secciones Precisión 1 y 2, documentos, marco normativo, contacto).
- **Redirección 301 (Vercel):** En `vercel.json` se añadieron:
  - `/transparencia.html` → `/precisiones-prensa.html`
  - `/transparencia` → `/precisiones-prensa.html`
- **`sitemap.xml`:** Eliminada la URL `transparencia.html`; añadida `precisiones-prensa.html` con `priority` 0.3, `changefreq` monthly, `lastmod` 2026-05-11.
- **`site.css`:** Reglas `.precision-svg-wrap` y `.precision-svg` bajo `.page-transparencia` para los SVG compactos inline.
- **Enlaces internos:** Todas las referencias navegacionales `transparencia.html` fuera del archivo legado fueron sustituidas por `precisiones-prensa.html`; el texto del enlace en nav unificado como «Precisiones sobre menciones en prensa». Incluye `index.html` (pie), `publicaciones.html`, artículos bajo `publicaciones/` y `publicaciones/wix/`, y plantilla `scripts/generate_wix_posts.py`.
- **Archivos no tocados deliberadamente:** `transparencia.html` conserva sus meta y canonical autopublicados hasta validar en producción el 301 y el rastreo. Las rutas físicas `--> /documentos/transparencia/...` siguen igual (sólo el nombre de carpeta).

## Correcciones de contenido residuales

- Eliminados artefactos de texto corrupto en «Contacto para correcciones documentadas» y pulido del ítem SIP/SPJ/UNESCO en Marco normativo.
- Alineación terminológica: «Precisión 1/2» en lugar de «Caso» donde correspondía.

## Comprobaciones post-deploy (manual)

1. **301:** Solicitar `https://www.miguelmarengocanales.com/transparencia.html` y `.com/transparencia` y verificar código **308/301** hacia `/precisiones-prensa.html` (según comportamiento exacto del edge).
2. **Sitemap:** En Search Console / índices, vigilar que el nuevo URL aparezca y que el viejo deje de indexarse tras redirección.
3. **Enlaces desde artículos:** Abrir cualquier pieza `publicaciones/*` y comprobar que el nav apunte correctamente desde rutas relativas (`../`, `../../`).
4. Opcional tras estabilización: retirar o transformar `transparencia.html` en una página mínima de aviso/redirección en cliente sólo si se desea; hoy **no es necesario** mientras exista redirect de servidor.

## Nota sobre anclas heredadas

Quienes enlacen `#caso-puga-transparencia` o `#contexto-publico-documentado` desde copias viejas pueden recibir contenido incompleto; el servidor no reescribe hash. El volumen debe ser bajo tras el canonical y el 301; si aparece necesidad documentada, se puede añadir `id` de compatibilidad en `precisiones-prensa.html`.
