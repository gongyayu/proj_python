import streamlit as st
from py_mod import line_print, st_print, st_code, outlines

### StartofFunc###


def py_import():
    # import modules from sys path
    import os
    import sys
    st_code(f"import from sys path: {sys.path}")

    # impot modules from cwd, if the script is not called from importlib, '.' might be needed
    from . import py_panda
    st_code(
        f"os.pwd(): {os.getcwd()},  \npy_panda.__file__: {py_panda.__file__}, \
            \npy_panda.py_panda: {py_panda.py_panda}")

    # import modules from sub-directory, if the script is not called from importlib, '.' might be needed
    from .pkg import sub_mod
    st_code(f"sub_mod.greeting: {sub_mod.greeting}")

    # import modulels from appended path
    # sys.path.append(os.path.join(os.path.dirname(__file__),'py_pkg'))
    sys.path.append(
        '/Users/gongya/Programming/mac_python/proj_python/py_demos/py07_modules/')
    from pkg import sub_mod
    st_code(f"sub_mod.greeting: {sub_mod.greeting}")

    # import a module via alias
    from pkg import sub_mod as mod3
    st_code(f"mod3.greeting: {mod3.greeting}")

    from pkg.sub_mod import greeting
    st_code(f"grreting: {greeting}")
### EndofCodeSection###
