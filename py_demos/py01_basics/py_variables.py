from py_mod import line_print,st_print,st_code,code_print,codelines

### StartofFunc###
def py_string():
    import string

    str = 'Hello World!'
    # Prints complete string
    line_print(f"str -> {str}")
    # Prints first character of the string
    line_print(f"str[0] - > {str[0]}")
    # Prints characters starting from 3rd to 5th
    line_print(f"str[2:5] -> {str[2:5]}")
    # Prints string starting from 3rd character
    line_print(f"str[2:] -> {str[2:]}")
    # update a string
    line_print(f"str[:6] + 'Python' ->  {str[:6] + 'Python'}")
    # Prints string two times
    line_print(f"str * 2 -> {str * 2}")
    # Prints concatenated string
    line_print(f"str + 'TEST' -> {str + 'TEST'}")
    line_print(f"'-' * 12 -> {'-' * 12}")

    # string function
    str = '   Hello World!'
    line_print(f'len(str) -> {len(str)}')
    line_print(f"str.upper() -> {str.lower()}")
    # strip all the white spaces from bother ends
    line_print(f"str.strip() -> {str.strip()}")
    line_print(f"str.find('wor') -> {str.find('wor')}")
    line_print(f"str.replace('W', '-') -> {str.replace('W', '-')}")
    line_print(f"str.split() -> {str.split()}")
    line_print(f"'Wor' in str -> {'Wor' in str}")
    line_print(f"'Wor' not in str -> {'Wor' not in str}")
    st_print(line_print(f''))
### EndofCodeSection###

def py_number():
    lp = '720'
    line_print(f"int(lp) / 500 -> {int(lp) / 500}")

    x1 = 10
    x2 = -10
    y = 0b10
    z = 0x12c

    line_print(f"x1={x1}, x2={x2}, y={y}, z={z}")
    line_print(
        f"bin(x1) -> {bin(x1)}, hex(x1) -> {hex(x1)}, abs(x1) -> {abs(x1)}, abs(x2) -> {abs(x2)}")

    # complex number
    import math
    line_print(f"1 + 2j -> {1 + 2j}")

    # print out 3.33333333335
    line_print(f"10 / 3 -> {10/3}")
    # print out 3
    line_print(f"10 // 3 -> {10 // 3}")
    line_print(f"10 % 3 -> {10 % 3}")
    line_print(f"10 ** 3 -> {10 ** 3}")

    x = 2
    x += 1
    line_print(f"x += 1 -> {x}")

    # constant
    pi = 3.14
    PI = 3.14
    line_print(f"pi = {pi}, PI = {PI}")

    line_print(f"math.floor(PI) -> {math.floor(PI)}")
    st_print(line_print(f''))
### EndofCodeSection###

def py_booltype():
    # False: "" for empty,0,[],None(null)
    st_code(
        f"{bool("")},' ',{bool(0)},' ',{bool([])},' ',{bool(-1)},' ',{bool(1)},' ',{bool("False")}")
### EndofCodeSection###


def py_unpacking():
    a, b = (1, 2)
    st_code(f"a: {a},b: {b}")
    a, _ = (1, 2)
    st_code(f"a: {a}")

    # *_ to skip all the 3,4,5  *c, d   *_,d
    a, b, *c = (1, 2, 3, 4, 5)
    st_code(f"a: {a},b: {b},c: {c}")                   # c = [3,4,5]

    a, b, *_ = (1, 2, 3, 4, 5)                         # not use 3,4,5
    st_code(f"a: {a}, b: {b}")
    
    a, b, *c, d = (1, 2, 3, 4, 5, 6, 7)
    st_code(f"a: {a}, b: {b}, c: {c}, d: {d}")
    
    a, b, *c_, d = (1, 2, 3, 4, 5, 6, 7)               # not use 3,4,5,6
    st_code(f"a: {a}, b: {b}, c: {c}, d: {d}")
### EndofCodeSection###

def py_scope():
    a = 0
    def local_scope():
        a = 10
    local_scope()
    st_code(f"a: {a}")

    def global_scopeA():
        global a                                       # no update for py_scope level
        global codelines                               # module level

        codelines = f"hello world!"
        a = 20
    global_scopeA()

    def global_scopeB():
        discount = 10

        def py_discount():
            print(discount)                           # discount 10
        discount += 10
        print (discount)                              # discount 20

    def nonlocal_scope():
        nonlocal a                                    # update a in py_scope level
        global codelines 
        codelines += " gongya"
        a = 10
    nonlocal_scope()
    st_code(f"a: {a}, codelines: {codelines}")  

    def py_main():    
        a = 0
        def main():
            a = 10
            def test():
                global a                               # global a inside test means Go to the global scope of main.py
                a = 20
            test()
            print(a)                                   # a = 10 

        main()
        print(a)                                       # a = 20
### EndofCodeSection###
