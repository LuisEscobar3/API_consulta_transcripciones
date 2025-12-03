# database.py
import psycopg2
from psycopg2 import OperationalError
from fastapi import HTTPException
from config import DB_SETTINGS

def get_db_connection():
    """
    Crea y gestiona una conexión a la BD para cada petición.
    Esta es una 'dependencia' de FastAPI.
    """
    conn = None
    try:
        conn = psycopg2.connect(**DB_SETTINGS)
        yield conn
    except OperationalError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error de conexión a la base de datos: {e}"
        )
    finally:
        if conn:
            conn.close()