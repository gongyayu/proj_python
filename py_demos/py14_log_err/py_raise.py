from py_mod import line_print,st_print,st_code,code_print, st_markline
import streamlit as st

### StartofFunc###

def py_raiseA():
    def check_value(x):
        if x < 0:
            # raise ValueError("Negative value not allowed")    only for the terminal
            st.error(f"Negative value not allowed")  # for the log file
        return x
    check_value(-5)
### EndofCodeSection###