import streamlit as st
from py_mod import line_print, st_print

### StartofFunc###


def py_for():
    # loop
    names = ['Corey', 'Chris', 'Dave', 'Travis']
    for index, name in enumerate(names):
        st.code(f"index {index}: name {name}")
    st.markdown('---')
    for index, name in enumerate(names, start=1):
        st.code(f"index {index}: name {name}")

    st.markdown('---')
    nameList = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruse Wayne']
    heroList = ['Spiderman', 'superman', 'Deadpool', 'Batman']
    universeList = ['Marvel', 'DC', 'Marvel', 'DC']

    for name, hero, universe in zip(nameList, heroList, universeList):
        st.code(f'{name} is actually {hero} from {universe}')

    for value in zip(nameList, heroList, universeList):
        st.code('value: %s ' % str(value))

    st.markdown('---')
    for x in range(0, 10, 2):
        # [0,2,4,6,8]
        st.code(x)

    st.markdown('---')
    # break
    names = ["AJohn", "Mary", "John"]
    for name in names:
        if name.startswith("J"):
            st.code("found")
            break
        else:
            st.code("Not found")

    st.markdown('---')
    names = ["AJohn", "Mary", "John"]
    for name in names:
        if name == 'Mary':
            continue
            pass
        st.code(name)

    st.markdown('---')
    for name in names:
        if name == 'Mary':
            pass
        st.code(name)

### EndofCodeSection###


def py_while():
    var = 10                    # Second Example
    while var > 0:
        var -= 1
        st.code(f"Current variable value : {var}")
### EndofCodeSection###
