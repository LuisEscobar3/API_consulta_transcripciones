# run.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.services.main:app", # Ruta corregida a la app FastAPI
        host="0.0.0.0",          # Necesario para que sea accesible desde fuera del contenedor
        port=8000,
        reload=True
    )