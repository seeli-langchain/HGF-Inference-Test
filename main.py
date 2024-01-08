import json
from dotenv import load_dotenv
import requests
import os


load_dotenv()
HF_API_KEY = os.environ.get('HF_API_KEY')

from huggingface_hub import InferenceClient

client = InferenceClient(model="meta-llama/Llama-2-70b-chat-hf", token=HF_API_KEY)

output = client.text_generation("Can you please let us know more details about your new lowcode platform? ")
print(output)
