import streamlit as st
from py_mod import line_print, st_print, code_print, st_code, st_markline

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

def pyoneline():
    device = 0 if torch.cuda.is_available() else -1
### EndofCodeSection###

def py_match():
    def demo1():
        a = 10
        b = 20
        cal = '*'
        num = 0

        match cal:
            case '+':
                num = a + b
            case '- ':
                num = a - b
            case '*':
                num = a * b
            case '/':
                num = a / b
            case '_':
                st_code(f"'_' is not supported !")
        st_code(f"num: {num}")
    demo1()
### EndofCodeSection###  


