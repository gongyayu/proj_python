from py_mod import line_print,st_print,st_code,code_print,codelines, st_markline

### StartofFunc###

def py_try():
    global codelines
    tinydict = {}
    # delete the entire dictionary
    del tinydict
    try:
        st_code(f"tinydict -> {tinydict}")
    except Exception as e:
        st_code(f"Error: {str(e)}")
    st_markline()

    try:
        with open("test.txt") as fh:
            codelines = f"file open successful"
            pass
    except Exception as e:
        st_code(f"Error: {str(e)}")
    else:
        codelines = f"\nELSE runs when the TRY works"
    finally:
        st_code(f"{codelines} \nfinal deal always runs")
    st_markline()

    try:
        with open("data/in/Parsing-input.txt") as fh:
            code_print(f"file open successful")
            #pass
    except Exception as e:
        st_code(f"Error: {str(e)}")
    else:
        code_print(f"ELSE runs when the TRY works")
    finally:
        st_code(f"{code_print(codelines)}final deal always runs")
    st_markline()

    try:
        answer = 10/0
        number = int(input('Enter a number: '))
        st_code(f"number -> {number}")
    except Exception as e:
        st_code(f"Error: {str(e)}")
    except ValueError:
        st_code(f"Error: {ValueError}")
### EndofCodeSection###

