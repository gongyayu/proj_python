import time
import streamlit as st
from py_mod import st_print, st_code, ollama_model, ollama_model, ollama_URL, debug


### StartofFunc###
def py_tokenrouter_chat():
    from tokenrouter import TokenRouter, AuthenticationError, RateLimitError
    from dotenv import load_dotenv
    import os

    load_dotenv(override=True)
    TOKENROUTER_API_KEY = os.getenv("TOKENROUTER_API_KEY")

    client = TokenRouter(
        api_key=TOKENROUTER_API_KEY,
        base_url="https://api.tokenrouter.com/v1"
    )

    try:
        response = client.chat.completions.create(
            model="z-ai/glm-5.3-free",
            mode="balanced",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Where is Seattle located?"}
            ],
        )
        st_code(response)
        return response

    except AuthenticationError:
        st_print("Invalid API key. Check your TokenRouter credentials.")
    except RateLimitError as e:
        st_print(f"Rate limited. Retry after: {e.retry_after}s")
    except Exception as e:
        st_print(f"Error: {e}")
### EndofCodeSection###