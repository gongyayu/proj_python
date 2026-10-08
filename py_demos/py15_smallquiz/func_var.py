import streamlit as st
from py_mod import line_print, st_print, st_code, code_print,st_markline

### StartofFunc###

def py_ext_variables():
    def outer(x):
        def inner():
            return x
        return inner
    f = outer(10)
    st_code(f"f(): {f()}")
### EndofCodeSection###

def py_lambda_varbind():
    def lambda01():
        funcs = []
        for i in range(3):
            func = lambda x: x + i               # late binding. In Python, a lambda (or any nested function) captures variables by reference, not by value. 
            funcs.append(func)
        run = [f(1) for f in funcs]
        st_code(f"{run}")
    lambda01()
    st_markline()

    def lambda02():
        funcs = []
        for i in range(3):
            func = lambda x, i=i: x + i           # bind the value instead of the references
            funcs.append(func)
        run = [f(1) for f in funcs]
        st_code(f"{run}")
    lambda02()
### EndofCodeSection###
