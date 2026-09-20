import streamlit as st
import os
import pathlib
from py_mod import line_print, st_print, st_code, code_print, st_markline
from pprint import pformat

### StartofFunc###
def py_directory():
    def pydirectory():
            import os
            # folder operation
            folder = '/users/gongya/Programming/mac_python/'
            # check if a folder exists
            if os.path.exists(folder):
                st_code(f"'{folder}' exists")
            else:
                st_code(f"{folder} does not exist")
    
    def pymkdir():
            try:
                path = os.getcwd() + '/data/out/'
                new_folder = path + 'test_folder'
                # os.makedirs('output', exist_ok=True), not to raise an exception if the directory already exists.
                os.makedirs(new_folder)
                st_code(f"successful to make a folder '{new_folder}'")
            except Exception as e:
                st_code(f"Error: {str(e)}")
    pydirectory()
    st_markline()
    pymkdir()
### EndofCodeSection###
    

def py_files():
    def pyglob():
        import glob
        from pathlib import Path
        contents = glob.glob('*.png')
        files = [file for file in contents if not os.path.isdir(file)]
        st_code(f'files: {files}, path: {Path(files[0])}, file: {files[0]}')

    def pyrename():
        # Path(file).rename(Path(new_file))
        pass
    pyglob()
### EndofCodeSection###

def py_path():
    def pydirname():
        # the directory where the current script runs
        # dirname() vs. dir() which returns a list of names (attributes and methods) of an object.
        # /Users/gongya/Programming/mac_python/proj_python/py_demos/py01_bas/py_fs.py
        st_code(f"os.path.dirname(__file__): {os.path.dirname(__file__)}")

    def pycwd():
        # the directory where the main script runs
        st_code(f"os.getcwd: {os.getcwd()}")
    pydirname()
    st_markline()
    pycwd()
### EndofCodeSection###


def py_listdir():
    entryList = []
    for entry in os.listdir():
        entryList.append(entry)
    st_code(f"os.listdir(): {os.listdir()}, \n\ndir(entry): {dir(entry)}")
### EndofCodeSection###


def py_iterdir():
    # return a list of names of the entries in the directory given by the path
    entrylist = []
    dir_path = pathlib.Path('.')   
    st_code(f"pathlib.Path('.'): {dir_path}")

    for entry in dir_path.iterdir():
        entrylist.append(entry)
    st_code(f"pathlib.path.iterdir(): {entrylist} \n\ndir(entry): {dir(entry)}")
### EndofCodeSection###

