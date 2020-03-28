from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
async def root():
    return "Hello world, from Alice."


@app.get("/health")
async def health():
    return {"status": "UP"}


@app.get("/call-bob")
def call_bob():
    r = requests.get('http://sidecar-alice:5678/hosts/bob')
    uri = r.json()[0]['uri']
    r = requests.get(uri)
    return r.text + ' Through Alice.'
