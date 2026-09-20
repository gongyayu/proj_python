import streamlit as st
import json
from py_mod import st_code, st_print, st_code,st_markline


### StartofFunc###


def py_list():
    mylist1 = []
    mylist1a = []
    mylist2 = []
    mylist3 = []
    st_code(
        f"id(mylist1): {id(mylist1)}, id(mylist1a): {id(mylist1a)}, id(mylist2): {id(mylist2)}, id(mylist3): {id(mylist3)}")
    # initialize a list
    mylist1 = ['abcd', 786, 2.23, 'john', 70.2, 'john']
    st_code(f'mylist1: {mylist1}, type(mylist1): {type(mylist1)}')

    mylist1a = mylist1.copy()
    st_code(f"mylist1a: {mylist1a}, id(mylist1a): {id(mylist1a)}")

    mylist2 = [123, 'Tom']
    mylist3 = [int(i) for i in range(10)]
    st_code(f"mylist2: {mylist2}, mylist3: {mylist3}")
    st_print(st_code(f''))
    st_markline()

    # this following is identical. The trailing comma style is often preferred because it makes future edits cleaner.
    numbersA = [1, 2, 3]
    numbersB = [1, 2, 3,]
    st_code(f"numbersA: {numbersA}, numbersB: {numbersB}")
    st_markline()

    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    st_code(f"a.index(2): {a.index(2)}")
    st_markline()

    for idx, val in enumerate(a, 1):
        st_code(f"idx: {idx}, val: {val}")
### EndofCodeSection###


def py_list_slice():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # [0, 1]    end with index - 1
    st_code(f"a[:2]: {a[:2]}")
    # [8, 9]    start from index 8
    st_code(f"a[8:]: {a[8:]}")
    # [2, 3, 4, 5, 6, 7]
    st_code(f"a[2:8]: {a[2:8]}")
    # [2, 4, 6]
    st_code(f"a[2:8:2]: {a[2:8:2]}")                       
    # [8, 6, 4]
    st_code(f"a[-2:2:-2]: {a[-2:2:-2]}")
    sample_url = 'http://coreyms.com'
    # moc.smyeroc//:ptth
    st_code(f"{sample_url}[::-1]: {sample_url[::-1]}")
    st_code(f"{sample_url}[::-2]: {sample_url[::-2]}")
    st_code(f"{sample_url}[7:]: {sample_url[7:]}")           # coreyms.com
    st_code(f"{sample_url}[-4:]: {sample_url[-4:]}")
    st_markline()

    s = "hello_python"
    st_code(f"{s}:  {s[::-2]}")    
### EndofCodeSection###

def py_list_operate():
    listA = ['abcd', 786, 2.23, 'john', 70.2, 'apple', 'lettuce', 4]
    listB = [123, 'Tom']

    # double a list
    st_code(f"listA * 2: {listA * 2} \
            \nlistA + listB: {listA + listB}")

    del mylistA[0]
    st_code(f"del mylistA[0]: {mylistA}")
    st_code(f"mylistA.count('john'): {mylistA.count('john')}")

    mylistA.append('Tom')
    st_code(
        f"mylistA.append('Tom): {mylistA},'Tom' in mylistA: {'Tom' in mylistA}")

    st_code(f"mylistA.append((1,2)): {mylistA}")
    st_code(f"mylistA.extend((1,2)): {mylistA}")
    st_code(f"mylistA.insert(3,'example'): {mylistA}")

    st_code(f"mylistA.pop(2): {mylistA.pop(2)} -> {mylistA}")
    st_code(
        f"mylistA.remove('apple'): {mylistA.remove('apple')} -> {mylistA}")

    del mylistA
    try:
        st_code(f"del mylistA: {mylistA}")
    except Exception as e:
        st_code(f"del mylistA -> Error: {str(e)}")
    st_print(st_code(f''))
### EndofCodeSection###


def py_list_sorting():
    st_code(f"pylist_sorting() {'-' * 30}")
    mylist1 = ['abcd', 786, 2.23, 'john', 70.2, 'apple', 'lettuce', 4]
    mylist2 = [32, 12, 6, 33, 256, 123, 12]
    # list reverse
    # [:]. [0:4:2], [::-1] reverse order
    st_code(
        f"mylist1[::-1]: {mylist1[::-1]}, mylist1.reverse(): {mylist1.reverse()}")
    st_code(f"mylist2.sort(reverse=True): {mylist2.sort(reverse=True)}")

    # sorted list
    st_code(f"sorted(mylist2): {sorted(mylist2)}")
    try:
        st_code(f"sorted(mylist1): {sorted(mylist1)}")
    except Exception as e:
        st_code(f"Error: {str(e)}")
    st_print(st_code(f''))
### EndofCodeSection###


def py_list_remove_duplicated_listitems():
    st_code(f"pylist_remove_duplicated_listItem() {'-' * 30}")
    list = [2, 18, 6, 8, 8, 4, 3, 2, 8, 23, 18]
    k = {}
    dup_items = []
    for m in (list):
        if m in k.keys():
            dup_items.append(m)
            continue
        k[m] = 0
    list = k.keys()
    st_code(f"list: {list}, dup_items: {dup_items}")
    st_print(st_code(f''))
### EndofCodeSection###


def pylinked_list():
    st_code(f"pylinked_list() {'-' * 30}")

    class Node(object):
        def __init__(self, data=None, next_node=None):
            self.data = data
            self.next_node = next_node

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next_node

        def set_next(self, new_next):
            self.next_node = new_next

    class LinkedList(object):
        def __init__(self, head=None):
            self.head = head

        def insert(self, data):
            new_node = Node(data)
            new_node.set_next(self.head)
            self.head = new_node

        def size(self):
            current = self.head
            count = 0
            while current:
                count += 1
                st_code(f"current.get_data(): {current.get_data()}")
                current = current.get_next()
            st_code(f"The size of linked list is , {count}")

        def search(self, data):
            current = self.head
            found = False
            while current and found is False:
                if current.get_data == data:
                    found = True
                else:
                    current = current.get_next()
                if current is None:
                    raise ValueError("Data not in list")
                    st_code(f"def search: Data not in list")
                return found

        def delete(self, data):
            current = self.head
            precious = None
            found = False
            while current and found is False:
                if current.get_data() == data:
                    found = True
                else:
                    previous = current
                    current = current.get_next()
            if current is None:
                raise ValueError("Data not in list")
                st_code(f"def delete: Data not in list")
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.size()
    val = ll.search(1)

    if val:
        st_code(f'val: Value is Found.')
    ll.delete(1)
    ll.size()
    st_print(st_code(f''))
### EndofCodeSection###
