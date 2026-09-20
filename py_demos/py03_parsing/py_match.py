import streamlit as st
import re
from py_mod import line_print, st_print, parsing_input

### StartofFunc###


def py_matchemptyline():
    lines = parsing_input()
    st.code(lines)

    for line in lines.splitlines():
        if (re.search(r'^\s*$', line)):                                    # an empty line
            st.code(f'match empty: {line}')
### EndofCodeSection###


def py_matchstartwith():
    lines = parsing_input()
    st.code(lines)

    for line in lines.splitlines():
        if line.startswith("#"):
            # if (re.match(r"^(#)",line)):
            # if (re.search(r'^\#',Line)):
            st.code(f'match comment: {line}')
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


def py_patternmatch():
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
