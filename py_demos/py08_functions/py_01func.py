import streamlit as st
from py_mod import st_code, line_print, st_markline, code_print, outlines

### StartofFunc###

def py_zip():
    def pyzipA():
        names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
        heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
        universes = ['Marvel', 'DC', 'Marvel', 'DC']

        for index, name in enumerate(names):
            hero = heroes[index]
            code_print(f'{name} is actually {hero}')
        st_code(f'{code_print(f'')}')
        st_markline()

        for name, hero, universe in zip(names, heroes, universes):
            code_print(f'{name} is actually {hero} from {universe}')
        st_code(f'{code_print(f'')}')
        st_markline()

        for value in zip(names, heroes, universes):
            code_print(f"value: {value}")
        st_code(f'{code_print(f'')}')
    pyzipA()
    st_markline()

    def pyzipB():
        a = [1,2,3,4]
        b = [4,5]

        result = []
        for x,y in zip(a,b):
            result.append(x+y)
        st_code(f'result: {result}')
    pyzipB()
### EndofCodeSection###


def py_map():
    # Apply a function to each item of an iterable (or iterables) and return the results.
    def add_three(x):
        return x + 3

    li = [1, 2, 3]
    st_code(f"{[i for i in map(add_three, li)]}")
    st_code(f"{list(map(add_three, li))}")
### EndofCodeSection###


def py_range():
    st_code(f"{[i for i in range(10)]}")  # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    st_code(f"{[i for i in range(2, 10)]}")  # => [2, 3, 4, 5, 6, 7, 8, 9]
    st_code(f"{[i for i in range(2, 10, 2)]}")  # => [2, 4, 6, 8]
    st_code(f"{list(range(2, 10, 2))}")  # => [2, 4, 6, 8]

    for i in list(range(1, 10, 2))+[50]:
        st_code(f"{i}")
### EndofCodeSection###

def py_filter():
    def add_three(x):
        if x % 2 == 0:
            return True
        else:
            return False

    def pyfilter():
        li = [1, 2, 3, 4, 5, 6, 7, 8]
        # filter(function, iterable) [2, 4, 6, 8]
        st_code(f"{[i for i in filter(add_three, li)]}")
    pyfilter()
### EndofCodeSection###


def py_isinstance():
    mylist = [{'a': 1}, {'b': 2}, {'c': 3},]
    try:
        st_code(
            f'isinstance(mylist,list): {isinstance(mylist, list)} -> {mylist}')
        st_code(
            f'isinstance(mylist,str): {isinstance(mylist, str)} -> {mylist}')
    except Exception as e:
        print(1, f'Error: {str(e)}')

    for idx, item in enumerate(mylist, 1):
        try:
            isinstance(item, dict)
            for key in item.keys():
                st_code(f'key:{key} -> {item.get(key, 'no key')}')
        except Exception as e:
            st_code(f'Error: {str(e)}')
### EndofCodeSection###


def py_dir():
    #
    # The dir() function returns a list of names (attributes and methods) of an object.
    #
    st_code(f"dir('Hello': {dir("hello")}")
    st_code(f"dir([1,2,3]): {dir([1, 2, 3])}")
### EndofCodeSection###


def py_any():
    def any_demo1():
        a = [False, False, False]
        b = [True, False, False]
        c = [True, True, True]
        st_code(f"any(a): {any(a)},any(b): {any(b)},any(c): {any(c)}")
    any_demo1()

    def any_demo2():
        words = ["apple", "banana", "grape", "orange"]
        has_an = any("an" in word for word in words)
        # True (banana has 'an')
        st_code(f"has_an: {has_an}")
    any_demo2()
### EndofCodeSection###


def py_join():
    def pyjoinA():
        words = ["Hello", "World", "Python"]
        result = " ".join(words)
        st_code(f"pyjoinA():\nresult: {result}")
    pyjoinA()

    def pyjoinB():
            retrieved = [('Python is a high-level programming language created by Guido van Rossum in 1991.', 0.746315062046051), 
                         ('RAG stands for Retrieval-Augmented Generation, combining a retriever with a language model.', 0.1926918625831604),
                        ]
            context = "\n".join(f"- {doc}" for doc, _ in retrieved)
            st.code(f"pyjoinB():\n{context}")
    pyjoinB()
    
    def pystrjoin():
        s1 = "hello"
        s2 = '-'.join(s1)
        st_code(f"pyjoinC():\ns2: {s2}")
    pystrjoin()

    
### EndofCodeSection###

def py_repr():
    # the repr() function is a built-in function that returns a string representation of an object. This string is often used for debugging and logging purposes, 
    # and it's also used by the print() function when you use the !r or !R
    text = "Hello\nWorld"

    text = "Hello\nWorld"

    code_print(f"str(text): {str(text)}")
    # Output:
    # Hello
    # World
    code_print(f"repr(text): {repr(text)}")
    # Output: 'Hello\nWorld'
    
    code_print(f"{'-' * 30}")
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __repr__(self):
            return f"Person(name={self.name!r}, age={self.age!r})"

    p = Person("Alice", 30)
    code_print(f"repr(p): {repr(p)}")
    # Output: Person(name='Alice', age=30)
    st_code(code_print(f''))
### EndofCodeSection###




