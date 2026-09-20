import streamlit as st
from py_mod import line_print, st_print

### StartofFunc###


def py_condition():
    age = 22
    if age >= 20:
        st.code("Adult")
    elif age >= 13:
        st.code("Teenager")
    else:
        st.code("Child")

    st.markdown('---')
    name = "Mosh"
    if not name:
        st.code("Name is empty")
    else:
        st.code(name)

    st.markdown('---')
    name = " "
    if not name.strip():
        st.code("Name is empty")

    st.markdown('---')
    age = 22
    if age >= 18 and age < 65:
        st.code("Eligible")

    st.markdown('---')
    if 18 <= age < 65:
        st.code("Eligible")

    st.markdown('---')
    # ternary
    message = "Eligible" if age >= 18 else "Not Eligible"
    st.code(message)

    st.markdown('---')
    x, y = 25, 50
    big = x if x < y else y
    st.code(big)

    st.markdown('---')
    x = 1
    y = x
    if y is x:
        st.code(f'x: {id(x)} y: {id(y)}')
### EndofCodeSection###
