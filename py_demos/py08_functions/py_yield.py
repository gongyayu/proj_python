import streamlit as st
from py_mod import st_code, st_markline, st_print, line_print


### StartofFunc###

def py_yield():
    def pyfabonacci(n):
        a, b = 0, 1
        for i in range(n):
            yield a
            a, b = b, a + b
    gen = pyfabonacci(10)
    for num in gen:
        st_code(f'{num}')
### EndofCodeSection###

def py_yield_send():
    def yield_generatorA():
        yield 'A'
        yield 'B'
        st_code('End')
    genA = yield_generatorA()
    try:
        st_code(f"genA.send('hello'): {genA.send('hello')}")
    except Exception as e:
        st_code(f"Error: {str(e)}")
    st_code(f"next(genA): {next(genA)}")
    st_code(f"genA.send('hello'): {genA.send('hello')}")
    try:
        st_code(next(genA))
    except Exception as e:
        st_code(f"Error: {type(e).__name__}")
    st_markline()

    def yield_generatorB(glist: list):
        for item in glist:
            item *= item
            yield item

    genB = yield_generatorB(range(1, 10, 2))
    for each in genB:
        st_code(f'{each}')
### EndofCodeSection###


def py_yield_throw():
    def yield_throw_genA():
        try:
            yield 0 / 5
        except ValueError:
            st_code(f"Error: {ValueError}")
        yield 10 / 5
        yield 15 / 5

    genA = yield_throw_genA()
    print(next(genA))
    # get error and move to the next yield
    st_code(genA.throw(ValueError))
    st_code(f"next(gen): {next(genA)}")
    st_markline()
    # ----------------------------------------------------------

    def yield_throw_genB():
        yield 0 / 5
        yield 10 / 5

    genB = yield_throw_genB()
    st_code(f"next(genB): {next(genB)}")
    try:
        st_code(
            f"genB.throw(ValueError('wrong definition')): {genB.throw(ValueError('wrong definition'))}")
    except Exception as e:
        st_code(f"Error: {str(e)}")

    try:
        st_code(next(genB))
    except Exception as e:
        st_code(f"Error: {type(e).__name__}")
### EndofCodeSection###


def py_yield_close():
    def yield_close():
        yield 2 * 5
        yield 3 * 5

    gen = yield_close()
    st_code(f"next(gen): {next(gen)}")
    gen.close()
    try:
        st_code(f"next(gen): {next(gen)}")
    except Exception as e:
        st_code(f"Error: {type(e).__name__}")
### EndofCodeSection###


def py_chunkreader():
    def chunkreader(file_path, chunk_size=10):
        with open(file_path, 'rb') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                yield chunk

    def process_data(chunk):
        st_code(f"{chunk}")

    for chunk in chunkreader('data/in/Parsing-input.txt', chunk_size=300):
        process_data(chunk)
### EndofCodeSection###


def py_linereader():
    def linereader(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                yield line.strip()

    def process_data(line):
        st_code(f"{line}")

    for line in linereader('data/in/Parsing-input.txt'):
        process_data(line)
### EndofCodeSection###
