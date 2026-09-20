import streamlit as st
from pprint import pformat
from py_mod import st_code, st_print, line_print, code_print, st_markline

### StartofFunc###

def pyreadbychunks():
    # See function -> yield
    pass
### EndofCodeSection###

def py_fromjson():
    import pandas as pd
    import json

    df = pd.read_json('data/in/sales.json')
    st_code(f"{df}")
    st_markline()
    #or fro simple json
    with open('data/in/sales.json', 'r') as f:
        data = json.load(f)
    st.code(pformat(data))
### EndofCodeSection###

def py_fromxls():
    import pandas as pd

    df = pd.read_excel('data/in/sales.xlsx')
    st_code(f"{df}")
### EndofCodeSection###

def py_fromcsv():
    import pandas as pd
    import csv
    df = pd.read_csv('data/in/sales.csv')
    st_code(f"{df}")

    df['total'] = df['quantity'] * df['price']
    st.code(f"{df}")

    '''
    df = pd.read_csv('data/in/sales.csv')
    '''
    for index, row in df.iterrows():
        st_code(f"{index}\n{row}")

    code_print('CSV data')
    code_print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    code_print(f"With totals:")
    st_code(code_print(f''))
### EndofCodeSection###

def pybinary_copy():
    def binary_copy(src_path: str, dst_path: str):
        buffer_size = 1024 * 4
        try:
            with open (src_path,'rb') as fr, open(dst_path,'wb') as fw:
                while chunk := fr.read(buffer_size):
                    fw.write(chunk)
            return True, 'copy done'
        except OSError as e:
            return False, f'IOError: {str(e)}'
    ok, msg = binary_copy("demo.jpg","demo_bak.jpg")
### EndofCodeSection###

