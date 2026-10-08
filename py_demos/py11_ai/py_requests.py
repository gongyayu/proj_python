import time
import streamlit as st
from py_mod import st_print, st_code, ollama_model, ollama_model, ollama_URL, debug

### StartofFunc###

def py_requests_chat():
    import json
    import requests

    def chat(prompt: str) -> str:
        payload = {
            "model": ollama_model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
        }
        response = requests.post(ollama_URL, json=payload)
        if debug == True:
            return response.json().get("message")
        return response.json().get("message", {}).get("content", "no response")
    st_print(chat("how are you today?"))
### EndofCodeSection###