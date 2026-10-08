import time
import streamlit as st
from py_mod import st_print, st_code, ollama_model, ollama_model, ollama_URL, debug


### StartofFunc###

def py_nvidia_chat():
    llm_model = 'moonshotai/kimi-k3'
    user_prompt = "Where is Seattle located?"
    from openai import OpenAI
    from dotenv import load_dotenv
    import os

    load_dotenv()
    base_url = 'https://integrate.api.nvidia.com/v1/'
    api_key = os.getenv("NVIDIA_API_KEY")

    client = OpenAI(
        base_url = base_url,
        api_key = api_key
    )
    response = client.chat.completions.create(
        model=llm_model,
        messages=[
            {"role": "user", "content": user_prompt}
        ]
    )
    #return response.choices[0].message.content
    st_print(f"response: {response.choices[0].message.content}")
### EndofCodeSection###

def nvidia_request_chat(llm_model, user_prompt, debug) -> str:
    from dotenv import load_dotenv
    import requests
    import os
    import json

    API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
    load_dotenv()
    api_key = os.getenv("NVIDIA_API_KEY")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    body = {
        "model": llm_model,
        "messages": [{"role": "user", "content": user_prompt}],
        "max_tokens": 2048,
        "stream": True,
        "temperature": 1.0,
    }
    #print(f"API_URL: {API_URL}")
    #print(f"llm_mosel: {llm_model}")
    #print(f"api_key is not None: {api_key is not None}")
    
    #resp = requests.post(API_URL, headers=headers, json=body, stream=True)
    resp = requests.post(API_URL, headers=headers, json=body)
    # print(resp.text)

    #print(f"resp.raise_for_status(): {resp.raise_for_status()}")
    #print(f"resp.text: {resp.text}")
    response = ''
    for line in resp.iter_lines():
        if not line or not line.startswith(b"data: "):
            continue
        data = line[6:]
        if data == b"[DONE]":
            break
        chunk = json.loads(data)
        if chunk["choices"]:
            delta = chunk["choices"][0].get("delta", {})
            if "content" in delta:
                #print(delta["content"], end="", flush=True)
                response += delta["content"]
    #return response
    st_print(f"response: {response}")
### EndofCodeSection###