from py_mod import line_print, st_print, code_print, st_code, st_markline

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

def py_quizzes():
    def quiz1():
        num = [10,20,30]
        for index, value in enumerate(num, start=1):
            code_print(f"index + value: {index + value}")
        st_code(f"{code_print(f'')}")
    quiz1()
### EndofCodeSection###