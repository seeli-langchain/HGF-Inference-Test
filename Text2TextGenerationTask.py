import json
from dotenv import load_dotenv
import requests
import os


load_dotenv()
HF_API_KEY = os.environ.get('HF_API_KEY')
MODEL = "dbmdz/bert-large-cased-finetuned-conll03-english"
API_URL = "https://api-inference.huggingface.co/models/" + MODEL

headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
data = query({"inputs": "My name is Sarah Jessica Parker but you can call me Jessica"})
print(data)