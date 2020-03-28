from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import requests

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
async def root():
    return "Hello world, from Alice."


@app.get("/health")
async def health():
    return {"status": "UP"}


@app.get("/call-bob", response_class=PlainTextResponse)
def call_bob():
    r = requests.get('http://sidecar-alice:5678/hosts/bob')
    json = r.json()
    if len(json) == 0:
        return 'Service bob is not available yet.'
    uri = json[0]['uri']
    nr = requests.get(uri)
    return nr.text + ' Through Alice.'
