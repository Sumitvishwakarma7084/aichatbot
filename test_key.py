import google.generativeai as genai

# Set your Gemini API Key
genai.configure(api_key="AIzaSyAEkcyV4eUHePK8JucoGaF86DMDNw1zKoo")

try:
    # Check available models
    models = genai.list_models()
    print("✅ Available models:")
    for m in models:
        print("-", m.name, m.supported_generation_methods)
except Exception as e:
    print("❌ ERROR:", e)
