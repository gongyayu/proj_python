import streamlit as st
from py_mod import line_print, st_print, st_code

### StartofFunc###


def py_nested_function():
    def out_function(x):
        # Inner function defined inside outer_function
        def inner_function(y):
            return y * 2

        # Calling inner_function inside outer_function
        result = inner_function(x)
        return result

    def nested_functioncall():
        # Output: 10
        st_code(f"out_function(5): {out_function(5)}")
    nested_functioncall()
### EndofCodeSection###


def py_recursive_call():
    c = 0

    def monkey_f(self, c):
        st_code(f'c = {c}')
        if c > 5:
            pass
        else:
            monkey_f('self', c+1)
    st_code(f"monkey_f('self', c): {monkey_f('self', c)}")
### EndofCodeSection###


def py_decorator():
    def pydecorator(func):
        def log_function_called():
            st_print('The decorator is called')
            func()
            st_print('The decorator is called')
        return log_function_called

    @pydecorator
    def py_decorated():
        st_code('py_decorated is called')
    py_decorated()

    # with func input parameters
    def add_sprinkles(func):
        def wrapper(*args, **kwargs):
            st_code(f' *You add sprinkle *')
            func(*args, **kwargs)
        return wrapper
    st.markdown('---')

    def add_fudge(func):
        def wrapper(*args, **kwargs):
            st_code(f' *You add fudge *')
            func(*args, **kwargs)
        return wrapper

    @add_sprinkles
    @add_fudge
    def get_ice_cream(flavor):
        st_code(f'Here is your {flavor} ice cream ')

    get_ice_cream('vanilla')
### EndofCodeSection###
