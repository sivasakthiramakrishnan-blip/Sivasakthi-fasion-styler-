import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

def generate_image(prompt, filename, save_dir):
    print(f"Generating image for: {prompt}")
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    print(f"Response status: {response.status_code}")
    if response.status_code == 200:
        os.makedirs(save_dir, exist_ok=True)
        filepath = os.path.join(save_dir, filename)
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"Image saved to {filepath}")
        return filepath
    else:
        print(f"Error: {response.text}")
        return "Error generating image"