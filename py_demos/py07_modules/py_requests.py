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