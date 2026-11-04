from py_mod import line_print,st_print,st_code,code_print, st_markline
import streamlit as st

### StartofFunc###
def py_tryA():
    tinydict = {}
    # delete the entire dictionary
    del tinydict
    try:
        st_code(f"tinydict -> {tinydict}")
    except Exception as e:
        st_code(f"Error: {str(e)}")
### EndofCodeSection###

def py_tryB():
    try:
        with open("test.txt") as fh:
            st_code(f"file open successful")
            pass
    except Exception as e:
        st_code(f"Error: {str(e)}")
    else:
        st_code(f"\nELSE runs when the TRY works")
    finally:
        st_code(f"final deal always runs")
### EndofCodeSection###

def py_tryC():
    try:
        with open("data/in/Parsing-input.txt") as fh:
            st_code(f"file open successful")
            #pass
    except Exception as e:
        st_code(f"Error: {str(e)}")
    else:
        st_code(f"ELSE runs when the TRY works")
    finally:
        st_code(f"final deal always runs")
### EndofCodeSection###

def py_tryD():
    try:
        answer = 10/0
        number = int(input('Enter a number: '))
        st_code(f"number -> {number}")
    except Exception as e:
        st_code(f"Error: {str(e)}")
    except ValueError:
        st_code(f"Error: {ValueError}")
### EndofCodeSection###

def py_raise_try():
    width = 1
    def check_width():
        if width <= 2:
            raise Exception("Width must be greater than 2.")
    
    try:
        check_width()
    except Exception as e:
        st.error(f"Error: {str(e)}")
### EndofCodeSection###

def py_assrt():
    ages = [26,34,92]
    assert ages[0] > ages[-1], "ages list should be ascending order"
    st_code(f"No Error !")
### EndofCodeSection###