# config.py

# Diccionario con la configuración de la base de datos
DB_SETTINGS = {
    "database": "Movilidad",
    "user": "postgres",
    "password": "1234",  # ⚠️ Cuidado: No compartas contraseñas reales
    "host": "54.205.173.107",
    "port": "8081",
    # Agrega esta línea para fijar el esquema por defecto:
    "options": "-c search_path=\"IA__DBT\",public"
}