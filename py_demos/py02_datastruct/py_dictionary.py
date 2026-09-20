import streamlit as st
import json
from typing import Dict, Any
import pprint
from py_mod import line_print, st_print, st_code, st_markline


### StartofFunc###


def py_dictionary():
    # initialization
    dict1 = {}
    dict1['one'] = "This is one"
    dict1[2] = "This is two"
    tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
    line_print(
        f"dict1['one']: {dict1['one']}, dict1[2]: {dict1[2]}, tinydict: {tinydict}")
    line_print(f'keys -----')
    # prints all the keys
    line_print(
        f"tinydict.keys(): {tinydict.keys()}, list(tinydict): {list(tinydict)}")
    for key in tinydict.keys():
        line_print(f"key: {key}")
    line_print(f"'gongya' in tinydict: {'gongya' in tinydict}")
    try:
        tinydict.get("gongya", "no gongya")
    except Exception as e:
        line_print(f"Error: {str(e)}")

    line_print(f'values -----')
    # print all the values
    line_print(f"tinydict.values(): {tinydict.values()}")
    line_print(f'items -----')
    # prints both keys and values
    line_print(f"tinydict.items(): {tinydict.items()}")
    # john, or not a valid key
    line_print(
        f"tinydict.get('name', 'not a valid key'): {tinydict.get('name', 'not a valid key')}")

    # TypeError: 'dict' object is not callable
    d = dict(a='Africa', b='Belgium', c='Cairo', d='Detroit')
    line_print(f"{d}")
    try:
        d = dict(a=10, b=20, c=30, d=40)
        line_print(f'{d}')
    except Exception as e:
        line_print(f"Error: {str(e)}")
    st_markline()
    # get usage
    order_dict = [{"order_id": 1, "price": 100, "product_quantity": 1},
                  {"order_id": 2, "price": 200, "product_quantity": 3},
                  {"order_id": 3, "price": -300, "product_quantity": 6},
                  {"order_id": 4, "price": 400, "product_quantity": 2},]
    for order in order_dict:
        st_code(f"order.get('order_id'): {order.get('order_id')}")

    # These are all valid with Dict[str, Any]
    my_dict: Dict[str, Any] = {         # Keys must be strings (str), Values can be anything (Any)
        "name": "Alice",                # str
        "age": 30,                      # int
        "scores": [95, 87, 92],         # list
        "active": True,                 # bool
        "metadata": {"key": "value"},   # dict
        "nothing": None                 # NoneType
    }
    line_print(f"my_dict: {my_dict}")

    """
    from typing import Dict, Union, TypedDict

    # More specific
    Dict[str, Union[int, str, list]]

    # Most precise - define expected structure
    class User(TypedDict):
        name: str
        age: int
        scores: list[int]
    # Then use: Dict[str, User] or just User
    """
    line_print(f"multivalues -----")
    multival = {'fruits': ['apple', 'peach', 'pear'],
                'vegetables': ['cabbage', 'carrot', 'lettuce']}
    line_print(f"multival: {multival}")
    for k in (multival.keys()):
        line_print(
            f"{str(k)} --> {multival[k][0]} --> {multival[k][1]} --> {multival[k][1]}")

    A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
    line_print(f"combine 2 lists to dictionary: -----<br> {A0}")
    st_print(line_print(f''))
### EndofCodeSection###


def py_dictionary_operations():
    import string
    tinydict = {'name': 'john', 'code': 6734,
                'dept': 'sales', 'major': 'Math'}
    line_print(f"pydictionary_operations() {'-' * 30}")
    line_print(
        f"'codex' in reversed(sorted(tinydict.keys())): {'codex' in reversed(sorted(tinydict.keys()))}")
    line_print(f"del, pop, popitem, clear -----")
    # delete an entry with key
    del tinydict['name']
    line_print(f"del tinydict('name'): {tinydict}")
    # return 6734
    line_print(
        f"tinydict.pop('code'): {tinydict.pop('code')}, tinydict: {tinydict}")
    # return ('dept', 'sales')
    line_print(
        f"tinydict.popitem(): {tinydict.popitem()}, tinydict: {tinydict}")

    # remove all entries
    tinydict.clear()
    line_print(f"tinydict: {tinydict}")
    # delete the entire dictionary
    del tinydict
    try:
        line_print(f"tinydict: {tinydict}")
    except Exception as e:
        line_print(f'Error: {str(e)}')

    # list(string.ascii_lowercase)
    line_print(f"list(string.ascii_lowercase) -----")
    alphabet = list(string.ascii_lowercase)
    line_print(f"alphabet: {alphabet}")
    # list comprehension
    d = {val: idx for idx, val in enumerate(alphabet)}
    line_print(f"d: {d}")
    st_print(line_print(f''))
### EndofCodeSection###


def py_dictionary_sorting():
    # sorted dictionary
    line_print(f"pydictionary_sorting() {'-' * 30}")
    mydict = dict(a=1, b=3, c=2)
    mydict_sorted = {k: v for k, v in sorted(
        mydict.items(), key=lambda x: x[1])}
    line_print(f"mydict: {mydict}, 'mydict_sorted: {mydict_sorted}")

    str_data = {'name': 'john', 'code': '6734', 'dept': 'sales'}
    line_print(f"str_data: {str_data}")
    line_print(
        f"sorted(str_data, key=str_data.__getitem__): {sorted(str_data, key=str_data.__getitem__)}")
    line_print(f"sorted(str_data.values(): {sorted(str_data.values())}")
    line_print(f"sorted(str_data.keys(): {sorted(str_data.keys())}")
    # return sorted dictionary based on the key
    line_print(f"sorted(str_data.items(): {sorted(str_data.items())}")
    st_print(line_print(f''))
### EndofCodeSection###


def py_getnesteddict():
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
