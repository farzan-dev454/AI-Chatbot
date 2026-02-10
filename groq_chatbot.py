import streamlit as st
import requests
import os
import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Groq API endpoint
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def chat(user_message):
    """Send message to Groq and get response"""
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama-3.1-8b-instant",  # Fast and free model
        "messages": [
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.7,
        "max_tokens": 1024
    }
    
    try:
        response = requests.post(GROQ_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        
        # Extract the response
        return result['choices'][0]['message']['content']
    
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("🤖 AI Chatbot")
st.write("Powered by Groq (Llama 3)")

# Sidebar for controls
with st.sidebar:
    st.header("⚙️ Controls")
    
    # Button to view history
    if st.button("📜 View Full History"):
        st.session_state.show_history = True
    
    # Button to clear history
    if st.button("🗑️ Clear History"):
        st.session_state.messages = []
        st.rerun()
    
    # Button to download history
    if st.button("💾 Download History"):
        if "messages" in st.session_state and st.session_state.messages:
            # Create text file content
            history_text = ""
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            history_text += f"Conversation History - {timestamp}\n"
            history_text += "="*50 + "\n\n"
            
            for msg in st.session_state.messages:
                role = "You" if msg["role"] == "user" else "Bot"
                history_text += f"{role}: {msg['content']}\n\n"
            
            # Create download button
            st.download_button(
                label="📥 Download as TXT",
                data=history_text,
                file_name=f"chat_history_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )
        else:
            st.info("No conversation history yet!")
    
    # Show message count
    if "messages" in st.session_state:
        total_messages = len(st.session_state.messages)
        user_messages = len([m for m in st.session_state.messages if m["role"] == "user"])
        bot_messages = len([m for m in st.session_state.messages if m["role"] == "assistant"])
        
        st.markdown("---")
        st.markdown("📊 **Statistics:**")
        st.markdown(f"- Total messages: {total_messages}")
        st.markdown(f"- Your messages: {user_messages}")
        st.markdown(f"- Bot responses: {bot_messages}")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize history view state
if "show_history" not in st.session_state:
    st.session_state.show_history = False

# Show full history if button was clicked
if st.session_state.show_history:
    st.markdown("---")
    st.subheader("📜 Full Conversation History")
    
    if st.session_state.messages:
        for i, message in enumerate(st.session_state.messages, 1):
            role = "🧑 You" if message["role"] == "user" else "🤖 Bot"
            with st.expander(f"Message {i}: {role}", expanded=False):
                st.write(message["content"])
    else:
        st.info("No conversation history yet!")
    
    # Button to close history view
    if st.button("❌ Close History View"):
        st.session_state.show_history = False
        st.rerun()
    
    st.markdown("---")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat(prompt)
            st.write(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})