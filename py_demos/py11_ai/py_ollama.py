import time
import streamlit as st
from py_mod import st_print, st_code, ollama_model, ollama_model, ollama_URL, debug


### StartofFunc###

def py_ollama_chat():
    def ollama_chat():
        from ollama import chat, ChatResponse
        response: ChatResponse = chat(model=ollama_model, messages=[
                                      {"role": "user", "content": "Where is Seattle located"}])
        st_print(f"{response}")
        # also response.message.content. <- ccess fields directly from the response object
        st_print(response['message']['content'])

    def langchain_chat():
        st_print(f"langchain_chat() {'-' * 30}")
        from langchain_ollama import ChatOllama
        llm = ChatOllama(model=ollama_model, temperature=0)
        response = llm.invoke("Where is Bellevue located?")
        st_print(f"{response}")
        st_print(f"{response.content}")

    def langchain_agent_chat():
        st_print(f"langchain_agent_chat() {'-' * 30}")
        from langchain.agents import create_agent
        from langchain_ollama import ChatOllama
        model = ChatOllama(model=ollama_model, temperature=0)
        agent = create_agent(model=model, tools=[])

        response = agent.invoke(
            {"messages": [("user", "Where is Sammamish located?")]})
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
                    {"role": "user", "content": "Where is Seattle located?"}], stream=True)

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


def py_llama_chat():
    from llama_cpp import Llama
    start = time.time()
    # if user_prompt:
    model_path = "/Users/gongya/.ollama/models/blobs/sha256-e566218f2f25cfb315482a280283016bdb0c011f97e49cb327708c38fa075db5"
    llm = Llama(model_path=model_path, n_ctx=2048, verbose=False)
    response = llm.create_chat_completion(
        messages=[{"role": "user", "content": "Where is Seattle located?"}], max_tokens=100000)
    st_print(response["choices"][0]["message"]["content"])
    end = time.time()
    st.write(f"Response time: {end - start} seconds")
    return response
### EndofCodeSection###

