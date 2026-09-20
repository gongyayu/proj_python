import streamlit as st
import os
from py_mod import line_print, st_code, st_print

### StartofFunc###


def py_create_package():
    st.markdown(f"create a \_\_init\_\_ empty file in a package folder. ")
    st_code(f"{os.listdir('py07_modules/pkg')}")
### EndofCodeSection###
