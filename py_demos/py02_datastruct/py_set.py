import streamlit as st
import json
from py_mod import line_print, st_print, st_code,code_print,st_markline

### StartofFunc###


def py_set():
    # create an empty set
    set1 = set()
    codelines =f"set1: {type(set1)}"
    # create a set with elements
    set1 = {1,2,2,3,4,4,5}
    st_code(f"{codelines} \nset1: {type(set1)} \nset: {set1}")   # no duplicated elements
### EndofCodeSection###

def py_list_set():
    a = [5,63,8,2,25,4,5,15,5,9]
    code_print(f"a: {a}")
    code_print(f"set(a): {set(a)}")                   # list to set to exclude the duplicates
    code_print(f"a: {list(set(a))}")                  # set back to list without the duplicates
    st_code(f"{code_print('')}")
### EndofCodeSection###

def py_setops():
    a = {1,2,3,4}
    code_print(f"a: {a}")
    a.add(5)
    st_code(f"{code_print('')}a: {a}")
    st_markline()

    a = {25,36,8}
    b = {3,25,9}
    st_code(f"a&b: {a&b}, a.intersection(b): {a.intersection(b)}")                                               # elements in both a and b
    st_markline()
    st_code(f"a-b: {a-b}, a.difference(b): {a.difference(b)} | b-a: {b-a}, b.difference(a): {b.difference(a)}")  # elements in a does not exist in b
    st_markline()
    st_code(f"a|b: {a|b}, a.union(b): {a.union(b)}")                                                              # elements in a or b
    st_markline()
    st_code(f"a^b: {a^b}, a.symmetric_difference(b) : {a.symmetric_difference(b)}")                               # elements exists in either of sets only
### EndofCodeSection###

def py_setcompare():
    # perform difference operation using &
    set1 = {1,2,3,4}
    set2 = {1,2,3,4}
    if set1 == set2:
        st_code(f'Set1 and Set2 are equal')
    else:
        st_code(f'Set1 and Set2 are not equal') 
### EndofCodeSection###

def py_setmodify():
    languages = {'Swift', 'Java', 'Python'}
    languages.discard('Java')                          # remove 'Java' from a set
    st_code(f"languages: {languages}")

    companies = {'Lacoste', 'Ralph Lauren'}
    tech_companies = ['apple', 'google', 'apple']                   # list
    companies.update(tech_companies) 
    st_code(f"companies.update(tech_companies): {companies}")
### EndofCodeSection###

def py_setloop():
    fruits = {"Apple", "Peach", "Mango"}
    # for loop to access each fruits
    for fruit in fruits:
        code_print(f"fruit: {fruit}")
    st_code(f"{code_print('')}")
### EndofCodeSection###



 
