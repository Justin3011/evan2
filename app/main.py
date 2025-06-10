from fastapi import FastAPI
import requests

app = FastAPI()

DOLAR_API_URL = "https://dolarapi.com/v1/dolares"
EURO_API_URL = "https://dolarapi.com/v1/euros"

@app.get("/status")
def status():
    return {"status": "Servicio funcionando correctamente"}

@app.get("/dolar")
def get_dolar():
    response = requests.get(DOLAR_API_URL)
    data = response.json()[0]
    return {
        "nombre": data["nombre"],
        "compra": round(data["compra"], 2),
        "venta": round(data["venta"], 2),
        "fecha": data["fecha"]
    }

@app.get("/euro")
def get_euro():
    response = requests.get(EURO_API_URL)
    data = response.json()[0]
    return {
        "nombre": data["nombre"],
        "compra": round(data["compra"], 2),
        "venta": round(data["venta"], 2),
        "fecha": data["fecha"]
    }
