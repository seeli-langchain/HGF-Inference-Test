import json
from dotenv import load_dotenv
import requests
import os


load_dotenv()
HF_API_KEY = os.environ.get('HF_API_KEY')
MODEL = "facebook/bart-large-mnli"
API_URL = "https://api-inference.huggingface.co/models/" + MODEL

headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
data = query(
    {
        "inputs": "Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!",
        "parameters": {"candidate_labels": ["refund", "legal", "faq"]},
    }
)
print(data)