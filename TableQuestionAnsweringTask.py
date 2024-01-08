import json
from dotenv import load_dotenv
import requests
import os


load_dotenv()
HF_API_KEY = os.environ.get('HF_API_KEY')
MODEL = "google/tapas-base-finetuned-wtq"
API_URL = "https://api-inference.huggingface.co/models/" + MODEL

headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
data = query(
    {
        "inputs": {
            "query": "How many stars does the transformers repository have?",
            "table": {
                "Repository": ["Transformers", "Datasets", "Tokenizers"],
                "Stars": ["36542", "4512", "3934"],
                "Contributors": ["651", "77", "34"],
                "Programming language": [
                    "Python",
                    "Python",
                    "Rust, Python and NodeJS",
                ],
            },
        }
    }
)
print(data)