import time
import streamlit as st
from py_mod import st_print, st_code, ollama_model, ollama_model, ollama_URL, debug

### StartofFunc###

def py_aiohttp():
    import asyncio
    import aiohttp
    import time

    SEMAPHONE = asyncio.Semaphore(3)
    URL = "http://localhost:11434/api/chat"

    async def async_llm_chat(session: aiohttp.ClientSession, prompt):
        async with SEMAPHONE:
            payload = {
                "model": "llama3.2:latest",
                "messages": [{"role": "user", "content": prompt}],
                "stream": False,
                # "done":True
            }
            async with session.post(URL, json=payload) as resp:
                st_print(f"HTTP status:  {resp.status}")
                result = await resp.json()
                st_print(f"{result}")
                return result.get("message", {}).get("content", "no response from LLM!")

    async def pymain():
        start = time.time()
        async with aiohttp.ClientSession() as session:
            # prompts = [f"A simple introduction for python async {i}" for i in range(5)]
            prompts = ['Say hello in one sentence', 'what date is it today',
                       'List 2 airlines available in Seatac airport', 'write a hello world python script for me']
            tasks = [async_llm_chat(session, p) for p in prompts]
            results = await asyncio.gather(*tasks, return_exceptions=True)
        for idx, res in enumerate(results):
            # st_print(f"Task {idx}: {res[:30]}...")
            st_print(f"Task {idx}: {res}...")
        end = time.time()
        st_print(f"All queries cost {end-start:.2f} seconds.")

    asyncio.run(pymain())
### EndofCodeSection###

def py_aiohttp_chat():
    import asyncio
    import aiohttp

    async def chat(prompt: str) -> str:
        payload = {
            "model": ollama_model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(ollama_URL, json=payload) as resp:
                result = await resp.json()
                if debug == True:
                    return result
                return result.get("message", {}).get("content", "no response")
    st_print(asyncio.run(chat("how are you today")))
### EndofCodeSection###