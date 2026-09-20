import streamlit as st
from py_mod import st_code, st_print, line_print, code_print

### StartofFunc###


def py_writetotextfile():
    outFile = 'data/out/demo-out.txt'
    try:
        with open(outFile, "w") as FH:                              # (r,a,w,x,t,b(binary))
            FH.write('This is written to a file')
            st_code(f"Successful to write to {outFile}")
    except Exception as e:
        st_code(f"Error: {str(e)}")
### EndofCodeSection###

def py_float():
    amount = 5.2300
    st_code(f"${amount:,.2f}")
### EndofCodeSection###
