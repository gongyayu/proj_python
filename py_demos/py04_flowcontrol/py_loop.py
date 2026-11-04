import streamlit as st
from py_mod import line_print, st_print,code_print,st_code,st_markline

### StartofFunc###

def py_for_enumerate():
    names = ['Corey', 'Chris', 'Dave', 'Travis']
    for index, name in enumerate(names):
        code_print(f"index {index}: name {name}")
    st_code(f"{code_print(f'')}")

    ###########################################
    st.markdown('---')
    for index, name in enumerate(names, start=1):
        code_print(f"index {index}: name {name}")
    st_code(f"{code_print(f'')}")  
### EndofCodeSection###

def py_for_zip():
    nameList = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruse Wayne']
    heroList = ['Spiderman', 'superman', 'Deadpool', 'Batman']
    universeList = ['Marvel', 'DC', 'Marvel', 'DC']

    for name, hero, universe in zip(nameList, heroList, universeList):
        code_print(f'{name} is actually {hero} from {universe}')
    st_code(f"{code_print(f'')}") 

    st.markdown('---')
    for value in zip(nameList, heroList, universeList):
        code_print('value: %s ' % str(value))
    st_code(f"{code_print(f'')}") 
### EndofCodeSection###

def py_for_range():
    for x in range(0, 10, 2):
        # [0,2,4,6,8]
        code_print(f"{x}")
    st_code(f"{code_print(f'')}") 
### EndofCodeSection###

def py_for_break():
    names = ["AJohn", "Mary", "John"]
    for name in names:
        if name.startswith("J"):
            code_print("found")
            break
        else:
            code_print("Not found")
    st_code(f"{code_print(f'')}")
### EndofCodeSection###


def py_for_continue():
    names = ["AJohn", "Mary", "John"]
    for name in names:
        if name == 'Mary':
            continue
        code_print(name)
    st_code(f"{code_print(f'')}")
### EndofCodeSection###

def py_for_pass():
    names = ["AJohn", "Mary", "John"]
    for name in names:
        if name == 'Mary':
            pass
        code_print(name)
    st_code(f"{code_print(f'')}")
### EndofCodeSection###

def py_for_else():
    def case_1():             # The else clause is skipped if the loop breaks prematurely due to a break statement.
        fruits = ['apple', 'banana', 'cherry']
        for fruit in fruits:
            if fruit == 'banana':
                break
            code_print(f"{fruit}")
        else:
            code_print(f"We didn't break out of the loop.")
        st_code(f"{code_print(f'')}")

    def case_2():                         # the else clause is executed if the loop iterates over all items in the iterable without encountering a break statement within the loop.
        numbers = [1, 2, -3, 4, 5]
        for num in numbers:
            if num < 0:
                code_print(f"Invalid number: {num}")
        else:
            code_print("All numbers are valid.")
        st_code(f"{code_print(f'')}")

    case_1()
    case_2()
### EndofCodeSection###


def py_while():
    var = 10                    # Second Example
    while var > 0:
        var -= 1
        st.code(f"Current variable value : {var}")
### EndofCodeSection###
