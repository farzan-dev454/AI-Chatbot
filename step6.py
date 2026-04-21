import requests
import os
import datetime
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

def send_message(user_message,memory):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": memory + [{"role": "user", "content": user_message}],
        "temperature": 0.9
    }
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    return result['choices'][0]['message']['content']

# Simple chat loop
print("Chatbot started! Type 'quit' to exit.\n")

bot_memory = []
message_count = 0
while True:
    user_input = input("You: ")
    
    if user_input.strip() == "":
        print("Please enter a valid message.")
        continue
    
    message_count += 1
    print(f"Message count: {message_count}")
    
    if user_input.lower() in ["quit", "exit", "bye", "goodbye"]:
        print("Goodbye!")
        break
    
    bot_response = send_message(user_input, bot_memory)
    print(f"Bot: {bot_response}\n")
    bot_memory.append({"role": "user", "content": user_input})
    bot_memory.append({"role": "assistant", "content": bot_response})
    with open("chat_log.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        file.write(f"[{timestamp}] User: {user_input}\n")
        file.write(f"[{timestamp}] Bot: {bot_response}\n\n")