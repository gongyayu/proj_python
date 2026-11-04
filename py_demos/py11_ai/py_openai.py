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
    def openai_agentA():
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

    def openai_agentB():
        # initiate large language model (temperature = 0)
        llm = ChatOpenAI(temperature=0)

        # fetch the prompt from the prompt hub
        prompt = hub.pull("hwchase17/openai-functions-agent")

        # create the tools
        @tool(response_format="content_and_artifact")
        def retrieve(query: str):
            """Retrieve information related to a query."""
            retrieved_docs = vector_store.similarity_search(query, k=2)
            serialized = "\n\n".join(
                (f"Source: {doc.metadata}\n" f"Content: {doc.page_content}")
                for doc in retrieved_docs
            )
            return serialized, retrieved_docs

        # combine the tools and provide to the llm
        tools = [retrieve]
        agent = create_tool_calling_agent(llm, tools, prompt)

        # create the agent executor
        agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

        # invoke the agent
        response = agent_executor.invoke({"input": "why is agentic rag better than naive rag?"})

        # put the result on the screen
        print(response["output"]) 
### EndofCodeSection###