import glob
import os
import re
import streamlit as st
import importlib


options = False
debug = False
non_topic_list = ['py_data', '__pycache__', 'data']
_st = True
outlines = codelines = ''
py_proj_path = '/Users/gongya/Programming/mac_python/proj_python/py_demos/'

# AI
llm_model = 'gpt-oss:latest'
ollama_model = 'llama3.1:8b'
ollama_URL = "http://localhost:11434/api/chat"

# demo variables

topic_list = sorted([topic for topic in glob.glob(
    '*') if os.path.isdir(topic) and topic not in non_topic_list])


def subtopic_list(topic):
    return [subtopic.split('/')[1] for subtopic in glob.glob(topic + '/*.py') if not os.path.isdir(subtopic) and re.search(r'^py(\d+)_', subtopic)]


def parsing_input() -> str:
    inFile = 'data/in/Parsing-input.txt'
    with open(inFile, 'r') as FH:
        return FH.read()


def get_func_info(mod_file):
    startoffunc = 0
    funcstart = 0
    funclist = []
    code_content = {}
    code_lines = ''
    code_def = 0

    with open(mod_file, 'r') as FH:
        for line in FH:
            # if (re.search(r'^\s*$',line)): continue
            if re.search(r'^###(\s)StartofFunc###', line):
                # funclist.append('null')
                startoffunc = 1
                continue
            if startoffunc == 1:
                if re.match(r'^def\s', line):
                    if code_lines == '':
                        code_lines = line
                        code_def = 1
                    # ln = re.sub(r'^def\s',"",line.strip(':')).split(':')[0]
                    # remove all trailing whilespaces
                    line = line.rstrip()
                    # remove the end :
                    ln = re.sub(r'^def\s', "", line.strip(':'))
                    funclist.append(ln)
                    funcstart = 1
                if re.match(r'###(\s)EndofCodeSection###', line):
                    code_content[ln] = code_lines
                    funcstart = 0
                    code_lines = ''
                    continue
                if funcstart == 1:
                    if code_def == 1:
                        code_def = 0
                        continue
                    code_lines += line
    return funclist, code_content


def func_details(mod_file, func_item, func_content):
    try:
        st.code(func_content[func_item], width="content")
    except Exception as e:
        print(f"Error: {str(e)}")
    if debug:
        st.write(mod_file, func_item)
    if re.search(r'^py_', func_item):
        f = re.sub(r'[\(|\):]', '', func_item)
        f = re.sub(r'\s+', '', f)

        mdir = mod_file.split('/')[-2]
        m = mod_file.split('/')[-1]
        m = re.sub(r'\.py', '', m)
        if st.button("run"):
            st.write(execute_func(mdir, m, f))


def execute_func(mod_dir, mod_name, func):
    # if mod_name in get_modlist(py_var.packages_dir):
    module = importlib.import_module(mod_dir + '.' + mod_name)
    func = getattr(module, func)
    func()


def line_print(out: str) -> str:
    global outlines
    outlines += out + '<br>'
    return outlines


def code_print(out: str) -> str:
    global codelines
    codelines += out + '\n'
    print(f"--- {codelines}")
    return codelines


def st_print(out: str):
    global outlines
    if _st:
        st.write(f'{out}', unsafe_allow_html=True)
        outlines = ''
    else:
        print(f'{out}')


def st_code(str):
    global codelines
    st.code(str, width='content', wrap_lines=True)
    codelines = ''


def st_markline():
    st.markdown("---")
