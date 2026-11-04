from py_mod import line_print,st_print,st_code,code_print, st_markline
import streamlit as st

### StartofFunc###
def py_logging():
    import logging
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    logging.debug('Start of program')

    def factorial(n):
        logging.debug("Start of factorial(%s)" %(n))
        total = 1
        for i in range(1, n + 1):                      # right one should be (1, n+1)
            total *= i
            logging.debug('i is %s, total is %s' % (1, total))
        return total
    
    print(factorial(5))
    logging.debug('End of program')  
py_logging()   

### EndofCodeSection###