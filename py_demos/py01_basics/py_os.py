# import py_mod
import streamlit as st
import os
import pathlib
from py_mod import line_print, st_print, st_code, code_print, st_markline

### StartofFunc###
### Section: OS and Memory ###


def py_env():
    import os
    from dotenv import load_dotenv

    # Load the .env file
    load_dotenv()                            # or load_dotenv("folder/.env")

    idx = 1
    '''
    # MAC/Linux
      export API_KEY=sk-1234567890abcdef
    # wins
      set API_KEY=sk-1234567890abcdef
    '''
    #
    # Method 1: Get with default
    #
    try:
        # return None (or default)
        api_key = os.environ.get('API_KEY', 'default-key')
        line_print(f'Method 1: api_key -> {api_key}')
    except Exception as e:
        err = str(e)
        line_print(f'Method 1: Error -> {err}')
    #
    # Method 2: Check if exists
    #
    if 'API_KEY' in os.environ:
        api_key = os.environ['API_KEY']                       # raise KeyError
        line_print(f"Method 2: API_KEY -> {api_key}")
    #
    # Method 3: Will crash if not found
    #
    try:
        # KeyError if missing!
        api_key = os.environ['API_KEY']
        line_print(f'Method 3: API_KEY -> {api_key}')
    except Exception as e:                                   # KeyError:
        line_print(f'Method 3: Error -> {str(e)}')
    st_print(line_print(''))
### EndofCodeSection###

def py_sys_call():
    def os_call():
        import os
        import subprocess
        line_print(f'def py_sys_call() {'-' * 30}')
        IP = '192.168.1.200'
        try:
            # deprecated
            os.system(f'ping -c 1 -t 1 {IP}')
            line_print(f'successful to ping {IP}')
        except Exception as e:
            line_print(f'Error: {str(e)}')

        ret = os.popen(f'ping -c 1 -t 1 {IP}').read()              # deprecated
        for line in ret.splitlines():
            line_print(line)
        st_print(line_print(''))
    os_call()

    def pyping():
        import os
        command = 'ping -c 1'

        hosts = ['192.168.1.200', '192.168.1.201', '127.0.0.1']
        while True:
            page = '''
               <meta http-equiv="refresh" content="5">
               <h1>Up/Down Dashboard</h1> 
               '''
            for site in hosts:
                response = os.popen(f'{command} {site}').read()
                page += f'<pre>{response}</pre>'
            with open('dashboard.htm', 'w') as file:
                file.write(page)

    def subprocess_call():
        import subprocess
        line_print(f'def subprocess_call() {'-' * 30}')
        IP = '192.168.1.200'
        subprocess.call(f'ping -c 2 -t 1 {IP}', shell=True)

        # for real time streaming output, subprocess.run() waits until the command finishes. For long-running commands(like ollama, servers, AL agents), use popen
        process = subprocess.Popen(["ollama", "list"],            # subprocess.Popen(["ping","google.com"],
                                   stdout=subprocess.PIPE,
                                   text=True)
        ln = ''
        for line in process.stdout:
            ln += line
        line_print(f'{ln}')

        # subprocess.run us better for short commands like git, ls or file operation
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True
        )
        line_print(result.stdout)
        st_print(line_print(''))
    subprocess_call()
### EndofCodeSection###


def py_memory_location():
    def memory_location(str1):
        line_print(f"{str1} -> memory location: {id(str1)}")  # => 4353702856
        str2 = str1  # new name, same object
        # => 4353702856    still the original object
        line_print(f"{str2} -> memory location: {id(str2)}")

        # creates a new name (with same name as the first) AND object
        str1 += 's'
        line_print(f"{str1} -> memory location: {id(str1)}")  # => 4387143328
    memory_location('gongya')
    st_print(line_print(''))
### EndofCodeSection###


def py_memory_mgmt():
    x = 'some text'
    line_print(f"x -> memory location: {id(x)}")
    y = x
    line_print(
        f"x -> memory location: {id(x)},'  y -> memory location: {id(y)}")

    if y is x:
        line_print(
            f"x -> memory location{id(x)}, y -> memory location: {id(y)}")

    def add_chars(text: str):
        text += text
        return text

    name = 'text'
    line_print(f"name -> memory location: {id(name)}")
    line_print(f"{add_chars(name)} -> memory location: {id(add_chars(name))}")

    value = 5                                                # immutable
    line_print(f"{value} -> memory location: {id(value)}")
    value += 1
    line_print(f"{value} -> memory location: {id(value)}")
    value -= 1
    line_print(f"{value} -> memory location: {id(value)}")
    value -= 1
    line_print(f"{value} -> memory location: {id(value)}")

    y = [1, 2, 3]                                             # mutable
    line_print(f"y -> {id(y)}")
    y.append(4)
    line_print(f'y -> {id(y)}')
    st_print(line_print(''))
### EndofCodeSection###


def py_memory_demo1():
    # is and ==
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
    st.code(
        f"a -> memory location: {id(a)}, b -> memory location: {id(b)}, c -> memory location: {id(c)}, \
            \na==b: {a == b}, a == c: {a == c}, a is b: {a is b}, a is c: {a is c}", language="python", width="content")
    b.append(4)
    st.code(f"after b.append(4) -> a: {a}, b: {b}")
### EndofCodeSection###


def py_memory_dup():
    #
    #   reference the original object
    #
    code_print(f"reference the original object: ---")
    li1 = [['a'], ['b'], ['c']]
    code_print(f"li1 -> memory location: {id(li1)}")
    li2 = li1
    code_print(f"li2 -> memory location: {id(li2)}")
    li1.append(['d'])
    code_print(
        f"li1 ({li1}) -> memory location: {id(li1)}, li2 ({li2}) -> memory location: {id(li2)}")
    st_code(f"{code_print(f'')}")
### EndofCodeSection###

def py_memory_shallowcopy():
    import copy
    #
    # Create a shallow copy of the original
    #
    code_print(f"create a shallow copy of the original (opt 1): ---")
    li3 = [['a'], ['b'], ['c']]
    li4 = list(li3)                                               # vs. li4 = li3
    code_print(f"li3: {id(li3)} - {li3}, li4: {id(li4)} - {li4}")
    li3.append([4])
    code_print(f"li3: {id(li3)} - {li3}, li4: {id(li4)} - {li4}")
    li3[0][0] = ['3']
    code_print(f"li3: {id(li3)} - {li3}, li4: {id(li4)} - {li4}")
    li4[1][0] = ['4']
    code_print(f"li3: {id(li3)} - {li3}, li4: {id(li4)} - {li4}")

    #
    # via copy routine
    #
    code_print(f"\ncreate a shallow copy of the original (opt 1): ---")
    original = ['a',[1, 2, 3], [4, 5, 6]]
    #shallow = copy.copy(original)
    shallow = original.copy()
    code_print(f"original: {id(original)} - {original}, shallow: {id(shallow)} - {shallow}")

    original.append(['a', 'b', 'c'])                                                           # the outer list not affect each other
    shallow.append([7, 8, 9])
    code_print(f"original: {id(original)} - {original}, shallow: {id(shallow)} - {shallow}")

    original[1][1] = ['b']                                                                     # the inner list affects each other
    code_print(f"original: {id(original)} - {original}, shallow: {id(shallow)} - {shallow}")
    shallow[1][0] = ['a']
    code_print(f"original: {id(original)} - {original}, shallow: {id(shallow)} - {shallow}")

    original[0] = ['x']                                                                     # the inner list affects each other
    code_print(f"original: {id(original)} - {original}, shallow: {id(shallow)} - {shallow}")
    shallow[0] = ['y']
    code_print(f"original: {id(original)} - {original}, shallow: {id(shallow)} - {shallow}")
   
    st_code(f"{code_print(f'')}")

    def quiz_1():
        a = [1,2]
        b = a
        c = a.copy()
        a[0] = 99
        st_code(f"a: {a}, b: {b}, c: {c}")
    quiz_1()
### EndofCodeSection###

def py_memory_deepcopy():
    import copy
    li5 = [['a'], ['b'], ['c']]
    li6 = copy.deepcopy(li5)
    code_print(f"li5: {id(li5)} - {li5}, li6: {id(li6)} - {li6}")

    li5.append([4])
    code_print(f"li5: {id(li5)} - {li5}, li6: {id(li6)} - {li6}")

    # nested
    li5[0][0] = ['X']
    li6[0][0] = ['Y']
    code_print(f"li5: {id(li5)} - {li5}, li6: {id(li6)} - {li6}")
    st_code(f"{code_print(f'')}")
### EndofCodeSection###
