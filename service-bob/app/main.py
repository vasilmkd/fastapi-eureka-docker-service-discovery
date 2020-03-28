from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
async def root():
    return "Hello world, from Bob."


@app.get("/health")
async def health():
    return {"status": "UP"}


@app.get("/call-alice")
def call_alice():
    r = requests.get('http://sidecar-bob:5678/hosts/alice')
    json = r.json()
    uri = json[0]['uri']
    print(json)
    print(uri)
    nr = requests.get(uri)
    return nr.text + ' Through Bob.'
