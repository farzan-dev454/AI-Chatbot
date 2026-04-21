from dotenv import load_dotenv
import os
import requests
import datetime

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def chat(user_input):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {
                "role" : "user",
                "content": user_input
            }
        ],
        "temperature": 0.7
    }
    try:
        response = requests.post(GROQ_URL, headers=headers, json= data)
        result = response.json()
        return result ["choices"][0]["message"]["content"]
    except Exception as error:
        return f"Error: {str(error)}"