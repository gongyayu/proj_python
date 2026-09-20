import streamlit as st
import re
from py_mod import line_print, st_print, parsing_input

### StartofFunc###


def py_replaceconstant():
    lines = parsing_input()
    st.code(lines)
    for line in lines.splitlines():
        if (re.search(r'first', line)):
            # replace a constant
            st.code(
                f"{line}\n re.sub(r'first', 'second', line) --> {re.sub(r'first', 'second', line)}")
### EndofCodeSection###


def py_replaceparentheses():
    lines = parsing_input()
    st.code(lines)
    for line in lines.splitlines():
        if (re.search(r'[(|)]', line)):
            st.code(
                f"{line}\n re.sub('[(|)]', '', line): --> {re.sub('[(|)]', '', line)}")
### EndofCodeSection###


def py_replacespaces():
    lines = parsing_input()
    st.code(lines, width='stretch')
    for line in lines.splitlines():
        if (re.search(r'^\s+', line)):
            st.code(
                f"{line}\n re.sub(r'^\s+', '', line): --> \n{re.sub(r'^\s+', '', line)}", width='stretch')

    s = 'A string with     white space'
    st.code(
        # => 'Astringwithwhitespace'
        f"s, ' -->', ''.join(s.split()): --> {s, ' -->', ''.join(s.split())}", width='stretch')

    s = 'A string with     white space'
    st.code(
        # => 'Astringwithwhitespace'
        f"s, ' --> ', s.replace(' ', ''): --> {s, ' --> ', s.replace(' ', '')}", width="stretch")
### EndofCodeSection###


def py_replacebyrex():
    str = 'njb-esw-ha-b-B20.amc.uwmedicine.org'
    st.code(f"{str}:re.sub(r'\..+','',str) -> {re.sub(r'\..+', '', str)}")
### EndofCodeSection###


def py_remove_hdtl_spaces():
    # removing tailing spaces, tab and newline
    text = "Hello World   \t\n"
    st.code(f"text {len(text)}: {text.rstrip()} ({len(text.rstrip())})")
    # remove only space characters, not other whitespace
    text = "Hello World   "
    st.code(f"text {len(text)}: {text.rstrip(' ')} ({len(text.rstrip(' '))})")

    text = "   Hello World   "
    # remove whitespace from both beginning and end rstrip vs.lstrip
    st.code(f"{text} {len(text)}: {text.strip()} ({len(text.strip())})")

    # Method 1: Using splitlines()
    multiline = "Line 1   \nLine 2   \nLine 3   "
    cleaned = '\n'.join(line.rstrip() for line in multiline.splitlines())
    st.code(f"{multiline}: \ncleaned: {cleaned}")

    # Method 2: Using list comprehension
    lines = ["Hello   ", "World   ", "Python   "]
    cleaned = [line.rstrip() for line in lines]
    st.code(f"cleaned: {cleaned}")

### EndofCodeSection###
