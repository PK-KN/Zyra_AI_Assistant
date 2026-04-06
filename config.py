import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file
load_dotenv()

# Get API key safely
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ API key not found. Check your .env file.")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")
