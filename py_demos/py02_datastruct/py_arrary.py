import streamlit as st
import json
import numpy as np
from py_mod import line_print, st_print


### StartofFunc###

def py_array():
    line_print(f"pyarray() {'-' * 30}")
    import array as arr
    array_1 = arr.array("i", [3, 6, 9, 12])
    line_print(f"type: {type(array_1)}, array_1: {array_1}")
    # 'u' is deprecated
    array_a = arr.array('u', ['e', 'f', 'd', 'g'])
    line_print(
        f"type: {type(array_a)},array_a.typecode: {array_a.typecode}, array_a: {array_a}")
    newArray = arr.array(array_1.typecode, (a for a in array_1))
    line_print(f"newArray: {newArray}")
    newArray_1 = arr.array(array_1.typecode, (a*a for a in array_1))
    line_print(f"newArray_1: {newArray_1}")

    array_2 = np.array(["numbers", 3, 6, 9, 12])
    line_print(f"type: {type(array_2)}, array_2: {array_2}")
    st_print(line_print(f''))
### EndofCodeSection###


def py_array_operations():
    import array as arr

    line_print(f"pyarray_operations(): {'-' * 30}")
    # arrary vs list (array for single type and list for multiple type)
    a = np.array([3, 6, 9, 12])
    line_print(f"np.array([3,6,9,12]): {a}, a/3: {a/3}")

    li = [3, 6, 9, 12]
    try:
        li/3
    except Exception as e:
        line_print(f"l1/3 Error: {str(e)}")

    array_1 = arr.array("i", [3, 6, 9, 12])
    for i in range(len(array_1)):
        line_print(f"array_1[i]: {array_1[i]}")

    # array info
    line_print(
        f"type(array_1): {type(array_1)}, array_1.buffer_info(): {array_1.buffer_info()}, array_1.typecode: {array_1.typecode}")

    line_print(f"array_1[::-1]: {array_1[::-1]}")

    a = arr.array('d', [1.1, 2.2, 3.8, 3.1, 3.7, 1.2, 4.6])
    line_print(
        f"a.pop(3): {a.pop(3)}, a.remove(1.1): {a.remove(1.1)}, a: {a}")

    # array concat
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    # => array([1, 2, 3, 4, 5, 6])
    line_print(f"np.concatenate((a, b)): {np.concatenate((a, b))}")
    st_print(line_print(f''))
### EndofCodeSection###
