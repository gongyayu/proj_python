from py_mod import line_print,st_print,st_code,code_print, st_markline

### StartofFunc###


### EndofCodeSection###

def py_tryA():
    tinydict = {}
    # delete the entire dictionary
    del tinydict
    try:
        st_code(f"tinydict -> {tinydict}")
    except Exception as e:
        st_code(f"Error: {str(e)}")
### EndofCodeSection###

def py_tryB():
    try:
        with open("test.txt") as fh:
            st_code(f"file open successful")
            pass
    except Exception as e:
        st_code(f"Error: {str(e)}")
    else:
        st_code(f"\nELSE runs when the TRY works")
    finally:
        st_code(f"final deal always runs")
### EndofCodeSection###

def py_tryC():
    try:
        with open("data/in/Parsing-input.txt") as fh:
            st_code(f"file open successful")
            #pass
    except Exception as e:
        st_code(f"Error: {str(e)}")
    else:
        st_code(f"ELSE runs when the TRY works")
    finally:
        st_code(f"final deal always runs")
### EndofCodeSection###

def py_tryD():
    try:
        answer = 10/0
        number = int(input('Enter a number: '))
        st_code(f"number -> {number}")
    except Exception as e:
        st_code(f"Error: {str(e)}")
    except ValueError:
        st_code(f"Error: {ValueError}")
### EndofCodeSection###

