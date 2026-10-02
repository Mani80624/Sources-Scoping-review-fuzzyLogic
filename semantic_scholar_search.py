"""
Búsqueda en Semantic Scholar (Graph API) para revisión PRISMA-ScR
Fuzzy logic / ANFIS aplicado a mamografía y clasificación BI-RADS

Requiere: pip install requests pandas

Notas sobre la sintaxis de búsqueda de Semantic Scholar:
- Espacio entre términos = AND implícito
- "|" = OR
- "" (comillas) = frase exacta
- () = agrupación
- API pública sin key: límite ~100 requests / 5 min (compartido entre todos
  los usuarios sin key). Si tienes muchos resultados, corre el script con
  pausas o solicita una API key gratuita en:
  https://www.semanticscholar.org/product/api#api-key-form
"""

import requests
import pandas as pd
import time
import re
import sys

# =========================================================
# CONFIGURACIÓN
# =========================================================

API_KEY = None  # Opcional: pega aquí tu key si la solicitaste
BASE_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

# Ecuación adaptada a la sintaxis de Semantic Scholar
QUERY = (
    '("fuzzy logic" | "fuzzy system" | "fuzzy inference system" | '
    '"fuzzy classifier" | ANFIS | "adaptive neuro-fuzzy inference system" | '
    '"neuro-fuzzy" | Mamdani | Sugeno) '
    '("breast cancer" | mammography | mammogram | "BI-RADS" | '
    '"breast mass" | "breast imaging")'
)

# Rango de año, consistente con lo definido para las otras 3 bases
YEAR_RANGE = "2010-2027"

# Campos a recuperar (equivalentes a lo que usamos en el CSV de Rayyan)
FIELDS = (
    "title,authors,year,venue,externalIds,abstract,url,"
    "publicationTypes,journal"
)

LIMIT_POR_PAGINA = 100  # máximo permitido por la API
PAUSA_ENTRE_REQUESTS = 3.5  # segundos; sube esto si te da error 429

OUTPUT_CSV = r"semantic_scholar_resultados.csv"


# =========================================================
# FUNCIONES
# =========================================================

def buscar_semantic_scholar(query, year_range, fields, limit=100):
    """Pagina sobre /paper/search hasta agotar resultados o llegar al tope de la API."""
    headers = {}
    if API_KEY:
        headers["x-api-key"] = API_KEY

    resultados = []
    offset = 0
    total_esperado = None

    while True:
        params = {
            "query": query,
            "year": year_range,
            "fields": fields,
            "limit": limit,
            "offset": offset,
        }

        resp = requests.get(BASE_URL, params=params, headers=headers)

        if resp.status_code == 429:
            print("Rate limit alcanzado. Esperando 30s antes de reintentar...")
            time.sleep(30)
            continue

        if resp.status_code != 200:
            print(f"Error {resp.status_code}: {resp.text[:300]}")
            break

        data = resp.json()
        total_esperado = data.get("total", 0)
        page = data.get("data", [])

        if not page:
            break

        resultados.extend(page)
        offset += len(page)

        print(f"  Recuperados {offset} / {total_esperado}")

        # Semantic Scholar limita el offset máximo navegable (~1000-10000
        # según endpoint); si total_esperado es muy grande, considera
        # acotar la búsqueda (p. ej. por rango de año más pequeño).
        if offset >= total_esperado or offset >= 9998:
            break

        time.sleep(PAUSA_ENTRE_REQUESTS)

    return resultados, total_esperado


def normaliza_doi(doi):
    if not doi:
        return None
    doi = str(doi).lower().strip()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi)
    return doi


def normaliza_titulo(t):
    if not t:
        return None
    t = str(t).lower().strip()
    t = re.sub(r"[^\w\s]", "", t)
    t = re.sub(r"\s+", " ", t)
    return t


def construir_dataframe(resultados):
    filas = []
    for r in resultados:
        authors = "; ".join(a.get("name", "") for a in (r.get("authors") or []))
        ext_ids = r.get("externalIds") or {}
        doi = ext_ids.get("DOI")
        journal_info = r.get("journal") or {}

        filas.append({
            "title": r.get("title") or "",
            "authors": authors,
            "journal": r.get("venue") or journal_info.get("name") or "",
            "year": r.get("year"),
            "volume": journal_info.get("volume") or "",
            "issue": "",
            "pages": journal_info.get("pages") or "",
            "doi": doi or "",
            "issn": "",
            "abstract": r.get("abstract") or "",
            "url": r.get("url") or "",
            "publication_types": ", ".join(r.get("publicationTypes") or []),
            "source_database": "Semantic Scholar",
        })

    df = pd.DataFrame(filas)
    df["doi_norm"] = df["doi"].apply(normaliza_doi)
    df["titulo_norm"] = df["title"].apply(normaliza_titulo)
    return df


def deduplicar(df):
    total_bruto = len(df)

    con_doi = df[df["doi_norm"].notna()].copy()
    sin_doi = df[df["doi_norm"].isna()].copy()

    antes = len(con_doi)
    con_doi = con_doi.drop_duplicates(subset="doi_norm", keep="first")
    dup_doi = antes - len(con_doi)

    antes = len(sin_doi)
    sin_doi = sin_doi.drop_duplicates(subset="titulo_norm", keep="first")
    dup_titulo = antes - len(sin_doi)

    df_final = pd.concat([con_doi, sin_doi], ignore_index=True)
    antes = len(df_final)
    df_final = df_final.drop_duplicates(subset="titulo_norm", keep="first")
    dup_cruzado = antes - len(df_final)

    print(f"\n--- Deduplicación interna Semantic Scholar ---")
    print(f"Total bruto: {total_bruto}")
    print(f"Duplicados por DOI: {dup_doi}")
    print(f"Duplicados por título (sin DOI): {dup_titulo}")
    print(f"Duplicados cruzados adicionales: {dup_cruzado}")
    print(f"Total único: {len(df_final)}")

    return df_final


# =========================================================
# EJECUCIÓN
# =========================================================

if __name__ == "__main__":
    print("Consultando Semantic Scholar...")
    print(f"Query: {QUERY}")
    print(f"Rango de año: {YEAR_RANGE}\n")

    resultados, total = buscar_semantic_scholar(
        QUERY, YEAR_RANGE, FIELDS, limit=LIMIT_POR_PAGINA
    )

    if not resultados:
        print("No se obtuvieron resultados. Revisa la query o el rate limit.")
        sys.exit(1)

    print(f"\nTotal reportado por la API: {total}")
    print(f"Total recuperado: {len(resultados)}")

    df = construir_dataframe(resultados)
    df_final = deduplicar(df)

    # Generar key y limpiar columnas auxiliares, mismo esquema que el CSV
    # ya usado para ScienceDirect + IEEE + PubMed en Rayyan
    df_final = df_final.reset_index(drop=True)
    df_final.insert(0, "key", df_final.index + 1)
    df_final = df_final.drop(columns=["doi_norm", "titulo_norm"])

    cols_rayyan = [
        "key", "title", "authors", "journal", "year", "volume", "issue",
        "pages", "doi", "issn", "abstract", "url", "publication_types",
        "source_database",
    ]
    df_final = df_final[cols_rayyan]

    df_final.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")
    print(f"\nArchivo guardado en: {OUTPUT_CSV}")