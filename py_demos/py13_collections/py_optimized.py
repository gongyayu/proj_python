import streamlit as st
from py_mod import line_print, st_code, st_print, parsing_input

### StartofFunc###


def py_singlelinecode():

    count = 0
    for line in parsing_input().splitlines():
        for character in line:
            if character.isupper():
                count += 1
    st_code(f"count: {count}")

    count = sum(
        1 for line in parsing_input().splitlines() for character in line if character.isupper())
    st_code(f"count: {count}")
### EndofCodeSection###


def py_if():
    condition = False
    x = 1 if condition else 0
    st_code(f"x: {x}")
### EndofCodeSection###

def py_specialsyntax():
    age = 16
    can_vote = age >= 18
    st_code(can_vote)
### EndofCodeSection###

