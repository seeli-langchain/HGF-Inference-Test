from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()
HF_API_KEY = os.environ.get('HF_API_KEY')

client = InferenceClient(model="meta-llama/Llama-2-70b-chat-hf", token=HF_API_KEY)

prompt = """<s>[INST] <<SYS>>
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.
<</SYS>>

There's a llama in my garden 😱 What should I do? [/INST]
"""

response = client.text_generation(prompt, max_new_tokens=200)
print(response)


