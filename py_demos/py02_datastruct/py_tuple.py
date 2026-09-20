import streamlit as st
import json
from py_mod import line_print, st_print

### StartofFunc###


def py_tuple():
    line_print(f"pytuple_operations() {'-' * 30}")
    prt = 0
    tup1 = ()
    # comma is required
    tup1 = (50,)
    tup2 = ('abcd', 786, 2.23, 'john', 70.2)
    line_print(
        f"tup1: {tup1}, tup2: {tup2}, tup2[0]: {tup2[0]}, tup2[1:4]: {tup2[1:4]}, tup2[2:]: {tup2[2:]}")
    # Print list two times
    line_print(f"tup1 * 2: {tup1 * 2}")
    # Print concatenated lists
    line_print(f"tup1 + tup2: {tup1 + tup2}")

    try:
        tup1[0] = 10
    except Exception as e:
        line_print(f'tup1[0] = 10:  {str(e)}')

    try:
        del tup1[0]
    except Exception as e:
        line_print(f'del tup1[0]: {str(e)}')

    # list to Tuple
    a = ['a', 'b', 'c']
    b = [1, 2, 3]
    # => [('a', 1), ('b', 2), ('c', 3)]
    line_print(
        f"[(k, v) for k, v in zip(a, b)]: {[(k, v) for k, v in zip(a, b)]}")
    st_print(line_print(f''))
### EndofCodeSection###
