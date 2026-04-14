from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Allow your website to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load fee
def get_fee():
    with open("fee.json") as f:
        return json.load(f)

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/fee")
def fee():
    return get_fee()
