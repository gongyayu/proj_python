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

def py_end_flush():
    a = [1,2,3,4]
    b = [4,5]

    for x,y in zip(a,b):
        print(x + y, end=" ", flush=True)                           # the output will hold without flush=True
### EndofCodeSection###

def py_alignmment():
    def horizontal_alignment():
        s = "Python"
        s1 = s.zfill(8)
        s2 = s.rjust(8,"0")
        s3 = s.ljust(8,"0")
        st_code(f"s1,s2,s3: {s1}, {s2}, {s3}")
    horizontal_alignment()
### EndofCodeSection###
