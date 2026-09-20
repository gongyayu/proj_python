import re
import streamlit as st
from py_mod import line_print, st_print, st_code, st_markline, py_proj_path, parsing_input


### StartofFunc###


def py_splitbylines():
    lines = parsing_input()
    inFile = py_proj_path + 'data/in/Parsing-input.txt'
    with open(inFile, 'r') as FH:
        st.code(FH.read())

    with open(inFile, 'r') as FH:
        for line in FH.read().splitlines():
            st.code(line)
            lines += line

    st.markdown('---')
    with open(inFile, 'r') as FH:
        for line in FH.read().split('\n'):
            st.code(line)
### EndofCodeSection###


def py_splitbyspace():
    line = 'VLAN1091            64:87:88:e1:82:4d   D   -   et-0/1/0.0             0         0'
    columns = line.split()
    for c in columns:
        st.code(c)
### EndofCodeSection###


def py_splitbychar():
    # Split the string into a list with max 2 items:
    txt = "apple#banana#cherry#orange"

    col = ''
    columns = txt.split('#')
    for c in columns:
        st.code(c)

    st.markdown('---')
    # setting the maxsplit parameter to 1, will return a list with 2 elements!
    columns = txt.split("#", 1)
    # ['apple', 'banana#cherry#orange']
    st.code(columns)

### EndofCodeSection###


def py_splitbyconstant():
    txt = "apple#banana#cherry#orange"
    # by a constance:
    st.code(txt.split('banana'))
### EndofCodeSection###

def py_splitquizes():
    def splitquiz01():
        import re
        text = "apple,banana;orange|grape"
        st_code(f"{re.split(r'[,;|]\s*',text)}")
    splitquiz01()
### EndofCodeSection###


        


