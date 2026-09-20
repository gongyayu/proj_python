import streamlit as st
from py_mod import st_code, st_markline, st_print, line_print

### StartofFunc###

def py_lambda():
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, numbers))
    # Output: [1, 4, 9, 16, 25]
    st_code(f"{squared}")

    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    even = list(filter(lambda x: x % 2 == 0, numbers))
    # Output: [2, 4, 6, 8]
    st_code(f"{even}")

    students = [
        {'name': 'Alice', 'grade': 85},
        {'name': 'Bob', 'grade': 92},
        {'name': 'Charlie', 'grade': 78}
    ]
    sorted_students = sorted(students, key=lambda x: x['grade'])
    st_code(f"{sorted_students}")

    squares = [x**2 for x in range(10)]
    st_code(f"squares: {squares}")
    squares = list(map(lambda x: x**2, range(10)))
    st_code(f"squares: {squares}")
### EndofCodeSection###