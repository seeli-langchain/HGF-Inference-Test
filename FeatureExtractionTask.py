import json
from dotenv import load_dotenv
import requests
import os


load_dotenv()
HF_API_KEY = os.environ.get('HF_API_KEY')
MODEL = "sentence-transformers/paraphrase-xlm-r-multilingual-v1"
API_URL = "https://api-inference.huggingface.co/models/" + MODEL

headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
data = query({"inputs": ["The answer to the universe is 42.", "42 is the answer to the universe."]})
print(data)