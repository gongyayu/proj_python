import streamlit as st
from py_mod import line_print, st_print, st_code,st_markline

### StartofFunc###


def py_demo1():
    a = 5
    a, a = a + 1, a + 2
    st.code(a)
### EndofCodeSection###

def py_TowerOfHanoi():
    def TowerOfHanoi(n, fromRod, toRod, auxRod):
        if n == 0:
            return
        TowerOfHanoi(n-1, fromRod, auxRod, toRod)
        st_code(f"Disk {n} moved from {fromRod} to {toRod}")
        TowerOfHanoi(n-1, auxRod, toRod, fromRod)
    TowerOfHanoi(3, 'F','A','T')
### EndofCodeSection###
