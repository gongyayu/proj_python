import streamlit as st
from py_mod import st_code, line_print, st_markline, st_code, outlines

### StartofFunc###


def py_enumerate():
    names = ['Corey', 'Chris', 'Dave', 'Travis',]
    for index, name in enumerate(names, start=1):
        st_code(f"index: {index}, name: {name}")
    st_markline()
    # Python program to illustrate enumerate function
    l1 = ["eat", "sleep", "repeat"]
    s1 = "geek"

    # creating enumerate objects
    obj1 = enumerate(l1)
    obj2 = enumerate(s1)
    st_code(f"enumerate(l1): {enumerate(l1)}")
    st_code(f"Return type for enumerate(l1): {type(enumerate(l1))}")
    st_code(f"list(enumerate(l1)): {list(enumerate(l1))}")

    # changing start index to 2 from 0
    st_code(f"list(enumerate(s1,2)): {list(enumerate(s1, 2))}")

    # printing the tuples in object directly
    for element in enumerate(l1):
        st_code(f"element: {element}")
    # changing index and printing separately
    for count, element in enumerate(l1, 100):
        st_code(f"count: {count}, element: {element}")
### EndofCodeSection###


def py_zip():
    names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
    heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
    universes = ['Marvel', 'DC', 'Marvel', 'DC']

    for index, name in enumerate(names):
        hero = heroes[index]
        st_code(f'{name} is actually {hero}')
    for name, hero, universe in zip(names, heroes, universes):
        st_code(f'{name} is actually {hero} from {universe}')
    for value in zip(names, heroes, universes):
        st_code(f"value: {value}")
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
    def pyjoin():
        words = ["Hello", "World", "Python"]
        result = " ".join(words)
        st_code(f"result: {result}")
    pyjoin()
    st_markline()
    
    def pystrjoin():
        s1 = "hello"
        s2 = '-'.join(s1)
        st_code(F"s2: {s2}")
    pystrjoin()
### EndofCodeSection###
