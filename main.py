# ✅ STEP 1: Load environment variables & configure Gemini
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()  # This loads the .env file
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ✅ STEP 2: Import FastAPI and setup app
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# ✅ STEP 3: Setup your model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# ✅ STEP 4: FastAPI app setup
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(message: str = Form(...)):
    try:
        if not message.strip():
            return JSONResponse(content={"response": "Please enter a valid message."})

        response = model.generate_content({"parts": [{"text": message}]})

        if hasattr(response, 'text') and response.text:
            return JSONResponse(content={"response": response.text})
        elif response.candidates:
            return JSONResponse(content={"response": response.candidates[0].content})
        else:
            return JSONResponse(content={"response": "No response from Gemini."})
    except Exception as e:
        return JSONResponse(content={"response": f"Error: {str(e)}"}, status_code=500)

# ✅ STEP 5: Run the server
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
