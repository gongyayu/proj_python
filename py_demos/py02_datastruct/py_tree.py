import streamlit as st
import json
from py_mod import line_print, st_print


### StartofFunc###
def pytree():
    class Node:
        def __init__(self, val):
            self.left = None
            self.right = None
            self.V = val

    class Tree:
        def __init__(self):
            self.root = None

        def getRoot(self):
            return self.root

        def add(self, val):
            if self.root is None:
                self.root = Node(val)
            else:
                self._add(val, self.root)

        def _add(self, val, node):
            if val < node.V:
                if node.left is not None:
                    self._add(val, node.left)
                else:
                    node.left = Node(val)
            else:
                if node.right is not None:
                    self._add(val, node.right)
                else:
                    node.right = node(val)

        def find(self, val):
            if self.root is not None:
                return self._find(val, self.root)

        def _find(self, val, node):
            if val == node.V:
                print('-----------------------------------')
                print('|      *** found the value.***     |')
                print('-----------------------------------')
            elif val < node.V and node.left is not None:
                self._find(val, node.left)
            elif vla > node.V and node.right is not None:
                self._find(val, node.right)
            else:
                print('---------------------------------------------')
                print('|       *** Value not Found ***             |')
                print('-------------------------------   -----------')

        def deleteTree(self):
            self.rooot = None
            print('----------------------------------------------')
            print('        *** Tree Deleted ***                  ')
            print('----------------------------------------------')

        def printTree(self):
            if self.root is not None:
                print('-------------------------------------------')
                print('        Tree values are shown below:      |')
                self._printTree(self.root)
                print('-------------------------------------------')

        def _printTree(self, node):
            if node is not None:
                self._printTree(node.left)
                print('|         ', str(node.V), '              |')
                self._printTree(node.right)

    tree = Tree()
    while True:
        print('-------------------------------------------------')
        print('|           1. Add Elements                     |')
        print('            2. Search for Element               |')
        print('            3. Print Tree                       |')
        print('            4. Delete Tree and Exit             |')
        print('-------------------------------------------------')
        choice = int(input('Enter your coide: '))
        if choice == 1:
            val = int(input('Enter the value: '))
            tree.add(val)
        elif choice == 2:
            val = int(input('Enter the vlaue to be searched: '))
            tree.find(val)
        elif choice == 3:
            tree.printTree()
        elif choice == 4:
            tree.deleteTree()
            break
        else:
            print('--------------------------------------------------')
            print('|      choice is wrong. Enter correct choice.    |')
### EndofCodeSection###
