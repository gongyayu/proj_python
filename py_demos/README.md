Readme for this project

Goal: To pile what you need during your python programming for quick references

Usages:
    1. for each topic, create a folder named pyXX_XXXXXX 
    2. for each subtopic, create a .py module file inside the topic folder.
    3. Inside the .py file, pile your functions related to that subtopic.
       Note for functions
       A. Inside .py file, add "### StartofFunc###" before you add the first function
       B. A function prefixed with 'py_' will be executed in addition to be displayed, otherwise, a function is only displayed.
       C. A function to be executed can't accept input parameters, if you need any input parameters, wrap that function inside a function without any parameters
       D. Each top level function should be ended with "### EndofCodeSection###" as function terminator for parsing purpose
    4. Only 2 main files for this project to run
       1. py_main.py creats GUI using streamlit
       2. py_mod.py tracks all the folders, modules and executes functions
