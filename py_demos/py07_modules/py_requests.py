import requests
from py_mod import st_code, code_print,st_markline
import streamlit as st
from pprint import pformat

### StartofFunc###

def py_getweather():
    # We need coordinates to get weather data
    latitude = 48.85   # Paris latitude
    longitude = 2.35   # Paris longitude

    # Build the API URL with our parameters
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

    # Make the request
    response = requests.get(url)
    data = response.json()

    st.code(pformat(data, width=60), language="python")
    st_markline()

    temperature = data['current']['temperature_2m']
    st_code(f"Temperature in Paris: {temperature}°C")

### EndofCodeSection###

def py_get_html_text():
    try:
        def get_web_text(url):
            headers = {"User-Agent": "Moxilla5.0"}
            resp = requests.get(url, headers=headers, timeout=10)
            resp.raise_for_status()
            resp.encoding = resp.apparent_encoding
            # get web page documentation
            html_text = resp.text
            # retrieve the first 500 words    
            html_text = f"browsing the web page docs: \n" + html_text[:500]
            return html_text
    except Exception as e:
        return f"Error: {str(e)}"
    st_code(f"{get_web_text('https://www.baidu.com')}")
### EndofCodeSection###

def py_fetch_html_textA():
    import requests
    from bs4 import BeautifulSoup

    url = "https://www.washington.edu"

    headers ={
        "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding
        soup = BeautifulSoup(resp.text,"html.parser")
        pure_text = soup.get_text(separator='\n', strip=True)
        code_print(f"{pure_text}")
    except Exception as e:
        code_print(f"{str(e)}")
    st_code(f"{code_print(f'')}")
### EndofCodeSection### 

def py_fetch_html_textB():
    import requests
    from bs4 import BeautifulSoup
    url = "https://wikipedia.org"
    response = requests.get(url)
    st.write(response)
    soup = BeautifulSoup(response.text,"html.parser")
    headings = soup.find_all("div") 

    for heading in headings:
        st_code(f"{heading.text.strip()}")
### EndofCodeSection### 

def py_fetch_html_textC():
    from bs4 import BeautifulSoup
    from urllib.request import urlopen

    with urlopen("https://en.wikipedia.org/wiki/Main_page") as response:
        soup = BeautifulSoup(response, "html.parser")
        for anchor in soup.find_all("a"):
            st_code(f"{anchor.get("href","/")}")
### EndofCodeSection### 


    