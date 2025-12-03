# crud.py
import psycopg2
from psycopg2.extras import RealDictCursor
from typing import List, Optional


def get_transcripciones(
        conn: psycopg2.extensions.connection,
        caso_id: Optional[str],
        usuario_id: Optional[str]
) -> List[dict]:
    """
    Ejecuta la consulta SQL para obtener las transcripciones
    y devuelve los resultados.
    """
    query = """
        SELECT 
            id, 
            caso_id, 
            usuario_id, 
            texto_transcripcion, 
            fecha_creacion::timestamp  -- Corrección para Pydantic
        FROM "IA__DBT".transcripciones_simples -- Corrección del esquema
    """
    filters = []
    params = []

    if caso_id:
        filters.append("caso_id = %s")
        params.append(caso_id)

    if usuario_id:
        filters.append("usuario_id = %s")
        params.append(usuario_id)

    if filters:
        query += " WHERE " + " AND ".join(filters)

    # Usamos RealDictCursor para obtener los resultados como diccionarios
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(query, tuple(params))
        resultados = cur.fetchall()

    return resultados
