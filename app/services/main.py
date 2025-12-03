# main.py

# ...otros imports de tu aplicación como Routers, etc.

# --- ESTA ES LA LÍNEA QUE DEBES AÑADIR ---
# Asegúrate de que se ejecute antes de crear la app de FastAPI
load_dotenv(encoding='utf-8')
# AHORA
import psycopg2
import app.functions.crud
from database import get_db_connection
from app.models import schemas
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException
from typing import List, Optional

app = FastAPI(
    title="API de Transcripciones (Modular)",
    description="Una API modular para consultar transcripciones.",
    version="2.0"
)

@app.get("/transcripciones/", response_model=List[schemas.TranscripcionSimpleSchema])
def obtener_transcripciones_endpoint(
    caso_id: Optional[str] = None,
    usuario_id: Optional[str] = None,
    conn: psycopg2.extensions.connection = Depends(get_db_connection)
):
    """
    Endpoint para obtener una lista de transcripciones, con filtros opcionales.
    """
    # Llama a la función de lógica de negocio en el módulo crud
    transcripciones = crud.get_transcripciones(
        conn=conn,
        caso_id=caso_id,
        usuario_id=usuario_id
    )

    if not transcripciones:
        raise HTTPException(
            status_code=404,
            detail="No se encontraron transcripciones con los filtros proporcionados."
        )

    return transcripciones