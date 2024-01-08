from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os


load_dotenv()
HF_API_KEY = os.environ.get('HF_API_KEY')

sdxl = InferenceClient(model="stabilityai/stable-diffusion-xl-base-1.0", token=HF_API_KEY)
image = sdxl.text_to_image(
    "Sunny day at the beach. A beautiful woman is walking towards you. She is smiling at you. She is wearing a bikini.",
    guidance_scale=9,
)
image.save("test.png")

