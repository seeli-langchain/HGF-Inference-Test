import json
from dotenv import load_dotenv
import requests
import os


load_dotenv()
HF_API_KEY = os.environ.get('HF_API_KEY')
MODEL = "sentence-transformers/all-MiniLM-L6-v2"
API_URL = "https://api-inference.huggingface.co/models/" + MODEL

headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
data = query(
    {
        "inputs": {
            "source_sentence": "That is a happy person",
            "sentences": ["That is a happy dog", "That is a very happy person", "Today is a sunny day"],
        }
    }
)
print(data)