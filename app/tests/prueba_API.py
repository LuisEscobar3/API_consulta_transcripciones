# cliente_api.py
import requests
import json
from typing import Optional, List, Dict

# URL base donde tu API está corriendo
BASE_URL = "http://127.0.0.1:8000"


def consultar_transcripciones(
        caso_id: Optional[str] = None,
        usuario_id: Optional[str] = None
) -> Optional[List[Dict]]:
    """
    Llama al endpoint /transcripciones/ de la API con filtros opcionales.

    Args:
        caso_id: El ID del caso a filtrar.
        usuario_id: El ID del usuario a filtrar.

    Returns:
        Una lista de diccionarios con las transcripciones o None si hay un error.
    """
    endpoint = f"{BASE_URL}/transcripciones/"
    params = {}

    # Construye el diccionario de parámetros solo con los valores que no son None
    if caso_id:
        params["caso_id"] = caso_id
    if usuario_id:
        params["usuario_id"] = usuario_id

    print(f"▶️  Consultando endpoint: {endpoint} con parámetros: {params}")

    try:
        # Realiza la petición GET a la API
        response = requests.get(endpoint, params=params)

        # Verifica si la petición fue exitosa (código 200 OK)
        if response.status_code == 200:
            print("✅ ¡Consulta exitosa!")
            # Devuelve el contenido de la respuesta en formato JSON
            return response.json()

        # Maneja errores comunes como "No encontrado"
        elif response.status_code == 404:
            print("🟡 No se encontraron registros para los filtros proporcionados.")
            return []

        # Maneja otros errores del servidor
        else:
            print(f"❌ Error en la API. Código de estado: {response.status_code}")
            print(f"   Respuesta: {response.text}")
            return None

    except requests.exceptions.ConnectionError as e:
        print(f"🔥 Error de conexión: No se pudo conectar a la API en {BASE_URL}.")
        print("   Asegúrate de que el servidor FastAPI (uvicorn) esté corriendo.")
        return None
    except Exception as e:
        print(f"🔥 Ocurrió un error inesperado: {e}")
        return None


def imprimir_resultado(resultado: Optional[List[Dict]]):
    """Función auxiliar para imprimir los resultados de forma legible."""
    if resultado is not None:
        # Usa json.dumps para un "pretty print"
        # AÑADE ensure_ascii=False para mostrar tildes y caracteres especiales
        print(json.dumps(resultado, indent=4, ensure_ascii=False, default=str))
    print("-" * 40)


# --- PUNTO DE ENTRADA PARA EJECUTAR EL SCRIPT ---
if __name__ == "__main__":
    print("🚀 Iniciando cliente de API...")
    print("=" * 40)

    # --- EJEMPLO 1: Consultar con los datos que proporcionaste ---
    print("Ejemplo 1: Buscando por caso_id y usuario_id")
    datos_especificos = consultar_transcripciones(
        caso_id="15050073916",
        usuario_id="alexander.ramirez.gutierrez@segurosbolivar.com"
    )
    imprimir_resultado(datos_especificos)


