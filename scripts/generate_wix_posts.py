#!/usr/bin/env python3
"""
Descarga el texto principal de cada post del blog Wix con trafilatura,
lee datePublished del JSON-LD en el HTML, y genera HTML estático en
publicaciones/wix/ para miguelmarengocanales.com

Uso (desde la raíz del repo):
  pip install -t .vendor trafilatura
  PYTHONPATH=.vendor python3 scripts/generate_wix_posts.py

Actualiza también publicaciones.html (bloque <!-- PUBLICACIONES-RUBROS-START/END -->:
contenido agrupado por rubro) y las URLs Wix en sitemap.xml
(<!-- WIX-SITEMAP-START/END -->).

Comprobación rápida de fechas JSON-LD sin regenerar HTML:
  python3 scripts/probe_wix_dates.py
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import textwrap
import unicodedata
from datetime import datetime, timezone
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "publicaciones" / "wix"
PUBLICACIONES_HTML = ROOT / "publicaciones.html"
SITEMAP_XML = ROOT / "sitemap.xml"
VENDOR = ROOT / ".vendor"
# Fecha de respaldo para lastmod si falta date en el manifiesto.
DEFAULT_LASTMOD = "2026-05-11"

MONTHS_ES = (
    "enero",
    "febrero",
    "marzo",
    "abril",
    "mayo",
    "junio",
    "julio",
    "agosto",
    "septiembre",
    "octubre",
    "noviembre",
    "diciembre",
)

SLUGS: list[str] = [
    "más-allá-del-hype-cómo-la-inteligencia-artificial-y-la-investigación-de-operaciones-están-optimizan",
    "logística-en-tiempo-real-por-qué-los-promedios-de-30-días-están-matando-tu-cadena-de-suministro",
    "más-allá-del-dato-por-qué-la-logística-de-clase-mundial-exige-medir-la-realidad-en-tiempo-real",
    "de-la-medición-a-la-acción-cómo-los-kpis-y-la-mejora-continua-definen-nuestra-excelencia-logística",
    "más-allá-del-echale-ganas-por-qué-la-cultura-de-datos",
    "más-allá-del-esfuerzo-la-ciencia-de-la-medición-logística-en-tiempo-real",
    "blog-silodisa-la-alineación-nuestro-motor-para-resultados-extraordinarios",
    "el-doble-motor-de-nuestro-éxito-precisión-en-el-inventario-y-pasión-en-nuestra-gente",
    "la-filosofía-del-cero-error-por-qué-en-silodisa-la-precisión-del-inventario-es-una-obsesión",
    "el-nearshoring-está-aquí-tu-socio-logístico-está-realmente-preparado",
    "el-poder-del-asombro-impulsando-la-motivación-en-silodisa-para-2025",
    "más-que-una-empresa-una-comunidad-el-ingrediente-secreto-de-silodisa",
    "de-tláloc-a-la-nube-cómo-la-sabiduría-ancestral-inspira-la-logística-sostenible-de-silodisa-mx",
    "detrás-de-cada-botella-de-electrolit-la-misión-esencial-de-silodisa",
    "en-silodisa-cada-dato-cuenta-la-clave-de-nuestra-excelencia-operativa",
    "en-silodisa-la-tecnología-tiene-un-propósito-tu-familia",
    "innovación-cumplimiento-y-bienestar-así-construimos-juntos-el-futuro-en-silodisa",
    "más-que-agua-el-gesto-que-muestra-el-corazón-de-silodisa",
    "cansado-del-caos-usa-los-secretos-de-la-logística-para-organizar-tu-vida-y-alcanzar-tus-metas",
    "datos-lo-que-diferencia-a-silodisa",
    "hackea-tu-felicidad-y-productividad-el-plan-definitivo-de-las-mejores-universidades-del-mundo-para",
    "la-importancia-de-las-evidencias-en-la-logística-garantizando-una-entrega-perfecta",
    "la-revolución-silenciosa-en-tu-almacén-cómo-la-ia-y-la-tecnología-están-redefiniendo-la-logística",
    "las-tendencias-más-innovadoras-en-la-logística-actual-2023",
    "el-futuro-de-la-logística-tendencias-e-innovaciones",
    "el-papel-de-la-inteligencia-artificial-en-la-optimización-de-la-logística",
    "la-importancia-de-un-almacén-caótico-y-sus-beneficios",
    "importancia-del-cumplimiento-perfecto-del-pedido-pof",
    "optimizando-el-diseño-del-almacén-para-mejorar-la-eficiencia",
    "optimizando-la-planificación-de-rutas-con-algoritmos-avanzados",
    "logística-innovadora",
]

# Clasificación temática (debe incluir exactamente cada slug de SLUGS).
SLUG_RUBRO: dict[str, str] = {
    "más-allá-del-hype-cómo-la-inteligencia-artificial-y-la-investigación-de-operaciones-están-optimizan": "ai",
    "logística-en-tiempo-real-por-qué-los-promedios-de-30-días-están-matando-tu-cadena-de-suministro": "operaciones",
    "más-allá-del-dato-por-qué-la-logística-de-clase-mundial-exige-medir-la-realidad-en-tiempo-real": "operaciones",
    "de-la-medición-a-la-acción-cómo-los-kpis-y-la-mejora-continua-definen-nuestra-excelencia-logística": "operaciones",
    "más-allá-del-echale-ganas-por-qué-la-cultura-de-datos": "liderazgo",
    "más-allá-del-esfuerzo-la-ciencia-de-la-medición-logística-en-tiempo-real": "operaciones",
    "blog-silodisa-la-alineación-nuestro-motor-para-resultados-extraordinarios": "liderazgo",
    "el-doble-motor-de-nuestro-éxito-precisión-en-el-inventario-y-pasión-en-nuestra-gente": "rh",
    "la-filosofía-del-cero-error-por-qué-en-silodisa-la-precisión-del-inventario-es-una-obsesión": "operaciones",
    "el-nearshoring-está-aquí-tu-socio-logístico-está-realmente-preparado": "operaciones",
    "el-poder-del-asombro-impulsando-la-motivación-en-silodisa-para-2025": "rh",
    "más-que-una-empresa-una-comunidad-el-ingrediente-secreto-de-silodisa": "rh",
    "de-tláloc-a-la-nube-cómo-la-sabiduría-ancestral-inspira-la-logística-sostenible-de-silodisa-mx": "operaciones",
    "detrás-de-cada-botella-de-electrolit-la-misión-esencial-de-silodisa": "operaciones",
    "en-silodisa-cada-dato-cuenta-la-clave-de-nuestra-excelencia-operativa": "operaciones",
    "en-silodisa-la-tecnología-tiene-un-propósito-tu-familia": "rh",
    "innovación-cumplimiento-y-bienestar-así-construimos-juntos-el-futuro-en-silodisa": "rh",
    "más-que-agua-el-gesto-que-muestra-el-corazón-de-silodisa": "rh",
    "cansado-del-caos-usa-los-secretos-de-la-logística-para-organizar-tu-vida-y-alcanzar-tus-metas": "operaciones",
    "datos-lo-que-diferencia-a-silodisa": "tecnologia",
    "hackea-tu-felicidad-y-productividad-el-plan-definitivo-de-las-mejores-universidades-del-mundo-para": "rh",
    "la-importancia-de-las-evidencias-en-la-logística-garantizando-una-entrega-perfecta": "operaciones",
    "la-revolución-silenciosa-en-tu-almacén-cómo-la-ia-y-la-tecnología-están-redefiniendo-la-logística": "ai",
    "las-tendencias-más-innovadoras-en-la-logística-actual-2023": "tecnologia",
    "el-futuro-de-la-logística-tendencias-e-innovaciones": "tecnologia",
    "el-papel-de-la-inteligencia-artificial-en-la-optimización-de-la-logística": "ai",
    "la-importancia-de-un-almacén-caótico-y-sus-beneficios": "operaciones",
    "importancia-del-cumplimiento-perfecto-del-pedido-pof": "operaciones",
    "optimizando-el-diseño-del-almacén-para-mejorar-la-eficiencia": "operaciones",
    "optimizando-la-planificación-de-rutas-con-algoritmos-avanzados": "operaciones",
    "logística-innovadora": "operaciones",
}

# Orden fijo de rubros en la página (clave interna, id HTML, título, texto intro).
RUBROS: list[tuple[str, str, str, str]] = [
    ("rh", "rubro-rh", "Recursos humanos", "Cultura, personas, motivación y bienestar laboral."),
    ("liderazgo", "rubro-liderazgo", "Liderazgo", "Alineación, dirección de equipos y cultura de datos."),
    ("operaciones", "rubro-operaciones", "Operaciones", "Cadena de suministro, almacén, cumplimiento, mediciones y ejecución."),
    ("tecnologia", "rubro-tecnologia", "Tecnología", "Sistemas, datos, plataformas y tendencias digitales."),
    ("ai", "rubro-ai", "Inteligencia artificial (IA)", "IA aplicada, optimización y algoritmos en contexto operativo."),
    ("agentic", "rubro-agentic", "Agentic AI", "Agentes autónomos, orquestación y flujos agentic (contenido en expansión)."),
]

# Publicaciones alojadas en este sitio (no Wix), con rubro y ficha para la portada de publicaciones.
NATIVE_PUBLICATIONS: list[dict] = [
    {
        "rubro": "tecnologia",
        "href": "publicaciones/biblioteca-videos-uroutes-silodisa.html",
        "title": "Biblioteca de video uRoutes — 17 clips",
        "date": "2026-05-12",
        "time_display": "Catálogo · ~2 min c/u · sin fechas por clip en origen",
        "summary": (
            "Introducción, panorama del ecosistema (11 módulos), WMS, TMS, CRM, almacén operativo, router web, "
            "distribución OR-Tools y app del chofer. Textos alineados a silodisa.com/es/videos; vídeos vía embed público de "
            "Synthesia."
        ),
        "cta": "Abrir biblioteca",
    },
    {
        "rubro": "tecnologia",
        "href": "publicaciones/cursor-zed-antigravity-ides-logistica.html",
        "title": "Cursor, Zed y Antigravity: IDEs para software de logística",
        "date": "2026-05-12",
        "summary": (
            "Ventajas y contrastes de tres entornos (IA integrada, colaboración en tiempo real, flujos agent-first) "
            "con ejemplos de rutas, almacén e integraciones; criterios para elegir sin imponer un único ganador."
        ),
        "cta": "Leer completo",
    },
    {
        "rubro": "ai",
        "href": "publicaciones/uroutes-heuristica-mejores-rutas.html",
        "title": "uRoutes: rutas excelentes sin pelear con el mapa (sí, con heurística)",
        "date": "2026-05-12",
        "summary": (
            "De «one map, full chain» a OR-Tools, ventanas de tiempo y un solo hilo WMS/TMS/CRM — con guiños a "
            "planificadores humanos que aún creen que el Excel compite en la liga de los solvers."
        ),
        "cta": "Leer completo",
    },
    {
        "rubro": "tecnologia",
        "href": "publicaciones/trazabilidad-datos-decisiones-logistica.html",
        "title": "Trazabilidad de datos en decisiones de cadena de suministro",
        "date": "2026-05-11",
        "summary": (
            "Cómo documentar el recorrido de los datos desde su captura hasta la decisión operativa reduce riesgo y "
            "acelera auditorías internas. Revisión práctica orientada a equipos pequeños y medianos."
        ),
        "cta": "Leer completo",
    },
]


def assert_slug_rubro_coverage() -> None:
    if set(SLUGS) != set(SLUG_RUBRO.keys()):
        missing = set(SLUGS) - set(SLUG_RUBRO.keys())
        extra = set(SLUG_RUBRO.keys()) - set(SLUGS)
        raise RuntimeError(f"SLUG_RUBRO desalineado con SLUGS. Faltan: {missing!r} Sobran: {extra!r}")


def slugify_filename(slug: str) -> str:
    s = unicodedata.normalize("NFD", slug)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.lower().replace(" ", "-")
    s = re.sub(r"[^a-z0-9-]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "post"


def curl_html(url: str) -> str:
    r = subprocess.run(
        ["/usr/bin/curl", "-sL", "--max-time", "45", url],
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        raise RuntimeError(f"curl failed: {url}")
    return r.stdout


def extract_date_published(html: str) -> str | None:
    m = re.search(
        r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2}T[^"]+)"',
        html,
    )
    return m.group(1) if m else None


def format_long_date(iso: str) -> str:
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        dt = dt.astimezone(timezone.utc)
        d, mo, y = dt.day, dt.month, dt.year
        return f"{d} de {MONTHS_ES[mo - 1]} de {y}"
    except Exception:
        return iso[:10]


def extract_body_text(html: str) -> tuple[str, str | None]:
    wp = str(VENDOR)
    if wp not in sys.path:
        sys.path.insert(0, wp)
    import trafilatura

    text = trafilatura.extract(html, include_comments=False, include_tables=True)
    meta = trafilatura.extract_metadata(html)
    ttl = meta.title if meta else None
    return (text or "").strip(), ttl


def text_to_html_paragraphs(text: str) -> str:
    """Convierte texto extraído en HTML. Si no hay párrafos dobles, usa una línea = un bloque."""
    if not text:
        return "<p><em>No se pudo extraer el cuerpo del artículo.</em></p>"

    # Preferir bloques separados por línea en blanco (estilo Markdown).
    blocks = re.split(r"\n\s*\n+", text.strip())
    if len(blocks) == 1 and "\n" in blocks[0]:
        # Texto plano denso: una línea visible = un párrafo corto.
        blocks = [ln.strip() for ln in blocks[0].split("\n") if ln.strip()]

    parts: list[str] = []
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        lines = block.split("\n")
        first = lines[0].strip()
        if first.startswith("### "):
            parts.append(f'<h3>{escape(first[4:].strip())}</h3>')
            rest = "\n".join(lines[1:]).strip()
            if rest:
                inner = "<br />\n            ".join(
                    escape(x.strip()) for x in rest.split("\n") if x.strip()
                )
                parts.append(f"<p>{inner}</p>")
        elif first.startswith("## "):
            parts.append(f'<h2>{escape(first[3:].strip())}</h2>')
            rest = "\n".join(lines[1:]).strip()
            if rest:
                inner = "<br />\n            ".join(
                    escape(x.strip()) for x in rest.split("\n") if x.strip()
                )
                parts.append(f"<p>{inner}</p>")
        elif len(lines) == 1:
            parts.append(f"<p>{escape(block)}</p>")
        else:
            inner = "<br />\n            ".join(escape(x.strip()) for x in lines if x.strip())
            parts.append(f"<p>{inner}</p>")
    return "\n        ".join(parts) if parts else "<p></p>"


def render_publicaciones_por_rubro(manifest: list[dict]) -> str:
    """HTML entre PUBLICACIONES-RUBROS-START y END: secciones por rubro, entradas por fecha."""
    assert_slug_rubro_coverage()
    wix_by: dict[str, list[dict]] = {k: [] for k, _, _, _ in RUBROS}
    for x in manifest:
        slug = x.get("slug") or ""
        r = x.get("rubro") or SLUG_RUBRO.get(slug, "operaciones")
        if r not in wix_by:
            r = "operaciones"
        wix_by[r].append(x)
    natives_by: dict[str, list[dict]] = {k: [] for k, _, _, _ in RUBROS}
    for n in NATIVE_PUBLICATIONS:
        natives_by[n["rubro"]].append(n)

    lines: list[str] = ["      <!-- PUBLICACIONES-RUBROS-START -->"]

    for key, sid, sec_title, lead in RUBROS:
        merged: list[tuple[str, dict]] = []
        for n in natives_by[key]:
            merged.append(("native", n))
        for x in wix_by[key]:
            merged.append(("wix", x))
        merged.sort(key=lambda t: t[1].get("date") or "", reverse=True)

        lines.append(
            f'      <section class="content pub-rubro-section" id="{escape(sid)}" '
            f'aria-labelledby="{escape(sid)}-heading">'
        )
        lines.append(
            f'        <h2 id="{escape(sid)}-heading" class="pub-section-title">{escape(sec_title)}</h2>'
        )
        lines.append(f'        <p class="pub-section-lead">{escape(lead)}</p>')

        if not merged:
            if key == "agentic":
                lines.append(
                    '        <p class="pub-rubro-empty"><em>Aún no hay publicaciones clasificadas en este rubro.</em></p>'
                )
            lines.append("      </section>")
            continue

        lines.append('        <div class="pub-rubro-body">')
        for kind, obj in merged:
            if kind == "native":
                td = escape(obj["date"])
                vis = escape(obj.get("time_display") or obj["date"])
                lines.append('          <article class="paper pub-card">')
                lines.append(f"            <h3>{escape(obj['title'])}</h3>")
                lines.append(f'            <time class="pub-date" datetime="{td}">{vis}</time>')
                lines.append(f'            <p class="pub-summary">{escape(obj["summary"])}</p>')
                lines.append(
                    f'            <a class="btn-read" href="{escape(obj["href"])}">{escape(obj["cta"])}</a>'
                )
                lines.append("          </article>")
            else:
                d = escape(obj.get("date") or "")
                t = escape(obj["title"])
                href = escape(f"publicaciones/wix/{obj['file']}")
                lines.append('          <article class="paper pub-card">')
                lines.append(f"            <h3>{t}</h3>")
                lines.append(f'            <time class="pub-date" datetime="{d}">{d}</time>')
                lines.append(f'            <a class="btn-read" href="{href}">Leer artículo</a>')
                lines.append("          </article>")
        lines.append("        </div>")
        lines.append("      </section>")

    lines.append("      <!-- PUBLICACIONES-RUBROS-END -->")
    return "\n".join(lines) + "\n"


def patch_publicaciones_rubros_section(manifest: list[dict]) -> None:
    if not PUBLICACIONES_HTML.is_file():
        print("Aviso: no existe publicaciones.html, se omite el índice por rubros.", file=sys.stderr)
        return
    text = PUBLICACIONES_HTML.read_text(encoding="utf-8")
    if "<!-- PUBLICACIONES-RUBROS-START -->" not in text:
        print(
            "Aviso: publicaciones.html no tiene <!-- PUBLICACIONES-RUBROS-START -->; añade los marcadores.",
            file=sys.stderr,
        )
        return
    block = render_publicaciones_por_rubro(manifest)
    new_text, n = re.subn(
        r"      <!-- PUBLICACIONES-RUBROS-START -->.*?      <!-- PUBLICACIONES-RUBROS-END -->\n",
        block,
        text,
        count=1,
        flags=re.DOTALL,
    )
    if n != 1:
        print("Aviso: no se reemplazó el bloque de rubros en publicaciones.html.", file=sys.stderr)
        return
    PUBLICACIONES_HTML.write_text(new_text, encoding="utf-8")


def patch_sitemap_wix_urls(manifest: list[dict]) -> None:
    if not SITEMAP_XML.is_file():
        print("Aviso: no existe sitemap.xml, se omite.", file=sys.stderr)
        return
    parts: list[str] = [
        "  <!-- WIX-SITEMAP-START -->",
    ]
    for x in sorted(manifest, key=lambda z: z.get("file") or ""):
        lm = (x.get("date") or DEFAULT_LASTMOD).strip()
        fn = x["file"]
        loc = f"https://www.miguelmarengocanales.com/publicaciones/wix/{fn}"
        parts.append("  <url>")
        parts.append(f"    <loc>{escape(loc)}</loc>")
        parts.append(f"    <lastmod>{escape(lm)}</lastmod>")
        parts.append("    <changefreq>yearly</changefreq>")
        parts.append("    <priority>0.65</priority>")
        parts.append("  </url>")
    parts.append("  <!-- WIX-SITEMAP-END -->")
    block = "\n".join(parts) + "\n"
    text = SITEMAP_XML.read_text(encoding="utf-8")
    if "<!-- WIX-SITEMAP-START -->" in text:
        new_text, n = re.subn(
            r"  <!-- WIX-SITEMAP-START -->.*?  <!-- WIX-SITEMAP-END -->\n",
            block,
            text,
            count=1,
            flags=re.DOTALL,
        )
        if n != 1:
            print("Aviso: no se reemplazó el bloque Wix en sitemap.xml.", file=sys.stderr)
            return
        SITEMAP_XML.write_text(new_text, encoding="utf-8")
        return
    if "</urlset>" not in text:
        print("Aviso: sitemap.xml no contiene </urlset>.", file=sys.stderr)
        return
    SITEMAP_XML.write_text(text.replace("</urlset>", block + "</urlset>", 1), encoding="utf-8")


def page_template(
    *,
    title: str,
    iso_date: str,
    long_date: str,
    body_html: str,
    canonical_path: str,
) -> str:
    canon = f"https://www.miguelmarengocanales.com{canonical_path}"
    esc_title = escape(title)
    return f"""<!DOCTYPE html>
<html lang="es-MX">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#050810" />
    <link rel="preload" href="/site.css" as="style" />
    <meta name="description" content="{escape(title[:155])}" />
    <meta name="robots" content="index, follow" />
    <meta name="author" content="Miguel Marengo Canales" />
    <meta property="og:type" content="article" />
    <meta property="og:locale" content="es_MX" />
    <meta property="og:title" content="{esc_title}" />
    <meta property="article:published_time" content="{iso_date[:10]}" />
    <meta property="og:url" content="{canon}" />
    <link rel="canonical" href="{canon}" />
    <link rel="stylesheet" href="/site.css" />
    <title>{esc_title} — Publicaciones técnicas</title>
    <script type="application/ld+json">
{json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": title,
            "datePublished": iso_date,
            "dateModified": iso_date,
            "url": canon,
            "inLanguage": "es-MX",
            "author": {"@id": "https://www.miguelmarengocanales.com/#person"},
            "isPartOf": {"@id": "https://www.miguelmarengocanales.com/#website"},
        },
        ensure_ascii=False,
        indent=2,
    )}
    </script>
  </head>
  <body class="page-publicaciones">
    <nav class="site-nav" aria-label="Menú principal">
      <a href="../../index.html">Inicio</a>
      <a href="../../publicaciones.html" aria-current="page">Publicaciones técnicas</a>
      <a href="../../precisiones-prensa.html">Precisiones sobre menciones en prensa</a>
      <a href="../../precisiones-prensa.html#criterios-verificacion" class="nav-muted">Criterios de análisis</a>
    </nav>
    <main class="wrap">
      <p class="pub-back">
        <a href="../../publicaciones.html">← Índice de publicaciones</a>
      </p>
      <header class="hero pub-article-hero" id="top">
        <h1>{esc_title}</h1>
        <p class="tagline">
          Publicado el <time datetime="{iso_date[:10]}">{long_date}</time>
        </p>
      </header>
      <article class="paper content">
        {body_html}
      </article>
      <footer class="doc-foot">
        <p>
          <a href="../../publicaciones.html">Índice de publicaciones</a>
        </p>
      </footer>
    </main>
    <script src="/vercel-analytics.js"></script>
  </body>
</html>
"""


def main() -> None:
    assert_slug_rubro_coverage()
    if not (VENDOR / "trafilatura").exists():
        print("Instala dependencias: pip install -t .vendor trafilatura", file=sys.stderr)
        sys.exit(1)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest: list[dict] = []
    for slug in SLUGS:
        wix_url = f"https://miguelmarengo1.wixsite.com/my-site/post/{slug}"
        print("Fetching", slug[:50], "...", flush=True)
        html = curl_html(wix_url)
        iso = extract_date_published(html) or ""
        body_txt, meta_title = extract_body_text(html)
        title = (meta_title or "").strip() or slug.replace("-", " ").title()
        # Título: primera línea del cuerpo si no hay meta útil
        if len(title) < 10 and body_txt:
            first = body_txt.strip().split("\n", 1)[0].strip()
            if first:
                title = first[:200]
        long_d = format_long_date(iso) if iso else "fecha no disponible"
        body_html = text_to_html_paragraphs(body_txt)
        fn = slugify_filename(slug) + ".html"
        path = OUT_DIR / fn
        canonical = f"/publicaciones/wix/{fn}"
        page = page_template(
            title=title,
            iso_date=iso or "1970-01-01T00:00:00.000Z",
            long_date=long_d,
            body_html=body_html,
            canonical_path=canonical,
        )
        path.write_text(page, encoding="utf-8")
        manifest.append(
            {
                "slug": slug,
                "file": fn,
                "title": title,
                "date": iso[:10] if iso else "",
                "wixUrl": wix_url,
                "rubro": SLUG_RUBRO[slug],
            }
        )
    (OUT_DIR / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    patch_publicaciones_rubros_section(manifest)
    patch_sitemap_wix_urls(manifest)
    print("Wrote", len(manifest), "files to", OUT_DIR)


def rebuild_publicaciones_index() -> None:
    """Regenera solo el bloque por rubros en publicaciones.html desde manifest.json (sin red Wix)."""
    assert_slug_rubro_coverage()
    path = OUT_DIR / "manifest.json"
    if not path.is_file():
        print("No existe publicaciones/wix/manifest.json.", file=sys.stderr)
        sys.exit(1)
    manifest = json.loads(path.read_text(encoding="utf-8"))
    for x in manifest:
        slug = x.get("slug")
        if slug and slug in SLUG_RUBRO:
            x["rubro"] = SLUG_RUBRO[slug]
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    patch_publicaciones_rubros_section(manifest)
    print("Actualizado índice por rubros en publicaciones.html y manifest.json")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--index-only":
        rebuild_publicaciones_index()
    else:
        main()
