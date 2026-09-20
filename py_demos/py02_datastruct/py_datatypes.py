import streamlit as st
import json
from py_mod import line_print, st_print,st_code,code_print,codelines

### StartofFunc###

def py_strtype():
    s: str = "123"                                                     # s = '123'
    st_code(f"s -> type: {type(s)}")
    st_code(f"'hello' -> string instance: {isinstance('hello', str)}")
### EndofCodeSection###

def py_numtype():
    a = 123
    b = 1.23
    st_code(f"a: {type(a)}, b: {type(b)}")  
### EndofCodeSection###

def py_booltype():
    a = True
    b = False
    st_code(f"a: {type(a)}, b: {type(b)}")
### EndofCodeSection###
  
def py_listtype():
    li = []
    codelines = f"li: {type(li)}"
    li = [1,2,3]
    st_code(f"li: {codelines}, li: {type(li)}")
    A = (['apple','banana','orange'])
    code_print(f"A: {A}, A: {type(A)}")
    B = (['apple','banana','orange'],['pear'])
    st_code(f"{code_print('')}B: {B}, B: {type(B)}")
### EndofCodeSection###

def py_dicttype():
    dict = {}
    codelines = f"dict: {type(dict)}"
    dict = {1:'apple',2:'banana',3:'orange'}
    st_code(f"{codelines}, dict: {type(dict)}")
### EndofCodeSection###

def py_tupletype():
    tup = ()
    codelines = f"tup: {type(tup)}"
    tup = ('apple','banana','orange')
    st_code(f"tup: {codelines}, tup: {type(tup)}")
### EndofCodeSection###

def py_settype():
    set1 = set()
    codelines =f"set1: {type(set1)}"
    set1 = {1,2,3,4}
    st_code(f"set1: {codelines}, set1: {type(set1)}")
### EndofCodeSection###
