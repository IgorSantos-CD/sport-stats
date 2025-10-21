from fastapi import FastAPI
from src.api.routes import routes_health


app = FastAPI(title="Sport-Stats API")

app.include_router(routes_health.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Ambiente funcionando!"}

@app.get("/health")
async def health():
    return {"status" : "ok"}