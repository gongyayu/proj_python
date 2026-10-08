import streamlit as st
import json
from typing import Dict, Any
import pprint
from py_mod import line_print, st_print, code_print, st_code, st_markline


### StartofFunc###


def py_dict():
    # initialization
    dict1 = {}

    # dictionary, keys and values
    #
    # These are all valid with Dict[str, Any]
    valid_dict: Dict[str, Any] = {         # Keys must be strings (str), Values can be anything (Any)
        "name": "Alice",                # str
        "age": 30,                      # int
        "scores": [95, 87, 92],         # list
        "active": True,                 # bool
        "metadata": {"key": "value"},   # dict
        "nothing": None                 # NoneType
    }
    code_print(f"valid_dict: {valid_dict}")
    st_markline()

    dict1['gongya'] = "Engineer"
    dict1[2] = 222
    code_print(f"dict1: {dict1}")
    code_print(f"dict1.keys(): {dict1.keys()}, list(dict1): {list(dict1)}")
    code_print(f"dict1.values(): {dict1.values()}")
    st_code(f"{code_print(f'')}")
    st_markline()

    # loop the keys
    for key in dict1.keys():
        code_print(f"key: {key}")
    st_code(f"{code_print(f'')}")
    st_markline()

    # check if the key exists
    code_print(f"'gongya' in dict1.keys(): {'gongya' in dict1.keys()}")
    code_print(f"'gongya' in dict1: {'gongya' in dict1}")
    st_code(f"{code_print(f'')}")
    st_markline()

    # get method
    try:
        val = dict1.get("gongya", "not a valid key")
        st_code(f"val: {val}")
    except Exception as e:
        st_code(f"Error: {str(e)}")
    st_markline()

    # prints both keys and values
    code_print(f"dict1.items(): {dict1.items()}")
    for key, value in dict1.items():
        code_print(f"key: {key}, value: {value}")
    st_code(f"{code_print(f'')}")

### EndofCodeSection###

def py_quizzes():
    def get_method():
        st_markline()
        order_list = [{"order_id": 1, "price": 100, "product_quantity": 1},
                    {"order_id": 2, "price": 200, "product_quantity": 3},
                    {"order_id": 3, "price": -300, "product_quantity": 6},
                    {"order_id": 4, "price": 400, "product_quantity": 2},]
        for order in order_list:
            code_print(f"order.get('order_id'): {order.get('order_id')}, order.get('price'): {order.get('price')}, order.get('product_quantity'): {order.get('product_quantity')}")
        st_code(f"{code_print(f'')}")
    get_method()   

    def demo():
        from typing import Dict, Union, TypedDict

        # More specific
        Dict[str, Union[int, str, list]]

        # Most precise - define expected structure
        class User(TypedDict):
            name: str
            age: int
            scores: list[int]
        # Then use: Dict[str, User] or just User
    
    def multivalues():
        st_markline()
        multival = {'fruits': ['apple', 'peach', 'pear'],
                    'vegetables': ['cabbage', 'carrot', 'lettuce']}
        code_print(f"multival: {multival}")
        for k in (multival.keys()):
            code_print(
                f"{str(k)} --> {multival[k][0]} --> {multival[k][1]} --> {multival[k][1]}")
        st_code(f"{code_print(f'')}")
    multivalues()

    def zip_method():
        st_markline()
        A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
        st_code(f"combine 2 lists to dictionary: -----<br> {A0}")
    zip_method()
### EndofCodeSection###

def py_dict_ops():
    dict1 = {'name': 'john', 'code': 6734,'dept': 'sales', 'major': 'Math'}

    def dict_pop():
        # return 6734
        st_code(f"dict1.pop('code'): {dict1.pop('code')}, dict1: {dict1}")
    dict_pop()

    def dict_popitem():
        st_markline()
        # return ('dept', 'sales')
        st_code(f"dict1.popitem(): {dict1.popitem()}, dict1: {dict1}")
    dict_popitem()

    def dict_clear():
        dict1 = {'name': 'john', 'code': 6734,'dept': 'sales', 'major': 'Math'}
        st_markline()
        # remove all entries
        st_code(f"dict1.clear(): {dict1.clear()}, {dict1}")
    dict_clear()

    def dict_del():
        nonlocal dict1
        st_markline()
        # delete an entry with key
        del dict1['name']
        st_code(f"del dict1('name'): {dict1}")

        # delete the entire dictionary
        del dict1
        try:
            st_code(f"dict1: {dict1}")
        except Exception as e:
            st_code(f'Error: {str(e)}')
    dict_del()

    def demo():
        import string
        st_markline()
        # list(string.ascii_lowercase)
        alphabet = list(string.ascii_lowercase)
        code_print(f"alphabet: {alphabet}")
        # list comprehension
        d = {val: idx for idx, val in enumerate(alphabet)}
        code_print(f"d: {d}")
        st_code(code_print(f''))
    demo()
### EndofCodeSection###


def py_dict_sort():
    dict1 = {'name': 'john', 'code': '6734','dept': 'sales', 'major': 'Math'}
    code_print(f"dict1: {dict1}")
    code_print(f"sorted(dict1, key=dict1.__getitem__): {sorted(dict1, key=dict1.__getitem__)}")  # sort the value and return the key
    code_print(f"sorted(dict1.values(): {sorted(dict1.values())}")
    code_print(f"sorted(dict1.keys(): {sorted(dict1.keys())}")

    # return sorted dictionary based on the key
    code_print(f"sorted(dict1.items(): {sorted(dict1.items())}")
    st_code(code_print(f''))

    # sorted dictionary
    st_markline()
    dict2 = dict(a=2, c=3, b=1)
    # x represents a single (key, value) tuple from dict2.items()
    # x[0] = the key (first element of the tuple)
    # x[1] = the value (second element of the tuple)
    dict2_sorted = {k: v for k, v in sorted(dict2.items(), key=lambda x: x[0])}                                                                           
    st_code(f"dict2: {dict2}, 'dict2_sorted: {dict2_sorted}")

    # reversed a dictionary
    st_markline()
    dict1 = {'name': 'john', 'code': '6734','dept': 'sales', 'major': 'Math'}
    # code_print(f"reversed(dict1: {dict(reversed(dict1))}")
    # code_print(f"reversed(dict1.keys()): {reversed(dict1.keys())}")
    # code_print(f"reversed(dict1.values()): {reversed(dict1.values())}")
    code_print(f"dict(reversed(dict1.items())): {dict(reversed(dict1.items()))}")
    code_print(f"sorted(dict(reversed(dict1.items()))): {sorted(dict(reversed(dict1.items())))}")
    st_code(code_print(f''))

    

    
### EndofCodeSection###


def py_dict_nested():
    def get_nested_value(data: dict, key_list: list, default=None):
        current = data
        for key in key_list:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return default
        return current
    mock_data = {"user": {"info": {"name": "zhangsan"}}}
    res1 = get_nested_value(mock_data, ["user", "info", "name"])
    res2 = get_nested_value(
        mock_data, ["user", "phone", "4254437932"], default="not found")
    st_code(f"res1: {res1}, res2: {res2}")
### EndofCodeSection###
