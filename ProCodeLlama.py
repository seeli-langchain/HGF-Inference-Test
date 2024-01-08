from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()
HF_API_KEY = os.environ.get('HF_API_KEY')
client = InferenceClient(model="codellama/CodeLlama-13b-hf", token=HF_API_KEY)

prompt_prefix = 'def remove_non_ascii(s: str) -> str:\n    """ '
prompt_suffix = "\n    return result"

prompt = f"<PRE> {prompt_prefix} <SUF>{prompt_suffix} <MID>"

infilled = client.text_generation(prompt, max_new_tokens=150)
infilled = infilled.rstrip(" <EOT>")
print(f"{prompt_prefix}{infilled}{prompt_suffix}")