import socket

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
class Operands(BaseModel):
    a: float
    b: float

@app.get("/")
def read_root():
    return {"message": "it works !"}

@app.post("/multiply")
def multiply(op: Operands):
    return {"result a*b=": op.a * op.b}
@app.post("/divide")
def divide(op: Operands):
    if op.b == 0:
        raise HTTPException(status_code=400, detail="Division par zéro impossible")
    return {"result a/b=": op.a / op.b}
@app.get("/greeting")
def greeting(name: str):
    hostname = socket.gethostname()
    # Récupération basique de l'IP locale connectée
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()

    return {
        "message": f"Hello, {name}",
        "developer": "Dev2",
        "hostname": hostname,
        "IP": IP
    }

@app.get("/addition")
def addition(a: float, b: float):
    return {"result a+b=": a + b, "developer": "Dev1"}

