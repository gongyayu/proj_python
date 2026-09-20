import streamlit as st
from py_mod import line_print, st_code, st_print

### StartofFunc###


def py_returnsinglevalue():
    def single_return(fname, lname):
        return f'hello {fname} {lname}'
    st_code(f"single return: {single_return('gongya', 'yu')}")

    def return_int() -> int:
        return 10
    st_code(f"return_int(): {return_int()}")
### EndofCodeSection###


def py_returnmultivalues():
    def returnmultivaluesA() -> tuple[str, list]:
        mylist = [1, 2, 3, 4]
        return f'Hello world!', f'{mylist}'
    st_code(f'{returnmultivaluesA()}')

    def returnmultivaluesB():
        name = 'Tom'
        welcome = f'hello {name}'
        leave = f'goodbye {name}'
        future = f'come again {name}'
        # response = retMultiple() welcome=response[0], leave=response[1] ..
        return welcome, leave, future
    response = returnmultivaluesB()
    st_code(
        f"response: {response}, \nresponse[0]: {response[0]}, response[1]: {response[1]}, response[2]: {response[2]} ")

    welcome, leave, future = returnmultivaluesB()
    st_code(f"welcome: {welcome},leave: {leave},future: {future}")
### EndofCodeSection###


def py_returnloop():
    def returnloop():
        tool_list = ['hammer', 'spade', 'knife', 'saw']
        return [
            {
                "type": "function",
                "function": {
                    "name": tool,
                    "description": "tool.description",
                    "parameters": "tool.inputSchema",
                },
            }
            for tool in tool_list
        ]
    st_code(f"returnloop(): {returnloop()}")
### EndofCodeSection###


def py_input_simple():
    def increment(number, by):
        return (number, number + by)
    st_code(f"increment: {increment(2, by=3)}")

    def incrementwithDefault(number, by=1):                                     # by=1 is default
        return (number, number + by)
    st_code(f"incrementwithDefault: {incrementwithDefault(2)}")

    def incrementByInt(number: int, by: int = 1) -> tuple:                      # parameter with default value must be the last
        return (number, number + by)
    st_code(f"incrementByInt: {incrementByInt(3)}")
### EndofCodeSection###


def py_input_list():
    def multiply(list):
        total = 1
        for number in list:
            total *= number
        return total
    st_code(f"multiply: {multiply([1, 2, 3])}")
### EndofCodeSection###


def py_input_bystar():
    # This operator takes the list elements and passes them as separate arguments to the function.
    def multiply(*list):
        total = 1
        for number in list:
            total *= number
        return total
    st_code(f"multiply: {multiply(1, 2, 3)}")

    def save_user(**user):                                         # pass in a tuple
        st_code(
            f"user: {user}, user('id'): {user['id']}, user['name']: {user['name']}")
    save_user(id=1, name="admin")
### EndofCodeSection###
