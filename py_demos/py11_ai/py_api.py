import time
import streamlit as st
from py_mod import st_print, st_code, ollama_model, ollama_model, ollama_URL, debug

### StartofFunc###

def py_local_API_chat():
    from openai import OpenAI
    user_prompt = "Where is Seattle located?"
    # Replace with your Ollama API key if needed
    start = time.time()
    if user_prompt:
        client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
        response = client.chat.completions.create(
            model=ollama_model,
            messages=[{"role": "user", "content": user_prompt}],
            stream=False
        )
        if debug == 'Yes':
            st.code(response)
            return response
        st.code(response.choices[0].message.content)
        end = time.time()
        st.write(f"Response time: {end - start} seconds")
        return response.choices[0].message.content
### EndofCodeSection###