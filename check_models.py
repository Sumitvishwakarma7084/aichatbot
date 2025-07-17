import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

models = genai.list_models()

print("\nAvailable models and their supported generation methods:\n")
for model in models:
    print(f"Model: {model.name}")
    print(f"  Generation methods: {model.supported_generation_methods}")
    print()
