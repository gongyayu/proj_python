import streamlit as st
from py_mod import st_print, st_code, ollama_model, ollama_model, ollama_URL, debug
from dotenv import load_dotenv

load_dotenv()

### StartofFunc###
def py_gemini_chat():  
    from google import genai
    from google.genai import types

    # Initialize the client (automatically uses GEMINI_API_KEY environment variable)
    client = genai.Client()

    # Initialize a chat session with system instructions
    chat = client.chats.create(
        model="gemini-3.6-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are a helpful, friendly AI assistant. Keep responses brief.",
            temperature=0.7,
        )
    )
    user_input = "Where is Seattle located?"
    # Send message and receive response
    response = chat.send_message(user_input)

    st_print(f"Bot: {response.text}\n")
### EndofCodeSection###