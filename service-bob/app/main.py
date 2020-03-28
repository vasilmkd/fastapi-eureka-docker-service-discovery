from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import requests

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
async def root():
    return "Hello world, from Bob."


@app.get("/health")
async def health():
    return {"status": "UP"}


@app.get("/call-alice", response_class=PlainTextResponse)
def call_alice():
    r = requests.get('http://sidecar-bob:5678/hosts/alice')
    json = r.json()
    if len(json) == 0:
        return 'Service alice is not available yet.'
    uri = json[0]['uri']
    nr = requests.get(uri)
    return nr.text + ' Through Bob.'
