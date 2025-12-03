# schemas.py
from pydantic import BaseModel
import datetime
from typing import Optional

class TranscripcionSimpleSchema(BaseModel):
    id: int
    caso_id: str
    usuario_id: str
    texto_transcripcion: Optional[str] = None
    fecha_creacion: datetime.datetime

    # Configuración para compatibilidad con objetos de la base de datos
    class Config:
        from_attributes = True