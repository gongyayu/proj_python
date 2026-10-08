from py_mod import line_print, st_print, st_code,code_print,st_markline

### StartofFunc###
import os

def py_dir():
    st_code(f"os.getcwd(): {os.getcwd()}, \n\ndir(os.getcwD()): {dir(os.getcwd())}")

    l1 = []
    st_code(f"dir(l1):  {dir(l1)}")
### EndofCodeSection###