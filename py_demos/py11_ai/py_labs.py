import streamlit as st
from shared_mod.shared_mod import st_print, st_code
from shared_mod.shared_ai import codedir


### StartofFunc###

def py_chat():
    codefile = codedir + 'ai_mod/chat_mod.py'
    with open(codefile, 'r', encoding='utf-8') as f:
        st_code(f.read())
### EndofCodeSection###

def py_agent():
    codefile = codedir + 'ai_mod/chain_mod.py'
    with open(codefile, 'r', encoding='utf-8') as f:
        st_code(f.read())
### EndofCodeSection###

def py_function_calling():
    codefile = codedir + 'ai_mod/fc_mod.py'
    with open(codefile, 'r', encoding='utf-8') as f:
        st_code(f.read())
### EndofCodeSection###