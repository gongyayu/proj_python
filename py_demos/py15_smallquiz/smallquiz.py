import streamlit as st
from py_mod import line_print, st_print, st_code, code_print,st_markline

### StartofFunc###


def py_map():
    m = map(str, [1, 2, 3])
    a = list(m)
    b = list(m)
    st_code(f"len(a): {len(a)}, len(b): {len(b)}")
### EndofCodeSection###

def py_errors():
    def func_return():
        try:
            return 1
        finally:
            try: 
                return 2      # A "return" cannot be used to exit a "finally" block
            except Exception as e:
                st_code(f"Error: {str(e)}")
    func_return()
    #---------------------------------------------------------------------------
    def typemismatch():
        char = 'A'
        num = 3
        for i in range(num):
            st_code(f"{char} + {i} = {chr(ord(char) + i)}")

        try:
            x = "2" + 3
            st_code(f"x: {x}")
        except TypeError as e:
            st_code(f"Error: {e}")
    typemismatch()
### EndofCodeSection###


def py_num():
    def floating_point():
        st_code(f"0.2 + 0.3 == 0.5: {0.2 + 0.3 == 0.5}")
        st_code(f"0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")
    floating_point()
### EndofCodeSection###


def py_calculateA():
    s = 0
    for i in range(1, 7):
        if i == 3 or i == 5:
            continue
        if i * s > 28:
            break
        s += i
        st_code(f"i: {i}, s: {s}")
    st_code(f"s: {s}")
### EndofCodeSection###


def py_bool():
    st_code(
        f"True + True: {True + True}, False: {False}, True * False: {True * False}")
    st_code(f"True + True * False: {True + True * False}")
### EndofCodeSection###

def py_unpacklist():
    a, *b, c = [1, 2, 3, 4, 5]              # list
    st_code(f"b: {b}")

    a, *b, c = (1, 2, 3, 4, 5)              # tuple
    st_code(f"b: {b}")
### EndofCodeSection###


def py_mem():
    a = [[5]] * 3
    st_code(f"a: {a}, [{id(a[0][0])}],[{id(a[1][0])}],[{id(a[2][0])}]")
    a[0][0] = 7
    st_code(f"a: {a}, [{id(a[0][0])}],[{id(a[1][0])}],[{id(a[2][0])}]")
### EndofCodeSection###


def py_yield():
    def yield_quizA():
        yield 1
        yield 2
        yield 3
    g = yield_quizA()
    try:
        st_code(list(g))
    except Exception as e:
        st_code(f"Error: {TypeError(e).__name__}")
    st_markline()

    def yield_quizB():
        yield 1
        yield 2
        yield 3
    g = yield_quizB()
    next(g)
    st_code(list(g))
    st_markline()

    def yield_quizC():
        yield 10 / 5
        yield 0 / 5  # . why not error here
        yield 15 / 5
    g = yield_quizC()
    next(g)
    st_code(list(g))
    # try:
    # st_code(list(g))
    # except Exception as e:
    # st_code(f"Error: {str(e)}")
### EndofCodeSection###


def py_onelinecode():
    # find non duplicated item via a single line code

    my_list = [1, 2, 2, 3, 4, 4, 5]
    # st_code(f"my_list=[1,2,2,3,4,4,5]: {list(dict.fromkeys(my_list))}")
    st_code(
        f"{[x for x in [1, 2, 2, 3, 4, 4, 5] if [1, 2, 2, 3, 4, 4, 5].count(x) == 1]}")

### EndofCodeSection###


def py_lambda():
    def lambda01():
        funcs = []
        for i in range(3):
            func = lambda x: x + i               # late binding. In Python, a lambda (or any nested function) captures variables by reference, not by value. 
            funcs.append(func)
        run = [f(1) for f in funcs]
        st_code(f"{run}")
    lambda01()
    st_markline()

    def lambda02():
        funcs = []
        for i in range(3):
            func = lambda x, i=i: x + i           # bind the value instead of the references
            funcs.append(func)
        run = [f(1) for f in funcs]
        st_code(f"{run}")
    lambda02()
### EndofCodeSection###

def py_datatype():
    def datatype01():
        a = {x: x**2 for x in range(30)}
        b = {x**2 for x in range(3)}
        st_code(f"a: {type(a)}, b: {type(b)}")
    datatype01()
### EndofCodeSection###

def py_listquizes():
    def listpop():
        x = [1,2,3]
        st_code(f"x.pop(), x: {x.pop(),x}")
    listpop()
    st_markline()

    def listsliceA():
        a = [1, 2, 3]
        a[::-1] = a
        st_code(f"a: {a}")
    listsliceA()
    st_markline()

    def listsliceB():
        a = [1,2,3,4]
        a[1:3] = [8]
        st_code(f"a: {a}")
    listsliceB()
    st_markline()
    
    def listinitializedA(x, y=[]):           # y is only initialized once, dict is the same, not other variables
        y.append(x)
        return y
    for i in range(1,4):
        code_print(f"listinitializedA(i): {listinitializedA(i)}")
    st_code(code_print(''))

    def listinitializedB(x, y=None):           # y is only initialized once, dict is the same, not other variables
        if y == None:
            y = []
        y.append(x)
        return y
    for i in range(1,4):
        code_print(f"listinitializedB(i): {listinitializedB(i)}")
    st_code(code_print(''))   
### EndofCodeSection###

def py_fstr():
    num = 255
    s1 = f"{num:x}"
    s2 = f"{num:X}"
    st_code(f"s1: {s1}, s2: {s2}")
### EndofCodeSection###

def py_while_else():
    n = 3
    while n > 0:
        n -= 1
    else:
        code_print(f"done")
    st_code(f"{code_print(f'')}{n}")
### EndofCodeSection###



