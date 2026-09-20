import openpyxl
import pandas as pd
import streamlit as st
from pprint import pformat
from py_mod import line_print, st_print, py_proj_path, st_markline

py_panda = 'Hello panda'
### StartofFunc###


def py_pd_demo1():
    df = pd.read_csv(py_proj_path + 'data/in/sales.csv')
    df['total'] = df['quantity'] * df['price']
    df.to_excel(py_proj_path + 'data/out/sales.xlsx', index=False)
    df = pd.read_excel(py_proj_path + 'data/out/sales.xlsx')
    st.code(df)
### EndofCodeSection###


def py_pd_demo2():
    df = pd.DataFrame(
        {
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        }
    )
    st.write(df)
    result = df[(df['A'] > 1) & (df['B'] < 6)]
    st.write(result)
### EndofCodeSection###

def py_pd_demo3():
    import requests
    from datetime import datetime, timedelta
    import matplotlib.pyplot as plt

    def get_weatherdata():
        # Calculate dates
        today = datetime.now()
        week_ago = today - timedelta(days=7)

        # Format dates for API (YYYY-MM-DD)
        start_date = week_ago.strftime("%Y-%m-%d")
        end_date = today.strftime("%Y-%m-%d")

        # Get Paris weather for past week
        url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

        response = requests.get(url)
        data = response.json()
        st.code(pformat(data, width=60), language="python")
        st_markline()

        daily_data = data['daily']
        st.code(pformat(daily_data))
        st_markline()

        # Create a DataFrame
        df = pd.DataFrame({
            'date': daily_data['time'],
            'max_temp': daily_data['temperature_2m_max'],
            'min_temp': daily_data['temperature_2m_min']
        })

        # Convert date strings to datetime
        # df['date'] = pd.to_datetime(df['date'])
        st.code(pformat(df))

        # Create the plot. This can't be run inside streamlit
        plt.figure(figsize=(10, 6))
        plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
        plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

        # Add labels and title
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.title('Paris Weather - Past 7 Days')
        plt.legend()

        # Rotate x-axis labels for readability
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the plot
        plt.savefig('weather_chart.png')
        plt.show()

    get_weatherdata()
### EndofCodeSection###

        
    


