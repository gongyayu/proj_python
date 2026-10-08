import streamlit as st
import re
from py_mod import line_print, st_print, parsing_input,st_code,st_markline

### StartofFunc###


def py_matchemptyline():
    lines = parsing_input()
    st.code(lines)

    for line in lines.splitlines():
        if (re.search(r'^\s*$', line)):                                    # an empty line
            st.code(f'match empty: {line}')
### EndofCodeSection###


def py_matchstartwith():

    def matchText():
        lines = parsing_input()
        st.code(lines)

        for line in lines.splitlines():
            if line.startswith("#"):
                # if (re.match(r"^(#)",line)):
                # if (re.search(r'^\#',Line)):
                st.code(f'match comment: {line}')
    matchText()
    st_markline()

    def matchBytes():
        line = b"data: hello"

        # ❌ Raises TypeError: startswith first arg must be bytes or a tuple, not str
        try:
            line.startswith("data: ")
            st_code(f"matched")
        except Exception as e:
            st_code(f"Error: line.startswith('data: ') {str(e)}")
        finally: 
            if line.startswith(b"data: "):
                st_code(f"line.startswith(b'data: '): matched")
            # ✅ Works as expected: returns True
    matchBytes()
### EndofCodeSection###


def py_matchbyconstant():
    lines = parsing_input()
    st.code(lines)

    for line in lines.splitlines():
        if (re.search(r'partition_demo', line)):                           # match a constant
            st.code(f'match constant: {line}')
### EndofCodeSection###


def py_matchbyspace():
    lines = parsing_input()
    st.code(lines)

    for line in lines.splitlines():
        if re.search(r'^(\s{4})-\s(\"destination\")', line):
            st.code(f'match regex: {line}')
### EndofCodeSection###


def py_matchmacaddr():
    lines = parsing_input()
    st.code(lines)

    for line in lines.splitlines():
        # re.I  case insensitive, match MAC
        if re.search(r'([0-9A-F]{2}[:-]){5}([0-9A-F]{2})', line, re.I):
            st.code(f'match MAC: {line}')
        if re.search(r'([0-9A-Fa-f]{4}[:-]){2}([0-9A-Fa-f]{4})', line, re.I):
            st.code(f'match MAC: {line}')
### EndofCodeSection###


def py_matchIPv4():
    lines = parsing_input()
    st.code(lines)

    for line in lines.splitlines():
        if re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line):       # match IP
            # if re.search(r"(\d+).(\d+).(\d+).(\d+)", line):
            st.code(f'match IPv4: {line}')
### EndofCodeSection###


def py_match_pattern():
    import re

    timeList = [
        '3hours5minutes12seconds',
        '34minutes44seconds',
        '4hours32minutes32seconds',
        '2hours',
        '9minutes',
        '45seconds',
    ]

    pattern = re.compile(r'(?:(\d+)hours)?(?:(\d+)minutes)?(?:(\d+)seconds)?')

    match = pattern.match(timeList[0])

    for timeslot in timeList:
        match = pattern.match(timeslot)
        if match:
            hours, minutes, seconds = match.groups()
            st.code(
                f'Parsed {timeslot}: hours={hours}, minutes={minutes}, seconds={seconds}')
### EndofCodeSection###

def py_match_demo1():
    import json
    from pprint import pformat

    datalines = [
        b'data: {"id":"chatcmpl-fed41c94-7966-4553-8eff-5248d33becfa","choices":[{"index":0,"delta":{"content":" presence"},"finish_reason":null,"logprobs":null}],"created":1790375243,"model":"moonshotai/kimi-k3","object":"chat.completion.chunk"}',
        b'',
        b'data: {"id":"chatcmpl-fed41c94-7966-4553-8eff-5248d33becfa","choices":[{"index":0,"delta":{"content":"."},"finish_reason":null,"logprobs":null}],"created":1790375243,"model":"moonshotai/kimi-k3","object":"chat.completion.chunk"}',
        b'',
        b'data: {"id":"chatcmpl-fed41c94-7966-4553-8eff-5248d33becfa","choices":[{"index":0,"delta":{},"finish_reason":"stop","logprobs":null}],"created":1790375243,"model":"moonshotai/kimi-k3","object":"chat.completion.chunk"}',
        b'',
        b'data: {"id":"chatcmpl-fed41c94-7966-4553-8eff-5248d33becfa","choices":[],"created":1790375243,"model":"moonshotai/kimi-k3","object":"chat.completion.chunk","usage":{"prompt_tokens":91,"completion_tokens":182,"total_tokens":273,"prompt_tokens_details":{"cached_tokens":0},"completion_tokens_details":{"reasoning_tokens":7}}}',
        b'',
    ]
    for line in datalines:
        if line.startswith(b'data:'):
            data = line[6:]
            chunk = json.loads(line[6:])
            st.code(pformat(chunk))
            st_code(f"chunk['choices']: {chunk['choices']}")
            if chunk['choices']:
                st_code(f"chunk['choices'][0]: {chunk['choices'][0]}")
                st_code(f"chunk['choices'][0].get('delta'): {chunk['choices'][0].get('delta')}")
                delta = chunk['choices'][0].get('delta')
                st_code(f"'content' in delta: {'content' in delta}")
            st_markline()

### EndofCodeSection###
