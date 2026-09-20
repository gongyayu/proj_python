from py_mod import line_print, st_print, st_code, st_markline


### StartofFunc###

def py_calculation():
    # Calculate: +, -, *, /, %, //
    a = 17
    b = 5
    st_code(
        f"(a / b) -> {(a / b)}, (a % b) -> {(a % b)}, (a // b) -> {(a // b)}")
### EndofCodeSection###


def py_compare():
    # Compare: >,>=, <, <=, ==, != 
    # Combine: and, or, not
    # is and ==
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]

    # compare vlues
    st_code(f"a == b -> {a == b}")                                 # => True
    st_code(f"a == c -> {a == c}")                                 # => True
    # compare location
    st_code(f"a {id(a)} is b {id(b)} -> {a is b}")                 # => True
    # => False
    st_code(f"a {id(a)} is c {id(c)} -> {a is c}")
### EndofCodeSection###


def py_equality():
    # Equality
    age = 25
    # True - equals
    st_code(f"age == 25 -> {age == 25}")
    # True - not equals
    st_code(f"age != 30 -> {age != 30}")

    # Greater/Less than
    # True - greater than
    st_code(f"age > 20 -> {age > 20}")
    # True - less than
    st_code(f"age < 30 -> {age < 30}")
    # True - greater or equal
    st_code(f"age >= 25 -> {age >= 25}")
    # True - less or equal
    st_code(f"age <= 25 -> {age <= 25}")
### EndofCodeSection###


def py_bitwise():
    def bitwise():
        a = 7               # 101 in binary
        b = 3               # 011 in binary
        st_code(f"a & b: {a & b}")      # Output: 1 (001 in binary)
    bitwise()
    st_markline()

    def bitmask():
        color = 0x00FF0000     # 16711680 in decimal (blue color)
        mask = 0x000000FF      # 255 in decimal (red color mask)
        # Output: 16711680 (blue color remains unchanged)
        st_code(f"color * mask: {color & mask}")
    bitmask()
    st_markline()

    def bitbool():
        a = True
        b = False
        st_code(f"a & b: {a & b}")
    bitbool()
    st_markline()

    def bitlist():
        var = {1, 2, 3} & {3, 4, 5}
        st_code(f"{var}")
    bitlist()
    st_markline()

    def bitpandas():
        import pandas as pd
        df = pd.DataFrame(
            {
                'A':[1,2,3],
                'B':[4,5,6]
            }
        )
        result = df[(df['A'] > 1) & (df['B'] < 6)]
        st_code(f"result: {result}")   
    bitpandas()
### EndofCodeSection###

def py_walrus():
    # It lets you assign a value to a variable inside an expression, rather than on a separate line. see reference for more
    with open ('/etc/hosts', 'r') as fr:
        while (line := fr.readline()):
            st_code(f"line: {line}")
### EndofCodeSection###            

    
    

