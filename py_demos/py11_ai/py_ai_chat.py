import time
import streamlit as st
from py_mod import st_print, st_code, ollama_model, ollama_model, ollama_URL, debug


### StartofFunc###

def pyopenai_chat():
    def openai_chat():
        from openai import OpenAI

        client = OpenAI()
        response = client.chat.completions.create(
            model='gpt-4o', messages=[{'role': 'user', 'content': 'Hello World!'}])
        st_print(f"response")

    def openai_api_chat():
        from openai._client import APIConfig

        class APIConfig:
            def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
                self.api_key = api_key
                self.model = model
                self.max_tokens = max_tokens
                self.base_url = "https://api.openai.com/v1"

        # Create different configurations
        # Using positional for required arg, named for optional
        dev_config = APIConfig("sk-dev-key", max_tokens=50)

        # Using all named arguments (clearest)
        prod_config = APIConfig(api_key="sk-prod-key",
                                model="gpt-4", max_tokens=1000)

        # Access the configuration
        st_print(dev_config.model)        # gpt-3.5-turbo
        st_print(prod_config.model)       # gpt-4
        st_print(prod_config.max_tokens)  # 1000
### EndofCodeSection###


def pyopenai_agent():
    def openai_agent():
        import os
        from dotenv import load_dotenv
        from langchain_openai import ChatOpenAI
        from langchain.agents import create_agent
        from langchain.tools import tool

        load_dotenv()

        llm = ChatOpenAI(                                              # step 1: create an llm object
            model="deepseek-chat",
            temperature=0.3,
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url="https://api.deepseek.com"
        )

        # Step 2: create tools with decrator
        @tool
        def calculator(expression: str) -> str:
            try:
                result = eval(expression)
                return f"calculation result: {result}"
            except Exception as e:
                return f"calculation error: {str(e)}"

        # Step 3: add tools to tool list
        tools = [calculator]

        agent = create_agent(                                          # Step 4: create an agent
            model=llm,
            tools=tools,
            system_prompt="You are an AI agent assistant, you can use calculation tools to answer calculation questions"
        )

        if __name__ == "__main__":
            question = "Please calculate 25 * 4 + 10 and tell what is the result? "
            print(f"user_question: {question}\n")
            result = agent.invole(                                      # Step 5: invoke the agent
                {"messages": [{"role": "user", "content": question}]}
            )
            print(f"\nthe final answer: {result['messages'][-1].contnent}")
### EndofCodeSection###


def py_ollama_chat():
    def ollama_chat():
        st_print(f"ollama_chat() {'-' * 30}")
        from ollama import chat, ChatResponse
        response: ChatResponse = chat(model=ollama_model, messages=[
                                      {"role": "user", "content": "hello, this is gongya"}])
        st_print(f"{response}")
        # also response.message.content. <- ccess fields directly from the response object
        st_print(response['message']['content'])

    def langchain_chat():
        st_print(f"langchain_chat() {'-' * 30}")
        from langchain_ollama import ChatOllama
        llm = ChatOllama(model=ollama_model, temperature=0)
        response = llm.invoke("hello, this is gongya")
        st_print(f"{response}")
        st_print(f"{response.content}")

    def langchain_agent_chat():
        st_print(f"langchain_agent_chat() {'-' * 30}")
        from langchain.agents import create_agent
        from langchain_ollama import ChatOllama
        model = ChatOllama(model=ollama_model, temperature=0)
        agent = create_agent(model=model, tools=[])

        response = agent.invoke(
            {"messages": [("user", "Explain quantum computing in simple words")]})
        st_print(f"{response}")
        st_print(f"{response["messages"][-1].content}")
    ollama_chat()
    langchain_chat()
    langchain_agent_chat()
### EndofCodeSection###


def py_stream_chat():
    from ollama import chat
    import streamlit as st
    st_print(f'py_stream_chat() {'-' * 30}')
    response = chat(model=ollama_model, messages=[
                    {"role": "user", "content": "hi, this is gongya"}], stream=True)

    def generate():
        for chunk in response:
            # st_print(f"{chunk['message']['content']}")
            # print(chunk["message"]["content"], end="", flush=True)                <-- for the cli
            yield chunk["message"]["content"]

    st.write_stream(generate)
### EndofCodeSection###


def pystart_ollama_daemon():
    import chainlit as cl

    def _ollama():
        import os
        import subprocess
        os.environ['OLLAMA_HOST'] = '0.0.0.0:11434'
        os.environ['OLLAMA_ORIGINS'] = '*'
        subprocess.popen(['ollama', 'serve'])

    def start_ollama():
        import threading
        thread = threading.thread(target=_ollama)
        thread.daemon = True
        thread.start()

    @cl.on_chat_start
    async def on_chat_start():
        import chainlit as cl
        start_ollama()
        cl.user_session.set('chat_history', [])
        cl.on_message("")
### EndofCodeSection###


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


def py_llama_chat():
    from llama_cpp import Llama
    # user_prompt = st.text_input("Enter your query:")
    start = time.time()
    # if user_prompt:
    model_path = "/Users/gongya/.ollama/models/blobs/sha256-e566218f2f25cfb315482a280283016bdb0c011f97e49cb327708c38fa075db5"
    llm = Llama(model_path=model_path, n_ctx=2048, verbose=False)
    response = llm.create_chat_completion(
        messages=[{"role": "user", "content": "This is hello from gongya."}], max_tokens=100000)
    st_print(response["choices"][0]["message"]["content"])
    end = time.time()
    st.write(f"Response time: {end - start} seconds")
    return response
### EndofCodeSection###


def py_local_API_chat():
    from openai import OpenAI
    user_prompt = st.text_input("Enter your query:")
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
