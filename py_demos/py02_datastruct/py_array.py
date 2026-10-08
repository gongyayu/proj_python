import streamlit as st
import json
import numpy as np
from py_mod import code_print, st_print, code_print, st_code, st_markline


### StartofFunc###

def py_array():
    import array as arr
    array_i = arr.array("i", [3, 6, 9, 12])
    code_print(f"type: {type(array_i)}, array_i: {array_i}, array_i.typecode: {array_i.typecode}, \
               array_i.itemsize: {array_i.itemsize}, array_i.buffer_info(): {array_i.buffer_info()}")
    
    # 'u' is deprecated
    array_u = arr.array('u', ['e', 'f', 'd', 'g'])
    code_print(
        f"type: {type(array_u)}, array_u: {array_u}, array_u.typecode: {array_u.typecode}, \
        array_u.itemsize: {array_u.itemsize}, array_u.buffer_info(): {array_u.buffer_info()}")
    st_code(code_print(f''))
### EndofCodeSection###


def py_array_loop():
    import array as arr

    array_i = arr.array("i", [3, 6, 9, 12])

    array_a = arr.array(array_i.typecode, (a for a in array_i))        # create a new array with the same typecode and values as array_i
    code_print(f"array_a: {array_a}")
    
    array_b = arr.array(array_i.typecode, (a*a for a in array_i))      # create a new array with the same typecode and values as array_i, but each value is squared
    code_print(f"array_b: {array_b}")
    st_code(code_print(f''))
### EndofCodeSection###

def py_array_ops():  
    import array as arr              
    # arrary vs list (array for single type and list for multiple type)
    li = [3, 6, 9, 12]

    try:
        code_print(f"li/3: {li/3}")
    except Exception as e:
        code_print(f"l1/3 Error: {str(e)}")
    
    array_i = arr.array("i", [3, 6, 9, 12])
    try:
        code_print(f"array_i/3: {array_i/3}")
    except Exception as e:
        code_print(f"array_i/3 Error: {str(e)}")             # For array division you should use NumPy.
    st_code(code_print(f''))
### EndofCodeSection###

def py_array_slicing():
    import array as arr
    array_i = arr.array("i", [3, 6, 9, 12])
    # array slicing
    code_print(f"array_i[1:3]: {array_i[1:3]}")
    code_print(f"array_i[::2]: {array_i[::2]}")
    code_print(f"array_i[::-1]: {array_i[::-1]}")
    st_code(code_print(f''))
### EndofCodeSection###

def py_array_methods():
    import array as arr
    a = arr.array('d', [1.1, 2.2, 3.8, 3.1, 3.7, 1.2, 4.6])
    code_print(f"array methods: {dir(a)}")
    code_print(
        f"a.pop(3): {a.pop(3)}, a.remove(1.1): {a.remove(1.1)}, a: {a}")

    st_code(code_print(f''))
### EndofCodeSection###
