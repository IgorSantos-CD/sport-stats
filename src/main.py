from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Ambiente funcionando!"}

@app.get("/health")
async def health():
    return {"status" : "ok"}