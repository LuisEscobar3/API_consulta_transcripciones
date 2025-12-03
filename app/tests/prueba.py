# test_consulta.py
import psycopg2
import json
from psycopg2.extras import RealDictCursor

# Coloca aquí la misma configuración de tu archivo config.py
DB_SETTINGS = {
    "database": "danos_bienes_terceros_rf",
    "user": "admin_user",
    "password": "Claro.3310",
    "host": "localhost",
    "port": "5432"
}

# --- DATOS PARA LA CONSULTA ---
CASO_ID_A_BUSCAR = "10100088546"
USUARIO_ID_A_BUSCAR = "alexander.ramirez.gutierrez@segurosbolivar.com"

def ejecutar_consulta_directa():
    """
    Se conecta a la BD y ejecuta la consulta de transcripciones con los filtros.
    """
    conn = None
    print("🚀 Iniciando prueba de consulta directa...")

    try:
        # 1. Conectar a la base de datos
        conn = psycopg2.connect(**DB_SETTINGS)
        print("✅ Conexión exitosa.")

        # 2. Construir la consulta SQL (misma lógica que en crud.py)
        query = "SELECT id, caso_id, usuario_id, texto_transcripcion, fecha_creacion FROM transcripciones_simples WHERE caso_id = %s AND usuario_id = %s"
        params = (CASO_ID_A_BUSCAR, USUARIO_ID_A_BUSCAR)

        print(f"\n📄 Ejecutando SQL:\n{query}")
        print(f"🔩 Con parámetros: {params}\n")

        # 3. Ejecutar la consulta
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, params)
            resultados = cur.fetchall()

        # 4. Mostrar los resultados
        if not resultados:
            print("❌ No se encontraron registros con los datos proporcionados.")
        else:
            print("🎉 ¡Registros encontrados!")
            # Usamos json.dumps para imprimir el resultado de forma legible (pretty-print)
            print(json.dumps(resultados, indent=4, default=str))

    except psycopg2.OperationalError as e:
        print(f"🔥 Error de conexión: {e}")
    except Exception as e:
        print(f"🔥 Ocurrió un error inesperado: {e}")
    finally:
        if conn:
            conn.close()
            print("\n🔌 Conexión cerrada.")

# --- Punto de entrada para ejecutar el script ---
if __name__ == "__main__":
    ejecutar_consulta_directa()