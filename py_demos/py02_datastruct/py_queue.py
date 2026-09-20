import streamlit as st
import json
from py_mod import line_print, st_print

### StartofFunc###


def py_queue():
    from collections import deque
    q = deque()

    q.append('1st element')
    q.append('2nd element')
    q.append('3rd element')

    line_print(f"q: {q}")

    a = q.popleft()
    line_print(f"The first popped element is: {a}")

    b = q.popleft()
    line_print(f"the second popped element is: {b}")

    c = q.popleft()
    line_print(f"The third popped element is : {c}")
    st_print(line_print(''))
### EndofCodeSection###
